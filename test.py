""" doc """
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score


# Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# x.shape = (150, 4) 4 is the number of columns
# y.shape = (150,)
# X_train.shape = (120, 4)
# y_train.shape = (120,)
# X_test.shape = (30, 4)
# y_test.shape = (30,)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Initialize the SVM classifier
classifier = svm.SVC()

# Train the model using the training data
classifier.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
