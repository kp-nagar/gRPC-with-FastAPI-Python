from fastapi import FastAPI


app = FastAPI(title="Server A")


@app.get("/", tags=["Endpoints"])
async def index():
    return "Server a is running."
