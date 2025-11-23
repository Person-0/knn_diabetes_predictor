# KNN Diabetes Predictor

# What is Diabetes?

> Source: [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/diabetes)

Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood glucose. Hyperglycaemia, also called raised blood glucose or raised blood sugar, is a common effect of uncontrolled diabetes and over time leads to serious damage to many of the body's systems, especially the nerves and blood vessels.
In 2022, 14% of adults aged 18 years and older were living with diabetes, an increase from 7% in 1990. More than half (59%) of adults aged 30 years and over living with diabetes were not taking medication for their diabetes in 2022. Diabetes treatment coverage was lowest in low- and middle-income countries.

In 2021, diabetes was the direct cause of 1.6 million deaths and 47% of all deaths due to diabetes occurred before the age of 70 years. Another 530 000 kidney disease deaths were caused by diabetes, and high blood glucose causes around 11% of cardiovascular deaths (1).

Since 2000, mortality rates from diabetes have been increasing. By contrast, the probability of dying from any one of the four main noncommunicable diseases (cardiovascular diseases, cancer, chronic respiratory diseases or diabetes) between the ages of 30 and 70 decreased by 20% globally between 2000 and 2019. 

# Predicting Diabetes

This program uses K-Nearest-neighbour algorithm to predict diabetes using input data with an accuracy of ~70%.<br>

The programming language used is Python v3.13.5 with libraries [pandas](https://pypi.org/project/pandas/) and [scikit-learn](https://pypi.org/project/scikit-learn/).<br>

The model is trained from [Pima Indians Diabetes Database available on kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).<br>

Predictions are made based on `Number of Pregnancies`, `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction` and `Age`.
