# 🌍 台東旅宿業者賦能案例 (WalkGIS Data Showcase)

歡迎來到 **台東旅宿業者賦能實踐案例** 專案！本 Repo 是專為台東在地旅宿業者、地方文化推廣人員設計的「軟體定義地圖 (SDM)」示範工程。

本專案將 2026 年「台東自造」 AI 賦能講堂的教學轉化為實體資產，展示了如何利用 AI 助理與 WalkGIS 協議，將零散的在地點位厚化為具備「地景解碼」深度的數位導覽。

## 📍 專案核心亮點

*   **實例民宿**：以「愛上台東藍民宿」為核心樞紐，向外擴散 35+ 個特色點位。
*   **深度解碼**：內容涵蓋台東天后宮碑文、卑南流域地理、大鳥村圖騰、在地美食心法。
*   **去中心化**：資料存放於 GitHub，完全由創作者自主掌握（Digital Sovereignty）。

## 🚀 快速瀏覽指南

### 1. 立即進入地圖 (WalkGIS Web App)
點擊下方連結，您可以直接在 WalkGIS App 中開啟這個專屬地圖：

[**👉 2026 台東市旅宿業者賦能實踐地圖**](https://walkgis-544663807110.us-west1.run.app/?node=official&map=2026_taitung_city_enablement_case)

### 2. 學習如何製作
如果您想了解這些資料是如何產製的，可以參考本專案的目錄結構：
*   **`features/`**: 每個點位的 Markdown 檔案，是 AI 協助搜集並撰寫的「深度故事」。
*   **`maps/`**: 地圖定義檔，包含 AI 智慧行程 Prompt 與 Mermaid 空間架構圖。
*   **`walkgis.db`**: SQLite 資料庫，提供高效的空間檢索索引。

## 🤖 賦能技術路徑 (SDM Workflow)

本專案全程採用以下 AI 協作流程產製：
1.  **清單採集**：搜集業者與學員感興趣的台東生活圈點位。
2.  **批次編碼**：利用 Google Maps API 批次獲取精確座標與基本資訊。
3.  **內容厚化**：引導 AI 根據「台東自造」講堂心法，為每個點位撰寫解說與導覽建議。
4.  **自動化固化**：執行 `scripts/sync_walkgis_db.py` 確保 Markdown 與 DB 同步。

## 📂 目錄結構
*   **`features/`**: 景點深度故事 (Markdown)。
*   **`maps/`**: 地圖整合定義。
*   **`assets/images/`**: 地圖封面與視覺影像。
*   **`scripts/`**: 自動化同步工具。

---
## 🔗 相關資源
*   [台東自造 YouTube 直播實況](https://www.youtube.com/watch?v=9RWWi2h0XQ8)
*   [WalkGIS 官方部落格：演講心法紀錄](https://wuulong.github.io/wuulong-notes-blog/posts/20260417_taitung_lecture_mindset/)
*   [WalkGIS App](https://walkgis-544663807110.us-west1.run.app/)

---
*Powered by WalkGIS Protocol & BMad Agentic System*
