from fastapi import FastAPI

app = FastAPI(
    title="AI Smart Workspace and Meeting Manager",
    description="Bilingual (English–Urdu) AI-powered workplace and meeting management system",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "Backend is running successfully 🚀"
    }
