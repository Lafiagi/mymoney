class DataSanitizer:
    '''
        Takes a strings of and removes new lines,
        percentage signs and empty spaces
    '''
    @staticmethod
    def clean_command(command_parameters: str) -> list:
        cleaned_command: list = command_parameters.strip("\n")
        cleaned_command: list = cleaned_command.replace("%", "")
        cleaned_command: list = cleaned_command.split(" ")[1:]

        return cleaned_command
