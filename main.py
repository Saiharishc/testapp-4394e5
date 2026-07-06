from fastapi import FastAPI

app = FastAPI()

@app.get("/api/status")
def api_status():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the TestApp API"}
