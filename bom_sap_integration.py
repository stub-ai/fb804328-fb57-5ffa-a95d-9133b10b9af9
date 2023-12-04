import requests
from sap import connection  # Assuming 'sap' is a library for SAP integration

def get_bom_data():
    # Define the URL of your BOM system API
    url = "http://bom_system_api_url"

    # Make a GET request to the BOM system API
    response = requests.get(url)

    # Convert the response to JSON
    data = response.json()

    # Return the data
    return data

def format_bom_data(bom_data):
    # Format the BOM data into the format required by the SAP system
    # This will depend on your specific BOM and SAP systems
    formatted_data = {}

    for item in bom_data:
        formatted_item = {
            "field1": item["field1"],
            "field2": item["field2"],
            # Add more fields as required
        }
        formatted_data.append(formatted_item)

    return formatted_data

def update_sap_system(formatted_data):
    # Connect to the SAP system
    conn = connection.Connection()

    # Update the SAP system with the formatted data
    for item in formatted_data:
        conn.update("endpoint", item)  # Replace "endpoint" with the specific endpoint you need to update

def main():
    # Get the data from the BOM system
    bom_data = get_bom_data()

    # Format the BOM data
    formatted_data = format_bom_data(bom_data)

    # Update the SAP system with the formatted data
    update_sap_system(formatted_data)

if __name__ == "__main__":
    main()