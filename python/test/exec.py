from environ import db_config
from collections import OrderedDict


test = db_config
print("Specific values:")
print('Name: ' + db_config["DB_HOST"])


