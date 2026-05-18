import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, recall_score
from sklearn.model_selection import train_test_split
import joblib


def train_model():
    #step 1: get the data
    df = pd.read_csv('data/earthquake_tsunami_cleaned.csv')

    print(df["tsunami_boolean"].value_counts())

    #step 2: select features and target variable
    features = ['magnitude', 'depth', 'cdi', 'sig', 'mmi', 'gap', 'nst', 'dmin'] # Added more features to improve model performance
    X = df[features]
    target = ['tsunami_boolean']
    Y = df[target]  

    #step 3: split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    #step 4: train the model using logistic regression
    model = LogisticRegression(max_iter=1000, class_weight='balanced') # Increased max_iter to ensure convergence amd added class_weight to handle class imbalance
    model.fit(X_train, Y_train.values.ravel())  # Used .values.ravel() to convert Y_train to a 1D array

    print("Model trained successfully")

    #step 5: evaluate the model
    Y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Model accuracy: {accuracy:.2%}")

    recall = recall_score(Y_test, Y_pred)
    print(f"Model recall: {recall:.2%}")
    classification = classification_report(Y_test, Y_pred)
    print("\nFull Report:")
    print(classification)

    #step 6: save the model for future use
    joblib.dump(model, 'server/ml/tsunami_prediction_model.pkl')
    print("Model saved successfully")

if __name__ == "__main__":
    train_model()