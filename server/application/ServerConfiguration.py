from api import FileProvider
from api.parser.OperationParser import OperationParser
from server.db_handler import DBHandler
from server.service import OperationService


class ServerConfiguration:
    def __init__(self):
        self.db_handler = DBHandler()
        self.file_provider = FileProvider()
        self.parser = OperationParser()
        self.service = OperationService(self.db_handler, self.file_provider)
