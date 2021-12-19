class PandasCallService:
    def __init__(self, db_handler, file_provider):
        self.file_provider = file_provider
        self.db_handler = db_handler

    def evaluate(self, operation):
        pandas_call = operation.pandas_call
        pd_file = self.file_provider.get_file_by_name(operation.file_path)
        result, error_value = self.db_handler.minus_launch(operation.user_id)
        if not result:
            return {"error occurred": error_value}
        return {"result": pandas_call.call_func(pd_file)}
