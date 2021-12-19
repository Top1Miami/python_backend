from api.entities.model.Model import Model
from api.entities.pandas_call import PandasCall
from api.operation import ModelOperation, PandasCallOperation, UserAdditionOperation, UserRemovalOperation
from api.parser.OperationType import OperationType


class OperationParser:

    def __init__(self):
        self.operation_registry = {
            OperationType.PANDAS_CALL: OperationParser.parse_pandas_call,
            OperationType.MODEL: OperationParser.parse_model,
            OperationType.USER_ADDITION: OperationParser.parse_addition,
            OperationType.USER_REMOVAL: OperationParser.parse_removal
        }

    def parse(self, op_type, *args):
        if op_type not in self.operation_registry:
            raise RuntimeError("Unsupported operation " + str(op_type) + " " + str(args))
        return self.operation_registry[op_type].__call__(*args)

    @staticmethod
    def parse_pandas_call(user_id, call_name, file_path):
        return PandasCallOperation(user_id, PandasCall.get_call_by_name(call_name), file_path)

    @staticmethod
    def parse_model(user_id, model_name, raw_params, file_path):
        params = OperationParser.__parser_parameters(raw_params)
        return ModelOperation(user_id, Model.get_model_by_name(model_name, params), file_path)

    @staticmethod
    def parse_addition(user_id, name, email, is_demo):
        return UserAdditionOperation(user_id, name, email, is_demo)

    @staticmethod
    def parse_removal(user_id):
        return UserRemovalOperation(user_id)

    @staticmethod
    def __parser_parameters(params):
        if not params:
            return {}
        param_dict = {}
        params_pair_split = params.split(',')
        for params_pair in params_pair_split:
            param = params_pair.split('!')
            param_dict[param[0]] = param[1]
        return param_dict
