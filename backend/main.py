from api.routes import router
from database import Base, engine
from fastapi import FastAPI

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
