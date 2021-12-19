class PandasCallOperation:
    def __init__(self, user_id, pandas_call, file_path):
        self.user_id = user_id
        self.pandas_call = pandas_call
        self.file_path = file_path

    def __str__(self):
        return "PandasCallOperation with model " + self.pandas_call.operation_name
