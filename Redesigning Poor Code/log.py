import json
from datetime import datetime

class Log:
    """
    A class for managing logs.
    """
    def __init__(self, log_db_path="json/log.json"):
        """
        Initializes the Log object.

        Parameters:
            - log_db_path (str): The file path of the log database.
        """
        self.log_db_path=log_db_path
        with open(self.log_db_path, "r") as file:
            self.data=json.load(file)
            self.logs=self.data["logs"]
    
    def add_log(self,message:str):
        """
        Adds a log message to the log database.

        Parameters:
            - message (str): The log message to be added.
        """
        new_log={f"{datetime.now().isoformat()}":message}
        self.logs.append(new_log)
        self.data["logs"]=self.logs
        with open(self.log_db_path,"w") as file:
            json.dump(self.data, file, indent=4)