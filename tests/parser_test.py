from unittest import TestCase

from sklearn.linear_model import LinearRegression

from api.operation import ModelOperation, PandasCallOperation, UserAdditionOperation, UserRemovalOperation
from api.parser import OperationParser, OperationType

parser = OperationParser()


class ParserTests(TestCase):

    def test_user_add_parse(self):
        user_id = 1
        name = "heh"
        email = "meh"
        is_demo = True
        result = parser.parse(OperationType.USER_ADDITION, user_id, name, email, is_demo)
        self.assertTrue(isinstance(result, UserAdditionOperation))
        self.assertEqual(name, result.name)
        self.assertEqual(email, result.email)
        self.assertEqual(user_id, result.user_id)
        self.assertEqual(is_demo, result.is_demo)

    def test_user_remove_parse(self):
        user_id = 1
        result = parser.parse(OperationType.USER_REMOVAL, user_id)
        self.assertTrue(isinstance(result, UserRemovalOperation))
        self.assertEqual(user_id, result.user_id)

    def test_parser_call_parse(self):
        user_id = 1
        pandas_call = "head"
        file_path = "1.csv"
        result = parser.parse(OperationType.PANDAS_CALL, user_id, pandas_call, file_path)
        self.assertTrue(isinstance(result, PandasCallOperation))
        self.assertEqual(user_id, result.user_id)
        self.assertEqual(pandas_call, result.pandas_call.call_name)
        self.assertEqual(file_path, result.file_path)

    def test_model_parse(self):
        user_id = 1
        model = "LinReg"
        raw_params = ""
        file_path = "1.csv"
        result = parser.parse(OperationType.MODEL, user_id, model, raw_params, file_path)

        self.assertTrue(isinstance(result, ModelOperation))
        self.assertTrue(isinstance(result.model.model, LinearRegression))
        self.assertEqual({}, result.model.params)
        self.assertEqual(user_id, result.user_id)
        self.assertEqual(file_path, result.file_path)
