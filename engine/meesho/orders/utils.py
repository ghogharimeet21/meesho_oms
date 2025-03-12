import os
from typing import Dict, Union

class OrderProcessor:
    def __init__(self):
        self.order_mapper: Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Union[int, float, str]]]]]] = {}

    def convert_data_type(self, value: str) -> Union[int, float, str]:
        """Converts string to int, float, or keeps it as str."""
        if value.replace(".", "", 1).isdigit():  # Check if it's a number
            return float(value) if "." in value else int(value)
        return value  # Keep as string if not a number

    def add_order(self, row_list, header):
        """Processes a row and adds it to the order metadata with correct data types."""
        product_name = row_list[4]  # 'Product Name'
        order_date = row_list[2]  # 'Order Date'
        sub_order_no = row_list[1]  # 'Sub Order No'
        packet_id = row_list[-1]  # 'Packet Id'

        product_details = {
            header[i]: self.convert_data_type(row_list[i])  # Convert to correct type
            for i in range(len(header))
            if i not in [1, 2, 4, -1]  # Exclude keys used for mapping
        }

        # Build nested dictionary
        if product_name not in self.order_mapper:
            self.order_mapper[product_name] = {}

        if order_date not in self.order_mapper[product_name]:
            self.order_mapper[product_name][order_date] = {}

        if sub_order_no not in self.order_mapper[product_name][order_date]:
            self.order_mapper[product_name][order_date][sub_order_no] = {}

        if packet_id not in self.order_mapper[product_name][order_date][sub_order_no]:
            self.order_mapper[product_name][order_date][sub_order_no][packet_id] = product_details

    def load_data(self, file_path: str):
        """Reads CSV file and processes orders."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as f:
            lines = f.readlines()

        header = [col.strip('"') for col in lines[0][:-1].split(",")]

        for row in lines[1:]:
            row_list = [col.strip('"') for col in row[:-1].split(",")]
            self.add_order(row_list, header)  # Use the class method

        return self.order_mapper  # Return structured order data

# Global instance
order_processor = OrderProcessor()