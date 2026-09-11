from fastapi import FastAPI

app = FastAPI(
    title="InvestIQ API",
    description="API para la plataforma de análisis financiero InvestIQ",
    version="1.0.0"
)

@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok", "message": "InvestIQ API is running"}
