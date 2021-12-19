from unittest import TestCase

from api import ModelOperation, OperationType
from server.application.ServerConfiguration import ServerConfiguration


class ServiceTest(TestCase):

    def setUp(self):
        self.server_configuration = ServerConfiguration()
        self.parser = self.server_configuration.parser
        self.service = self.server_configuration.service
        self.db_handler = self.server_configuration.db_handler

    def create_user_add(self, user_id=1, email="meh", is_demo=True):
        return self.parser.parse(OperationType.USER_ADDITION, user_id, "heh", email, is_demo)

    def create_user_rem(self, user_id=1):
        return self.parser.parse(OperationType.USER_REMOVAL, user_id)

    def test_user_add_parse(self):
        user_add = self.create_user_add()
        result = self.service.execute_operation(user_add)
        self.assertEqual({"result": "User added 1"}, result)
        user = self.db_handler.get_user(user_add.user_id)
        self.assertEqual(user_add.user_id, user[0])
        self.assertEqual(user_add.name, user[1])
        self.assertEqual(user_add.email, user[2])
        self.assertEqual(user_add.is_demo, user[3])

    def test_remove_user(self):
        user_add = self.create_user_add()
        self.service.execute_operation(user_add)
        user_rem = self.create_user_rem()
        result = self.service.execute_operation(user_rem)
        self.assertEqual({"result": "User removed 1"}, result)
        all_users = self.db_handler.get_all_users()
        self.assertEqual(0, len(all_users))

    def test_pandas_call(self):
        user_add = self.create_user_add(is_demo=False)
        self.service.execute_operation(user_add)
        user_id = user_add.user_id
        pandas_call_op = self.parser.parse(OperationType.PANDAS_CALL, user_id, "head", ".\\..\\1.csv")
        result = self.service.execute_operation(pandas_call_op)
        self.assertTrue("result" in result)
        user = self.db_handler.get_user(user_id)
        self.assertEqual(5, user[4])

        user_add = self.create_user_add(user_id=2, email="neh")
        self.service.execute_operation(user_add)
        user_id = user_add.user_id
        pandas_call_op = self.parser.parse(OperationType.PANDAS_CALL, user_id, "head", ".\\..\\1.csv")
        result = self.service.execute_operation(pandas_call_op)
        self.assertTrue("result" in result)
        user = self.db_handler.get_user(user_id)
        self.assertEqual(4, user[4])

    def test_model(self):
        user_add = self.create_user_add(is_demo=False)
        self.service.execute_operation(user_add)
        user_id = user_add.user_id
        model = self.parser.parse(OperationType.MODEL, user_id, "LinReg", "", ".\\..\\1.csv")
        result = self.service.execute_operation(model)
        self.assertTrue("score" in result)
        user = self.db_handler.get_user(user_id)
        self.assertEqual(5, user[4])
        # test cache
        cache_dict = self.service.operation_registry[ModelOperation].cache.cache_dict
        self.assertEqual(1, len(cache_dict))
        self.assertTrue((model.model, model.file_path) in cache_dict)

        user_add = self.create_user_add(user_id=2, email="neh")
        self.service.execute_operation(user_add)
        user_id = user_add.user_id
        model = self.parser.parse(OperationType.MODEL, user_id, "LinReg", "", ".\\..\\1.csv")
        result = self.service.execute_operation(model)
        self.assertTrue("score" in result)
        user = self.db_handler.get_user(user_id)
        self.assertEqual(4, user[4])
