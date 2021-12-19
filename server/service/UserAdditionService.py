class UserAdditionService:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def evaluate(self, operation):
        self.db_handler.add_user(operation.user_id, operation.name, operation.email, operation.is_demo)
        return {"result": "User added " + str(operation.user_id)}
