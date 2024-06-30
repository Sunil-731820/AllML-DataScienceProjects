from datetime import datetime

# Example date string
date_str = "2023-01-01"

# Convert the string to a datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Convert the datetime object to a timestamp
timestamp = date_obj.timestamp()

# Print the timestamp
print(timestamp)
print(type(timestamp))
