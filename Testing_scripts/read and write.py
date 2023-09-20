import os
import xml.etree.ElementTree as ET

# Define the namespace for XML elements
ns = {'ixretail': 'http://www.nrf-arts.org/IXRetail/namespace/'}

# Specify the directory containing the XML files
directory_path = 'C:/Users/Admin/Desktop/Uzduotis/main/receipts'

# Get a list of XML files in the directory
xml_files = [file for file in os.listdir(directory_path) if file.endswith('.xml')]

# Iterate through each XML file
for xml_file in xml_files:
    file_path = os.path.join(directory_path, xml_file)
    
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract the specific field names
        today_date_element = root.find(".//ixretail:TransactionID", ns)
        store_id_element = root.find(".//ixretail:UnitID", ns)
        items_sold_element = root.find(".//ixretail:Quantity", ns)
        total_paid_element = root.find(".//ixretail:Total[@TotalType='TransactionNetAmount']", ns)
        total_receipts_element = root.find(".//ixretail:Total[@TotalType='TransactionPurchaseQuantity']", ns)

        # Check if elements were found before accessing their 'text' attribute
        if today_date_element is not None:
            today_date = today_date_element.text[0:8]
        else:
            today_date = "Not found"

        if store_id_element is not None:
            store_id = store_id_element.text
        else:
            store_id = "Not found"

        if items_sold_element is not None:
            items_sold = items_sold_element.text
        else:
            items_sold = "Not found"

        if total_paid_element is not None:
            total_paid = total_paid_element.text
        else:
            total_paid = "Not found"

        if total_receipts_element is not None:
            total_receipts = total_receipts_element.text
        else:
            total_receipts = "Not found"

        # Write the field names to a .txt file with the same name as the XML file
        output_file_path = os.path.splitext(file_path)[0] + '.txt'
        with open(output_file_path, 'w') as f:
            f.write(f"Today's date: {today_date}\n")
            f.write(f"Internal ID of the Store: {store_id}\n")
            f.write(f"Amount of items sold: {items_sold}\n")
            f.write(f"Total amount paid in the receipt: {total_paid}\n")
            f.write(f"Total amount of receipts received from the store: {total_receipts}\n")

        print(f"Processed {xml_file} and saved the field names to {output_file_path}")
    except Exception as e:
        print(f"Error processing {xml_file}: {str(e)}")
