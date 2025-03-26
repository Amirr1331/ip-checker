# GeoTool - Network and IP Information Tool

## Description:
GeoTool is a simple Python tool that allows users to check network status, retrieve their public IP address, get information about an IP, and convert coordinates to Google Maps links and vice versa. It uses the `requests` library to fetch data from APIs and provides real-time network and geolocation data. The tool also logs all actions to a file named `GeoTool_log.txt` for future reference.

## Features:
1. **Check Network Status**: Checks if the network is up by sending a request to Google.
2. **Get My IP**: Retrieves your public IP address.
3. **Get IP Information**: Provides detailed information about any given IP address (location, ISP, etc.).
4. **Convert Coordinates to Map Link**: Converts latitude and longitude coordinates into a Google Maps URL.
5. **Convert Map Link to Coordinates**: Extracts latitude and longitude coordinates from a Google Maps link.
6. **Logging**: All actions are logged to a text file for troubleshooting or future reference.

## Requirements:
To run this tool, you need to install the required dependencies. You can install them using `pip` with the following command:

```bash
pip install -r requirements.txt
python main.py
```