import sqlite3, os, yaml, re

DB_PATH = "walkgis.db"
FEATURE_DIR = "features"
MAP_DIR = "maps"

def sync():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. 初始化圖層 (Layers)
    layers_map = {}
    for cat in ["美食", "服務據點", "人文史蹟", "日常"]:
        cur.execute("INSERT OR IGNORE INTO layers (layer_type, layer_subtype) VALUES (?, ?)", (cat, "台東賦能案例"))
        cur.execute("SELECT layer_id FROM layers WHERE layer_type = ? AND layer_subtype = ?", (cat, "台東賦能案例"))
        layers_map[cat] = cur.fetchone()[0]

    # 2. 同步 Features
    for f_name in os.listdir(FEATURE_DIR):
        if not f_name.endswith(".md"): continue
        path = os.path.join(FEATURE_DIR, f_name)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            parts = content.split("---")
            if len(parts) >= 3:
                try:
                    meta = yaml.safe_load(parts[1])
                    if not meta: continue
                    body = "---".join(parts[2:])
                    f_id = str(meta.get("id", f_name.replace(".md", "")))
                    f_name_zh = meta.get("name") or meta.get("title") or f_name.replace(".md", "")
                    wkt = meta.get("geometry_wkt", "POINT(0 0)")
                    f_cat = meta.get("type", "日常")
                    l_id = layers_map.get(f_cat, layers_map["日常"])
                    g_type = "Point" if "POINT" in wkt.upper() else "LineString"
                    
                    cur.execute("""
                        INSERT OR REPLACE INTO walking_map_features (feature_id, name, description, layer_id, geometry_type, geometry_wkt) 
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (f_id, f_name_zh, body.strip(), l_id, g_type, wkt))
                except Exception as e:
                    print(f"Skipping {f_name}: {e}")

    # 3. 同步 Maps
    for m_name in os.listdir(MAP_DIR):
        if not m_name.endswith(".md"): continue
        path = os.path.join(MAP_DIR, m_name)
        m_id = m_name.replace(".md", "")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            parts = content.split("---")
            if len(parts) >= 3:
                try:
                    meta = yaml.safe_load(parts[1])
                    if not meta: continue
                    desc = "---".join(parts[2:])
                    title = meta.get("title") or meta.get("name") or m_id
                    cover = meta.get("cover_image", "")
                    
                    cur.execute("""
                        INSERT OR REPLACE INTO walking_maps (map_id, name, description, cover_image) 
                        VALUES (?, ?, ?, ?)
                    """, (m_id, title, desc.strip(), cover))
                    
                    # 自動建立 Relation
                    cur.execute("SELECT feature_id FROM walking_map_features")
                    all_fids = [r[0] for r in cur.fetchall()]
                    for fid in all_fids:
                        cur.execute("INSERT OR IGNORE INTO walking_map_relations (map_id, feature_id) VALUES (?, ?)", (m_id, fid))
                except Exception as e:
                    print(f"Skipping map {m_name}: {e}")

    conn.commit()
    conn.close()
    print("Independent DB Sync (v2 Schema) Complete.")

if __name__ == "__main__":
    sync()
