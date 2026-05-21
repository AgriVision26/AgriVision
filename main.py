from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# ✅ Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ SERVE YOUR FRONTEND (VERY IMPORTANT)
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

# ✅ HEALTH CHECK
@app.get("/status")
def status():
    return {"status": "running"}

# ✅ ANALYZE ENDPOINT (MULTIPLE DETECTIONS)
@app.post("/analyze")
async def analyze_image(file: UploadFile):
    contents = await file.read()

    # ✅ Simulated detections (replace with real AI later)
    return {
        "detections": [
            {
                "issue": "Chlorosis",
                "confidence": 0.65,
                "bbox": [100, 100, 250, 250]
            },
            {
                "issue": "Leaf Burn",
                "confidence": 0.72,
                "bbox": [300, 150, 450, 300]
            }
        ]
    }