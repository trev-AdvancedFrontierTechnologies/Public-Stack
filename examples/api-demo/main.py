from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="AFT Public Software Demo", version="0.1.0")

@app.get("/")
def root():
    return {
        "company": "Advanced Frontier Technologies",
        "uei": "W2MEEUJACRJ3",
        "cage": "1ZV02",
        "posture": "prototype-backed, validation-first, evidence-controlled",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/governance/status")
def governance_status():
    return {
        "mode": "public-safe-demo",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "claims": [
            "prototype-backed",
            "validation-first",
            "evidence-controlled"
        ]
    }

@app.get("/agents")
def agents():
    return {
        "count": 21,
        "public_safe": True,
        "agents": [f"smileqt_agent_{i:02d}" for i in range(1, 22)]
    }

@app.post("/simulate")
def simulate(payload: dict):
    return {
        "mode": "stub",
        "input": payload,
        "result": "demo-only; not certified simulation output"
    }
