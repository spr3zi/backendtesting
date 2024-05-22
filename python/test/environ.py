import os
from dotenv import dotenv_values
from dotenv import load_dotenv
from collections import OrderedDict

load_dotenv()

#print('Dict Values')
db_config = dotenv_values()
#print(db_config)
#print(db_config.keys())
#for key, value in db_config.items():
    #print(f"{key}: {value}")

#print("Specific values:")
#print('Name: ' + db_config["DB_HOST"])
#print('Age: ' + db_config["DB_PORT"])

