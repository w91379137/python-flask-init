
'''

https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

'''

import os

FlaskHost = os.getenv('FLASKHOST', "0.0.0.0")
FlaskPort = os.getenv('FLASKPORT', "5000")