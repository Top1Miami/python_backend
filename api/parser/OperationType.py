from enum import Enum


class OperationType(Enum):
    PANDAS_CALL = 1
    MODEL = 2
    USER_ADDITION = 3
    USER_REMOVAL = 4
