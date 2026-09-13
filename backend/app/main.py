from fastapi import FastAPI

app = FastAPI(
    title="ForgingValue API",
    description="API para la plataforma de análisis fundamental y valoración financiera ForgingValue",
    version="1.0.0"
)

@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok", "message": "ForgingValue API is running"}
