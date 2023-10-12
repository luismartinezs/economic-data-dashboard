import os
from dotenv import load_dotenv
import quandl

# Load environment variables from .env file
load_dotenv()

# Set your API key
quandl.ApiConfig.api_key = os.getenv('QUANDL_API_KEY')

# Get data
data = quandl.get("ODA/ESP_LUR", start_date="2000-01-01", end_date="2020-12-31")

# Print data
print(data)

# Get metadata
metadata = quandl.Dataset('ODA/ESP_LUR').data_fields()

# Print metadata
print(metadata)