import pandas as pd


class FileProvider:
    @staticmethod
    def get_file_by_name(file_name):
        return pd.read_csv(file_name, sep=',')
