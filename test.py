from main import parser_parameters, read_file, fit_model, load_file, fit_loaded, pandas_op, pandas_loaded
import pytest
import pandas as pd


def test_unit_first():
	res1 = parser_parameters("key=1")
	assert res1 == {"key":"1"}

def test_unit_second():
	res2 = parser_parameters("")
	assert res2 == {}

def test_unit_third():
	res3 = parser_parameters("key=1,value=2")
	assert res3 == {"key":"1", "value":"2"}


def test_int_first():
	pd_file = read_file("1.csv")
	res1 = fit_model(pd_file, "LinReg", "")
	assert 'score' in res1 
	assert len(res1['score']) == 3 # cv == 3, so size eq 3

def test_int_second():
	load_file("1.csv")
	res1 = fit_loaded(0, "LinReg", "")
	assert 'score' in res1 
	assert len(res1['score']) == 3 # cv == 3, so size eq 3

def test_int_third():
	res = pandas_op("1.csv", "head")
	assert "result" in res
	assert isinstance(res["result"], pd.DataFrame)
	assert res["result"].size == 30
	load_file("1.csv")
	res = pandas_loaded(0, "head")