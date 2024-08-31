from urllib.request import urlretrieve
import os
import logging

# Run this:
# /usr/bin/python3 /Users/jeremylau/project-1-individual-jeremlll/scripts/download.py

def download_taxi_data(year, month, output_dir='./data/Landing Layer/Yellow Taxi'):
    """
    Download the NYC taxi data for a given year and month.
    
    Parameters:
    - year: str, the year to download data for (e.g., '2023')
    - month: str or int, the month to download data for (e.g., '12' or 12)
    - output_dir: str, the directory to save the data to (default: '../data/tlc_data')
    """
    # Ensure month is two digits
    month = str(month).zfill(2)
    
    # Construct the URL and output file path
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"
    output_file = os.path.join(output_dir, f"{year}-{month}.parquet")
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download the file
    print(f"Starting download for {year}-{month}...")
    urlretrieve(url, output_file)
    print(f"Completed download for {year}-{month}")



# Specify the output directory
output_relative_dir = './data/Landing Layer/Yellow Taxi'

# Download data for December 2023
download_taxi_data('2023', '12', output_dir=output_relative_dir)

# Download data for January to May 2024
for month in range(1, 6):
    download_taxi_data('2024', month, output_dir=output_relative_dir)



#API for 2023 data
#https://data.cityofnewyork.us/resource/nc67-uf89.csv?$query=SELECT%0A%20%20%60state%60%2C%0A%20%20%60issue_date%60%2C%0A%20%20%60violation_time%60%2C%0A%20%20%60violation%60%2C%0A%20%20%60fine_amount%60%2C%0A%20%20%60penalty_amount%60%2C%0A%20%20%60interest_amount%60%2C%0A%20%20%60reduction_amount%60%2C%0A%20%20%60payment_amount%60%2C%0A%20%20%60amount_due%60%2C%0A%20%20%60precinct%60%2C%0A%20%20%60county%60%0AWHERE%0A%20%20caseless_one_of(%60state%60%2C%20%22NY%22)%0A%20%20AND%20(caseless_contains(%60issue_date%60%2C%20%222023%22)%0A%20%20%20%20%20%20%20%20%20AND%20caseless_contains(%60issue_date%60%2C%20%2212%22))
    

#API for 2024 data
#
    
"""
# Downloading Parking and Camera Violations
output_dir_ticket = './data/Landing Layer/Parking and Camera Violations'

# 2024 Ticket Data
url_tickets_2024 = f"    "
output_file_tickets_2024 = os.path.join(output_dir_ticket, f"2024-ticket.parquet")

# 2023 Ticket Data
url_tickets_2023 = f"    "
output_file_tickets_2023 = os.path.join(output_dir_ticket, f"2023-ticket.parquet")

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir_ticket):
    os.makedirs(output_dir_ticket)

# Download the file
print(f"Starting download for 2024 tickets...")
urlretrieve(url_tickets_2024, output_file_tickets_2024)
print(f"Completed download for 2024 tickets!")

print(f"Starting download for 2024 tickets...")
urlretrieve(url_tickets_2023, output_file_tickets_2023)
print(f"Completed download for 2024 tickets!") """