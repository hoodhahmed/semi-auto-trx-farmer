from main import debug_print

class NotJsonError(Exception):
    """Exception raised when a file is not a json file."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.message = f"{file_path} is not a json file."
        super().__init__(self.message)
        debug_print(self.message)
        
