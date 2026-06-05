python
import requests
import json
import pandas as pd
from datetime import datetime

# Example API URLs for getting real-time data
TRAFFIC_API_URL = 'https://api.abudhabi.gov/traffic-data'
AIR_QUALITY_API_URL = 'https://api.abudhabi.gov/air-quality'

# Fetch real-time traffic data
def get_traffic_data():
    response = requests.get(TRAFFIC_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching traffic data: {response.status_code}")
        return None

# Fetch real-time air quality data
def get_air_quality_data():
    response = requests.get(AIR_QUALITY_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching air quality data: {response.status_code}")
        return None

# Combine data and save to a CSV file
def save_combined_data_to_csv():
    traffic_data = get_traffic_data()
    air_quality_data = get_air_quality_data()

    if traffic_data and air_quality_data:
        # Create DataFrames for both datasets
        df_traffic = pd.DataFrame(traffic_data)
        df_air_quality = pd.DataFrame(air_quality_data)

        # Merge datasets on a common key, e.g., location
        combined_data = pd.merge(df_traffic, df_air_quality, on='location', how='outer')

        # Save combined data to CSV
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'combined_data_{timestamp}.csv'
        combined_data.to_csv(file_name, index=False)
        print(f"Combined data saved to {file_name}")
    else:
        print("Failed to fetch data for combining.")

# Run the script
if __name__ == "__main__":
    save_combined_data_to_csv()
