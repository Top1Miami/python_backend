from typing import Optional

import pandas as pd
from fastapi import FastAPI
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

pd_mapper = {"head": lambda x: x.head(), "tail": lambda x: x.tail()}
model_mapper = {"LinReg": LinearRegression()}


# open file locally and print head
# @app.get("/pandas_op/")
def pandas_op(file_name: str, pandas_operation: str):
    pd_file = read_file(file_name)
    return pandas_abstract(pd_file, pandas_operation)


def pandas_abstract(pd_file, pandas_operation):
    pd_func = pd_mapper[pandas_operation]
    return {"result": pd_func(pd_file)}


def read_file(file_name):
    return pd.read_csv(file_name, sep=',')


# fit model_name with file_name
# @app.get("/fit/")
def fit(file_name: str, model_name: str, model_params: str):
    pd_file = read_file(file_name)
    return fit_model(pd_file, model_name, model_params)


def fit_model(pd_file, model_name, model_params):
    params = parser_parameters(model_params)
    model = model_mapper[model_name]
    model.set_params(**params)
    return {"score": count_cv(model, pd_file)}


def count_cv(model, pd_file):
    return cross_val_score(model, pd_file, pd_file['mark'].to_numpy(), scoring='neg_mean_squared_error', cv=3)


def parser_parameters(params):
    if not params:
        return {}
    param_dict = {}
    params_pair_split = params.split(',')
    for params_pair in params_pair_split:
        param = params_pair.split('=')
        param_dict[param[0]] = param[1]
    return param_dict


loaded_files = []


# @app.post("/load_file/")
def load_file(file_name: str):
    loaded_files.append(read_file(file_name))
    return {"loaded_file": file_name, "file_id": len(loaded_files) - 1}


# @app.get("/fit_loaded/")
def fit_loaded(file_id: int, model_name: str, model_params: Optional[str] = ""):
    if len(loaded_files) <= file_id:
        return {"error": "wrong id"}
    return fit_model(loaded_files[file_id], model_name, model_params)


def pandas_loaded(file_id: int, pandas_operation: str):
    return pandas_abstract(loaded_files[file_id], pandas_operation)
