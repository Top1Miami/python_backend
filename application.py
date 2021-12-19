from fastapi import FastAPI

from server.application.ServerConfiguration import ServerConfiguration

app = FastAPI()
configuration = ServerConfiguration()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/user_add/")
def add_user(user_id: int, name: str, email: str, is_demo: bool):
    return {"user_id": user_id, "name": name, "email": email, "is_demo": is_demo}
