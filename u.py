from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request body model
class User(BaseModel):
    name: str
    age: int


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}"
    }


@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
