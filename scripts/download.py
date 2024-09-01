from urllib.request import urlretrieve
import os
import logging

# Run this:
# /usr/bin/python3 /Users/jeremylau/ads-assignment-1/scripts/download.py


def download_taxi_data(year, month, output_dir='./data/Landing Layer/Yellow Taxi'):
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
