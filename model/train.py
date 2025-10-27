import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras. layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load models

df = pd.red_csv("bank_churn_data.csv")
x=df.drop(['customerId','surname','Exited'],axis=1)
y=df['Exited']


X['Geography'] = LabelEncoder(). fit_transform(X|' Geography' I)
X['Gender'] = LabelEncoder(). fit_transform(X|'Gender'])
X_train, X_test, y_train, _test = train_test_split(X, y, test_size=8.2, random_state=42)
19) #tranform of the data #transform of the data
scaler = StandardScaler()
X_train = scaler. fit_transform(X_train)