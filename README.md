# Nirmaan_Netra
AI Construction Dust &amp; Debris Monitor
# 🏗️ Nirmaan-Netra (Smart Bengal Hackathon)
**AI Construction Dust & Debris Monitor**

### 🚨 The Problem
Unregulated micro-construction sites violate environmental norms by leaving materials uncovered, causing severe localized PM10 air pollution and blocking drains. Municipalities lack the manpower to patrol every lane.

### 💡 Our Solution
Nirmaan-Netra is a lightweight, edge-deployable AI surveillance system. Using dashcams on municipal garbage trucks or citizen smartphones, it automatically detects uncovered construction materials, logs the GPS coordinates, and instantly generates a digital E-Challan (Penalty Notice).

### 🛠️ Tech Stack
* **AI/Computer Vision:** Custom-trained YOLOv8 (Ultralytics)
* **Backend API:** Python, FastAPI, Uvicorn
* **Frontend Dashboard:** HTML5, Vanilla JS, Tailwind CSS
* **Automation:** jsPDF for instant E-Challan generation

### 🚀 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install fastapi uvicorn python-multipart ultralytics`
3. Run the AI server: `uvicorn main:app --reload`
4. Open `index.html` in any web browser.
5. Upload a street image and click "Scan for Violations"!

*Built with ❤️ for the Smart Bengal Hackathon.*
