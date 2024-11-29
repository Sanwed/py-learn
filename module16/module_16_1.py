from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin():
  return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_more(user_id, name, age):
  return {"message": f"Информация о пользователе. Имя: {name}, Возраст: {age}"}


@app.get("/user/{user_id}")
async def user(user_id):
  return {"message": f"Вы вошли как пользователь №{user_id}"}