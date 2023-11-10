import datetime
import pytz
import csv

# Input timestamp and time zone
#timestamp_str = "2023-10-02 00:52:22"
#input_timezone = "America/Creston"

# Specify the path to the CSV file
csv_file_path = 'grep0x.txt'

# Define a custom sorting key to extract the timestamp for sorting
def custom_sort_key(line):
    timestamp_str, _ = line.split(';')
    return timestamp_str

with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file, delimiter=' ')
   
    logs_list = []

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        timestamp_str = row[0] + ' ' + row[1]
        input_timezone = row[2]
        letter = chr(int(row[9][1:-1], 16))
        
        # Create a datetime object from the input timestamp and specify the input time zone
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        input_timezone_obj = pytz.timezone(input_timezone)
        localized_timestamp = input_timezone_obj.localize(timestamp)

        # Convert the localized timestamp to UTC
        utc_timezone = pytz.utc
        utc_timestamp = localized_timestamp.astimezone(utc_timezone)

        # Format the result as a string in UTC
        result = utc_timestamp.strftime("%Y-%m-%d %H:%M:%S %Z")

        #print(timestamp_str,result,letter)
        print(result,letter)
