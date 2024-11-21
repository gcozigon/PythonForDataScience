import time
from datetime import datetime

timenow = time.time()
print(f'Seconds since January 1, 1970 {timenow:,.4f} or {timenow:,.4e} in scientific notation')
print(datetime.now().strftime("%b %d %Y"))