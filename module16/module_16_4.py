from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
  id: int
  username: str
  age: int


@app.get("/users", response_model=List[User])
async def get_users():
  return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
  user_id = (users[-1].id + 1) if users else 1
  new_user = User(id=user_id, username=username, age=age)
  users.append(new_user)
  return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
  for user in users:
    if str(user.id) == user_id:
      user.username = username
      user.age = age
      return user
  raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
  for i, user in enumerate(users):
    if user.id == user_id:
      deleted_user = users.pop(i)
      return deleted_user
  raise HTTPException(status_code=404, detail="User was not found")
