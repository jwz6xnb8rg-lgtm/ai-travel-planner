from fastapi import FastAPI

app = FastAPI(
    title="AI Travel Planner",
    version="1.0.0"
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/ping")
def ping():
    return {"message": "API funcionando"}
