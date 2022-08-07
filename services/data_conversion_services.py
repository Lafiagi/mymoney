class DataConverter:
    '''
        Takes a list of strings of float or int
        and convert to the respective data type
    '''
    @staticmethod
    def convert_to_int(data: list) -> list:
        data = map(int, data)
        data = list(data)
        return data
    
    @staticmethod
    def convert_to_float(data: list) -> list:
        data = map(float, data)
        data = list(data)
        return data