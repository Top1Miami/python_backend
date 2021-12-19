from sklearn.linear_model import LinearRegression


class Model:
    model_mapper = {"LinReg": LinearRegression()}

    def __init__(self, model, model_name, params, scoring='neg_mean_squared_error', cv=3):
        self.model = model
        self.model_name = model_name
        self.params = params
        self.scoring = scoring
        self.cv = cv
        self.set_params(params)

    def set_params(self, params):
        self.model.set_params(**params)

    @staticmethod
    def get_model_by_name(model_name, params):
        return Model(Model.model_mapper[model_name], model_name, params)

    @staticmethod
    def get_supported_models():
        return Model.model_mapper.keys()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.params, self.scoring, self.cv) == (other.params, other.scoring, other.cv)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((str(self.params), self.scoring, self.cv))
