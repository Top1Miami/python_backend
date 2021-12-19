class UserRemovalService:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def evaluate(self, operation):
        self.db_handler.remove_user(operation.user_id)
        return {"result": "User removed " + str(operation.user_id)}
