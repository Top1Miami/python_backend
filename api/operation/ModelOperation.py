class ModelOperation:
    def __init__(self, user_id, model, file_path):
        self.user_id = user_id
        self.model = model
        self.file_path = file_path

    def __str__(self):
        return "ModelOperation with model " + self.model.model_name
