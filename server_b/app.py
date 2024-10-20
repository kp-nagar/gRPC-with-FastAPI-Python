from fastapi import FastAPI


app = FastAPI(title="Server B")


@app.get("/", tags=["Endpoints"])
async def index():
    return "Server b is running."
