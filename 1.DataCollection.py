import csv
from datetime import datetime

def generate_sample_data():
    # Generate a list of sample cybersecurity events
    sample_data = [
        {'source_ip': '192.168.0.1', 'destination_ip': '10.0.0.1', 'timestamp': '2023-05-31 10:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.2', 'destination_ip': '10.0.0.2', 'timestamp': '2023-05-31 11:15:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.3', 'destination_ip': '10.0.0.3', 'timestamp': '2023-05-31 12:45:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.4', 'destination_ip': '10.0.0.4', 'timestamp': '2023-05-31 13:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.5', 'destination_ip': '10.0.0.5', 'timestamp': '2023-05-31 14:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.6', 'destination_ip': '10.0.0.6', 'timestamp': '2023-05-31 15:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.7', 'destination_ip': '10.0.0.7', 'timestamp': '2023-05-31 15:45:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.8', 'destination_ip': '10.0.0.8', 'timestamp': '2023-05-31 16:30:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.9', 'destination_ip': '10.0.0.9', 'timestamp': '2023-05-31 17:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.10', 'destination_ip': '10.0.0.10', 'timestamp': '2023-05-31 18:00:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.11', 'destination_ip': '10.0.0.11', 'timestamp': '2023-05-31 18:45:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.12', 'destination_ip': '10.0.0.12', 'timestamp': '2023-05-31 19:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.13', 'destination_ip': '10.0.0.13', 'timestamp': '2023-05-31 20:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.14', 'destination_ip': '10.0.0.14', 'timestamp': '2023-05-31 21:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.15', 'destination_ip': '10.0.0.15', 'timestamp': '2023-05-31 21:45:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.16', 'destination_ip': '10.0.0.16', 'timestamp': '2023-05-31 22:30:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.17', 'destination_ip': '10.0.0.17', 'timestamp': '2023-05-31 23:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.18', 'destination_ip': '10.0.0.18', 'timestamp': '2023-05-31 23:45:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.19', 'destination_ip': '10.0.0.19', 'timestamp': '2023-05-31 00:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.20', 'destination_ip': '10.0.0.20', 'timestamp': '2023-05-31 01:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.21', 'destination_ip': '10.0.0.21', 'timestamp': '2023-05-31 02:00:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.22', 'destination_ip': '10.0.0.22', 'timestamp': '2023-05-31 02:45:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.23', 'destination_ip': '10.0.0.23', 'timestamp': '2023-05-31 03:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.24', 'destination_ip': '10.0.0.24', 'timestamp': '2023-05-31 04:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.25', 'destination_ip': '10.0.0.25', 'timestamp': '2023-05-31 05:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.26', 'destination_ip': '10.0.0.26', 'timestamp': '2023-05-31 05:45:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.27', 'destination_ip': '10.0.0.27', 'timestamp': '2023-05-31 06:30:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.28', 'destination_ip': '10.0.0.28', 'timestamp': '2023-05-31 07:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.29', 'destination_ip': '10.0.0.29', 'timestamp': '2023-05-31 08:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.30', 'destination_ip': '10.0.0.30', 'timestamp': '2023-05-31 08:45:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.31', 'destination_ip': '10.0.0.31', 'timestamp': '2023-05-31 09:30:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.32', 'destination_ip': '10.0.0.32', 'timestamp': '2023-05-31 10:15:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.33', 'destination_ip': '10.0.0.33', 'timestamp': '2023-05-31 11:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.34', 'destination_ip': '10.0.0.34', 'timestamp': '2023-05-31 11:45:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.35', 'destination_ip': '10.0.0.35', 'timestamp': '2023-05-31 12:30:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.36', 'destination_ip': '10.0.0.36', 'timestamp': '2023-05-31 13:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.37', 'destination_ip': '10.0.0.37', 'timestamp': '2023-05-31 14:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.38', 'destination_ip': '10.0.0.38', 'timestamp': '2023-05-31 14:45:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.39', 'destination_ip': '10.0.0.39', 'timestamp': '2023-05-31 15:30:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.40', 'destination_ip': '10.0.0.40', 'timestamp': '2023-05-31 16:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.41', 'destination_ip': '10.0.0.41', 'timestamp': '2023-05-31 17:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.42', 'destination_ip': '10.0.0.42', 'timestamp': '2023-05-31 17:45:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.43', 'destination_ip': '10.0.0.43', 'timestamp': '2023-05-31 18:30:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.44', 'destination_ip': '10.0.0.44', 'timestamp': '2023-05-31 19:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.45', 'destination_ip': '10.0.0.45', 'timestamp': '2023-05-31 20:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.46', 'destination_ip': '10.0.0.46', 'timestamp': '2023-05-31 20:45:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.47', 'destination_ip': '10.0.0.47', 'timestamp': '2023-05-31 21:30:00', 'event_type': 'malware'},
        {'source_ip': '192.168.0.48', 'destination_ip': '10.0.0.48', 'timestamp': '2023-05-31 22:15:00', 'event_type': 'intrusion'},
        {'source_ip': '192.168.0.49', 'destination_ip': '10.0.0.49', 'timestamp': '2023-05-31 23:00:00', 'event_type': 'login'},
        {'source_ip': '192.168.0.50', 'destination_ip': '10.0.0.50', 'timestamp': '2023-05-31 23:45:00', 'event_type': 'intrusion'}
        # Add more sample data as needed
    ]
    return sample_data

def save_data_to_csv(data, filename):
    # Define the attributes for the CSV file
    fieldnames = ['source_ip', 'destination_ip', 'timestamp', 'event_type']

    # Save the data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    # Generate sample data
    sample_data = generate_sample_data()

    # Save the sample data to a CSV file
    save_data_to_csv(sample_data, 'cybersecurity_logs.csv')

    print("Data collection completed.")

if __name__ == '__main__':
    main()
