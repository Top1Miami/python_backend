from api.operation import ModelOperation, PandasCallOperation, UserAdditionOperation, UserRemovalOperation
from server.service.ModelService import ModelService
from server.service.PandasCallService import PandasCallService
from server.service.UserAdditionService import UserAdditionService
from server.service.UserRemovalService import UserRemovalService


class OperationService:
    def __init__(self, db_handler, file_provider):
        self.operation_registry = {
            PandasCallOperation: PandasCallService(db_handler, file_provider),
            ModelOperation: ModelService(db_handler, file_provider),
            UserAdditionOperation: UserAdditionService(db_handler),
            UserRemovalOperation: UserRemovalService(db_handler)
        }

    def execute_operation(self, operation):
        return self.operation_registry[operation.__class__].evaluate(operation)
