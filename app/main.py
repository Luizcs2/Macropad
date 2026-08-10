import uvicorn
from .config import settings
from fastapi import FastAPI

app = FastAPI()

def main():
    print("Hello from macropad!")

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host = settings.HOST, port = settings.PORT, reload = True)
