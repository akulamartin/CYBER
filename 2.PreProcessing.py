import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_data(csv_file, output_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Perform data cleaning (if needed)
    # Example: Drop any rows with missing values
    df.dropna(inplace=True)

    # Perform normalization of numerical features (if needed)
    # Example: Normalize the 'timestamp' column
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = (df['timestamp'] - df['timestamp'].min()) / (df['timestamp'].max() - df['timestamp'].min())

    # Perform encoding of categorical variables (if needed)
    # Example: Encode the 'event_type' column
    label_encoder = LabelEncoder()
    df['event_type'] = label_encoder.fit_transform(df['event_type'])

    # Save the preprocessed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Preprocessed data saved to {output_file}.")

def main():
    # Specify the path to the input CSV file
    csv_file = 'cybersecurity_logs.csv'

    # Specify the path to the output CSV file
    output_file = 'preprocessed_data.csv'

    # Perform data preprocessing and save the preprocessed data
    preprocess_data(csv_file, output_file)

if __name__ == '__main__':
    main()
