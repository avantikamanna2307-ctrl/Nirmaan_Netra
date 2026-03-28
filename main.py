from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import shutil
import os

app = FastAPI(title="Nirmaan-Netra API")

# This prevents annoying "CORS" errors when we build the Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your custom AI model
print("Loading AI Model...")
model = YOLO("best.pt")
print("Model Loaded Successfully!")

@app.post("/detect")
async def detect_violation(file: UploadFile = File(...)):
    # 1. Save the uploaded image temporarily
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. Run the AI on the image
    results = model(temp_file, conf=0.1) 
    
    # 3. Look at what the AI found
    detections = []
    for r in results:
        for box in r.boxes:
            class_name = model.names[int(box.cls[0])]
            confidence = float(box.conf[0])
            
            # If the AI sees something that is NOT "Covered", flag it!
            if class_name != "Covered":
                detections.append({
                    "material": class_name,
                    "confidence": round(confidence, 2),
                    "status": "ILLEGAL"
                })
    
    # Clean up the temp image so your hard drive doesn't get full
    os.remove(temp_file)

    # 4. Return the result to the Frontend Dashboard
    if len(detections) > 0:
        return {"violation_found": True, "details": detections, "message": "ILLEGAL MATERIAL DETECTED! Notice Ready."}
    else:
        return {"violation_found": False, "message": "Site is compliant."}