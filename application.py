from fastapi import FastAPI

from api import OperationType
from server.application.ServerConfiguration import ServerConfiguration

app = FastAPI()
configuration = ServerConfiguration(script_path=".\\sql_script.sql")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# example call on localhost http://127.0.0.1:8000/user_add/?user_id=1&name=meh&email=heh&is_demo=true
@app.get("/user_add/")
def add_user(user_id: int, name: str, email: str, is_demo: bool):
    operation = configuration.parser.parse(OperationType.USER_ADDITION, user_id, name, email, is_demo)
    return configuration.service.execute_operation(operation)


# example call on localhost http://127.0.0.1:8000/user_remove/?user_id=1
@app.get("/user_remove/")
def remove_user(user_id: int):
    operation = configuration.parser.parse(OperationType.USER_REMOVAL, user_id)
    return configuration.service.execute_operation(operation)


# example call on localhost http://127.0.0.1:8000/pandas_call/?user_id=1&call_name=head&file_path=.\\1.csv
@app.get("/pandas_call/")
def pandas_call(user_id: int, call_name: str, file_path: str):
    operation = configuration.parser.parse(OperationType.PANDAS_CALL, user_id, call_name, file_path)
    return configuration.service.execute_operation(operation)


# example call on localhost http://127.0.0.1:8000/model/?user_id=1&model_name=LinReg&file_path=.\\1.csv
@app.get("/model/")
def model(user_id: int, model_name: str, file_path: str, params: str = ""):
    operation = configuration.parser.parse(OperationType.MODEL, user_id, model_name, params, file_path)
    return configuration.service.execute_operation(operation)
