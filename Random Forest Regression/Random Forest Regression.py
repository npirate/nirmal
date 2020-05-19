########################### Data Preprocessing ############################

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the data set
dataset = pd.read_csv('beer_data.csv')


# Printing first 10 rows of the dataset
print("\n----------------------------\n",dataset.head(10))


# Dealing with the categorical data

# Spliting Cellar Temperature into Maximum and Minimum based on the given data and converting the type from str to int

dataset['Minimum_Cellar_Temp'] = dataset['Cellar Temperature'].apply(lambda x : int(x.split('-')[0].strip()))
dataset['Maximum_Cellar_Temp'] = dataset['Cellar Temperature'].apply(lambda x : int(x.split('-')[1].strip()))

# New dataset with selected features
dataset = dataset[['ABV', 'Ratings','Minimum_Cellar_Temp','Maximum_Cellar_Temp', 'Score']]

# Printing first 10 rows of the dataset
print("\n----------------------------\n",dataset.head(10))

# Printing the summary of the dataset
print("\n----------------------------\n")
print(dataset.info())


# Classifying dependent and independent variables

# All columns except the last column are independent features - (Selecting every column except Score)
X = dataset.iloc[:,:-1].values

# Only the last column is the dependent feature or the target variable(Score)
y = dataset.iloc[:,-1].values

# Creating training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


# Step 2

########################### Random Forest Regression ###########################

# Create a Random Forest Regressor and provide the dataset
from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(n_estimators=100, criterion='mse', n_jobs= -1, random_state=2)
# Training the regressor with training data
rfr.fit(X_train, y_train)

# Predicting the salary for a test set
y_pred = rfr.predict(X_test)

# Priniting the predicted values
print("\n----------------------------\nPredictions = \n",y_pred)

# Calculating score from Root Mean Log Squared Error
def rmlse(y_test, y_pred):
    error = np.square(np.log10(y_pred +1) - np.log10(y_test +1)).mean() ** 0.5
    score = 1 - error
    return score

# Printing the score
print("\n----------------------------\nRMLSE Score = ", rmlse(y_test, y_pred))