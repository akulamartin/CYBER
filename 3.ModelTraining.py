import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
from sklearn import svm
def train_model(csv_file):
    # Load the preprocessed CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Split the data into features (X) and target labels (y)
    X = df.drop(columns=['event_type'])  # Features: all columns except 'event_type'
    y = df['event_type']  # Target labels: 'event_type' column

    # Encode categorical variables using one-hot encoding
    categorical_features = ['source_ip', 'destination_ip']
    categorical_indices = [X.columns.get_loc(feature) for feature in categorical_features]
    transformer = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), categorical_indices)], remainder='passthrough')
    X_encoded = transformer.fit_transform(X)

    # Split the data into training and testing sets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest classifier
    classifier = RandomForestClassifier(random_state=42)
    #classifier = svm.SVC()
    # Train the model using the training data
    classifier.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = classifier.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

def main():
    # Specify the path to the preprocessed CSV file
    preprocessed_file = 'preprocessed_data.csv'

    # Train the model using the preprocessed data
    train_model(preprocessed_file)

if __name__ == '__main__':
    main()
