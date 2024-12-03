from os.path import defpath
from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {
  '1': 'Имя: Example, возраст: 18'
}


@app.get("/users")
async def get_users():
  return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
  max_index = str(max(map(int, users.keys())) + 1)
  users[max_index] = f"Имя: {username}, возраст: {age}"
  return f"User {max_index} is registered."


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
  if user_id in users:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'
  return 'User not found'


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
  if user_id in users:
    del users[user_id]
    return f'User {user_id} has been deleted'
  return 'User not found'