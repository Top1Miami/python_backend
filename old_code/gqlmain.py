from graphene import ObjectType, Schema, String, Field, List, Float
from fastapi import FastAPI
from collections import namedtuple
from starlette.graphql import GraphQLApp

FitParametersValueObject = namedtuple("FitParameters", ["key", "value"])
FitQueryObject = namedtuple("FitQuery", ["file_name", "model_name", "parameters", "score"])

class FitParameters(ObjectType):
	key = String()
	value = String()

class FitQuery(ObjectType):
    file_name = String()
    model_name = String()
    parameters = List(FitParameters)
    score = Float()

class Query(ObjectType):
	fit_model = Field(FitQuery)

	def resolve_fit_model(self, info):
		return FitQueryObject(file_name="../1.csv", model_name="LinReg", parameters=[FitParametersValueObject(key="n_jobs", value="4"), FitParametersValueObject(key="copy_X", value="true")], score=0.5)

app = FastAPI()
app.add_route("/", GraphQLApp(schema=Schema(query=Query)))