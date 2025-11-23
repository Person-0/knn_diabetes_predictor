import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

sep_line = "="*35
print("\n" + sep_line)
print("KNN-based Diabetes Predictor")
print(sep_line)

print("reading data from csv file")
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = pd.read_csv("diabetes.csv", names=column_names)

Data_Required = column_names[:-1]
X=data[Data_Required]
Y=data['Outcome']

test_size = 0.3
print(f"splitting testing and training data in a {test_size * 10}:{(1-test_size)*10} ratio")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = test_size, random_state=42)

print("scaling data")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("fitting data to the KNN classifier")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, Y_train)
print("done!\n")

print("predicting testing data")
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(Y_test, y_pred)
print("Model Accuracy: ", round(accuracy * 100, 4), "%")
print(sep_line, "\n")

while True:
    should_input = input("Would you like to enter your information to predict diabetes or not? (y/n): ").strip().lower() == "y"
    if not should_input:
        break

    input_data = []
    for key in Data_Required:
        d = input("Enter " + key + ": ")
        input_data.append(d)

    df = pd.DataFrame([input_data], columns=Data_Required)
    scaled = scaler.transform(df)

    result = bool(knn.predict(scaled)[0])
    if result:
        result = "Yes"
    else:
        result = "No"

    print("Prediction: ", result, "\n")