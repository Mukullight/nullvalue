import pandas as pd
import xml.etree.ElementTree as ET
############### loading the required files #############################################
################# formatting it to the required format ################################

def load_to_df(file_path):
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


#################### passing the data frame ##################################
################### spotting the location of the outliers #####################



def nulls_and_outs(df, q1=0.25, q3=0.75):
    """
    Finds the locations of null values and outliers in a DataFrame, and drops columns with categorical variables.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    q1 (float): The lower quartile value.
    q3 (float): The upper quartile value.

    Returns:
    dict: A dictionary with two keys 'nulls' and 'outliers', each containing the locations of null values and outliers respectively.
    pd.DataFrame: The DataFrame after dropping categorical columns.
    """
    # Drop categorical columns
    df = df.select_dtypes(exclude=['object', 'category'])

    null_locations = {}
    outlier_locations = {}
    
    # Identify null values
    nulls = df.isnull()
    for col in df.columns:
        null_indices = nulls.index[nulls[col]].tolist()
        if null_indices:
            null_locations[col] = null_indices
    
    # Identify outliers using IQR method
    for col in df.select_dtypes(include=[pd.np.number]).columns:  # Consider only numeric columns
        Q1 = df[col].quantile(q1)
        Q3 = df[col].quantile(q3)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        if not outliers.empty:
            outlier_locations[col] = outliers.index.tolist()
    
    return {
        'nulls': null_locations,
        'outliers': outlier_locations
    }, df





"""
data = {
    'A': [1, 2, 3, None, 5, 100],
    'B': [10, 12, None, 14, 16, 18],
    'C': ['cat', 'dog', 'cat', 'dog', 'cat', 'dog'],
    'D': [1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

result, df_cleaned = find_nulls_and_outliers(df, q1=0.25, q3=0.75)
print("Null values:", result['nulls'])
print("Outliers:", result['outliers'])
print("DataFrame after dropping categorical columns:")
print(df_cleaned)







"""


