import json
from datetime import datetime

class Log:
    def __init__(self, log_db_path="C:/Users/MOHAK/Desktop/TASK/Redesigning Poor Code/json/log.json"):
        self.log_db_path=log_db_path
        with open(self.log_db_path, "r") as file:
            self.data=json.load(file)
            self.logs=self.data["logs"]
    
    def add_log(self,message:str):
        new_log={f"{datetime.now().isoformat()}":message}
        self.logs.append(new_log)
        self.data["logs"]=self.logs
        with open(self.log_db_path,"w") as file:
            json.dump(self.data, file, indent=4)