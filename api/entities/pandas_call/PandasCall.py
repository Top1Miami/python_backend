class PandasCall:
    pd_mapper = {"head": lambda x: x.head(), "tail": lambda x: x.tail()}

    def __init__(self, call_name, call_func):
        self.call_name = call_name
        self.call_func = call_func

    @staticmethod
    def get_call_by_name(call_name):
        return PandasCall(call_name, PandasCall.pd_mapper[call_name])

    @staticmethod
    def get_supported_calls():
        return PandasCall.pd_mapper.keys()
