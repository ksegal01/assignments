# Print as 5/1/2012
from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") 
print(date_str)
