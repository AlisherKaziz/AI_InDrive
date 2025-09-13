# 🚗 Car Condition Detection API (FastAPI + YOLO)

This project is a **FastAPI-based REST API** that uses a **YOLO model** to detect the condition of a car (clean, dirty, damaged, or both).  
It classifies an uploaded image into one of four categories based on detected objects (car, dirt, rust, dent, scratch).

---

## 📦 Features

- **FastAPI** backend with `/check` endpoint (*POST*).
- Accepts image upload (`.jpg`, `.png`).
- Uses **YOLO** model for object detection.
- Returns classification result:
  - `clean_car`
  - `dirty_car`
  - `damaged_car`
  - `damaged_dirty_car`

---

## 🛠 Installation

### 1️⃣ Prerequisites
**Python 3.10** (recommended)  
Check version: 
```bash
python --version
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/AlisherKaziz/AI_InDrive.git
cd AI_InDrive
```

### 3️⃣ Create Virtual Environment
```bash
python -m venv .venv
```
Activate the environment

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 🚀 Run Project
```bash
python -m uvicorn main:app
```