class CacheWrapper:
    def __init__(self):
        self.cache_dict = {}

    def get_value(self, cache_id, function, *args):
        if cache_id not in self.cache_dict:
            self.cache_dict[cache_id] = function.__call__(*args)
        return self.cache_dict[cache_id]
