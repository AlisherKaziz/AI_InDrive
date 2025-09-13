from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import numpy as np
import cv2
import uvicorn

model = YOLO("best.pt")

app = FastAPI()

@app.post("/check")
async def check_car(file: UploadFile = File(...)):
    image_bytes = await file.read()

    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # img is now a proper numpy array (BGR)

    if img is None:
        return {"error": "Could not decode image"}

    # Run YOLO prediction
    results = model.predict(source=img, conf=0.02, verbose=False)

    # Counters
    car_count = rust_count = dunt_count = scratch_count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])  # class index
            cls_name = r.names[cls_id]  # class label
            if cls_name == "car":
                car_count += 1
            elif cls_name == "rust":
                rust_count += 1
            elif cls_name == "dunt":
                dunt_count += 1
            elif cls_name == "scratch":
                scratch_count += 1

    # Decision logic
    damaged = (dunt_count > 0 or scratch_count > 0)
    dirty = (rust_count > 0)
    if car_count > (rust_count + dunt_count + scratch_count):
        return {"status": "clean_car"}
    else:
        if damaged and dirty:
            return {"status": "damaged_dirty_car"}
        elif damaged:
            return {"status": "damaged_car"}
        elif dirty:
            return {"status": "dirty_car"}
        else:
            return {"error": "Could not recognize image"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, workers=2)