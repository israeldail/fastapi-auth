from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="FastAPI Auth", version="1.0.0", docs_url="/docs", redoc_url="/redocs"
)


@app.get("/")
def root():
    return {"Hello": "There"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
