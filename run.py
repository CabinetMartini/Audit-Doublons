import uvicorn # type: ignore

if __name__ == "__main__":
    uvicorn.run(
        "app.internal.main:app",
        host="localhost",
        port=8022,
        log_level="info",
        reload=True,
    )