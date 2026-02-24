import uvicorn # type: ignore

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8080,
        log_level="info",
        reload=True,
    )