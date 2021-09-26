from fastapi import FastAPI

from app.routers import shipment, harbor

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello, world!"}

app.include_router(
    router=shipment.router,
    prefix="/shipment",
    tags=['shipment']
)
app.include_router(
    router=harbor.router,
    prefix="/harbor",
    tags=["harbor"]
)


if __name__ == "__main__":
    import uvicorn
    print("Starting shipping-service")
    uvicorn.run(app, host="0.0.0.0", port=8000)