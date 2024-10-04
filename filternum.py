import pandas as pd


def filternum(csv_input_path, csv_output_path):
    df = pd.read_csv(csv_input_path)
    column_name = 'phone_number'
    start_number = '2547'
    # Checks if row on the phone_number column starts with 2547
    filtered_df = df[df[column_name].astype(str).str.startswith(str(start_number))]
    filtered_df.to_csv(csv_output_path, index=False)

csv_input_path = '/Users/fahimrashid/Desktop/uncleaned.csv'
csv_output_path = '/Users/fahimrashid/Desktop/filternum.csv'

filternum(csv_input_path, csv_output_path)