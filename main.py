from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="APIs Trabajo 5 MLOps", version="0.0.1")


list_users = {}


class User(BaseModel):
    username: str
    email: str
    password: str


@app.post("/api/v1/register")
def register_user(user: User):
    if user.username in list_users:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    list_users[user.username] = user
    return {"message": "Usuario registrado exitosamente"}

