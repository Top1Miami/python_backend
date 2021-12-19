from sklearn.model_selection import cross_val_score

from server.cache_wrapper.CacheWrapper import CacheWrapper


class ModelService:
    LABEL_FIELD_NAME = 'mark'

    def __init__(self, db_handler, file_provider):
        self.file_provider = file_provider
        self.db_handler = db_handler
        self.cache = CacheWrapper()

    def evaluate(self, operation):
        configured_model = operation.model
        pd_file = self.file_provider.get_file_by_name(operation.file_path)
        result, error_value = self.db_handler.minus_launch(operation.user_id)
        if not result:
            return {"error occurred": error_value}

        cached_result = self.cache.get_value((configured_model, operation.file_path),
                                             ModelService.count_cv, configured_model.model, pd_file,
                                             configured_model.scoring, configured_model.cv)
        return {"score": cached_result}

    @staticmethod
    def count_cv(model, pd_file, scoring='neg_mean_squared_error', cv=3):
        return cross_val_score(model, pd_file, pd_file[ModelService.LABEL_FIELD_NAME].to_numpy(),
                               scoring=scoring, cv=cv)
