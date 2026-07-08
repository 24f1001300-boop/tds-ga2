from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid

app = FastAPI()

# Allow ONLY the assigned origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dash-n1moaf.example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware for Request ID and Process Time
@app.middleware("http")
async def add_headers(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start

    response.headers["X-Request-ID"] = str(uuid.uuid4())
    response.headers["X-Process-Time"] = f"{process_time:.6f}"

    return response


@app.get("/stats")
def stats(values: str):
    nums = [int(x) for x in values.split(",")]

    return {
        "email": "24f1001300@ds.study.iitm.ac.in",
        "count": len(nums),
        "sum": sum(nums),
        "min": min(nums),
        "max": max(nums),
        "mean": sum(nums) / len(nums),
    }