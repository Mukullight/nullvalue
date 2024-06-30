import pandas as pd
import xml.etree.ElementTree as ET

def load_file_to_dataframe(file_path):
    """
    Load data from CSV, XML, Excel, or JSON file into a Pandas DataFrame.

    Parameters:
    - file_path (str): Path to the file to be loaded.

    Returns:
    - df (DataFrame): Pandas DataFrame containing the loaded data.
    """
    try:
        # Determine file type based on extension
        file_type = file_path.split('.')[-1].lower()

        if file_type == 'csv':
            df = pd.read_csv(file_path)
        elif file_type == 'xml':
            tree = ET.parse(file_path)
            root = tree.getroot()

            data = []
            for item in root.findall('row'):
                row = {}
                for child in item:
                    row[child.tag] = child.text
                data.append(row)

            df = pd.DataFrame(data)
        elif file_type in ['xls', 'xlsx']:
            df = pd.read_excel(file_path, sheet_name='Sheet1')  # Specify sheet name if necessary
        elif file_type == 'json':
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        # Print information about columns
        print(f"Loaded {file_type.upper()} file successfully.")
        print("Columns:")
        print(df.columns)
        
        return df

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    except Exception as e:
        print(f"Error loading file '{file_path}':")
        print(e)
        return None


