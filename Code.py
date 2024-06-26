import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction .text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df=pd.read_csv("mail_data.csv")
print(df)
data=df.where((pd.notnull(df)),'')
data.head()
data.info()
data.shape
(5572, 2)
data.loc[data['Category']=='spam', 'Category',]=0
data.loc[data['Category']=='ham', 'Category',]=1
x=data['Message']
y=data['Category']
print(x)
print(y)
x_train, x_test, y_train, y_test
train_test_split(x,y,test_size=0.2,random_state=3)
print(x.shape)
print(x_train.shape)
print(x_test.shape)
print(y.shape)
print(y_train.shape)
print(y_test.shape)
feature_extraction = TfidfVectorizer(min_df =1, stop_words =
'english',lowercase=True)
x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)
y_train = y_train.astype('int')
y_test = y_test.astype('int')
print(x_train)
print(x_train_features)
model = LogisticRegression()
model.fit(x_train_features,y_train)
prediction_on_training_data = model.predict(x_train_features)
accuracy_on_training_data = accuracy_score(y_train,
prediction_on_training_data)
print('ACC_on_training_data:', accuracy_on_training_data)
prediction_on_test_data = model.predict(x_test_features)
accuracy_on_test_data = accuracy_score(y_test,
prediction_on_test_data)
print('acc on test data:', accuracy_on_test_data)

// Lets take the test cases to check whether the mail is spam
or not
// Firstly taking the “Spam Mail” as input
input_your_mail=["SIX chances to win CASH! From 100 to 20,000
pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+
TsandCs apply Reply HL 4"]
input_data_features =
feature_extraction.transform(input_your_mail)
prediction = model.predict(input_data_features)
print(prediction)
if(prediction[0]==1):
print('Ham Mail')
else:
print('Spam Mail')
OUTPUT: 0 (Spam Mail)
// Secondly taking thE “Ham Mail or Not Spam Mail” as input
input_your_mail=["I'm gonna be home soon and i don't want to
talk about this stuff anymore tonight, k? I've cried enough
today"]
input_data_features =
feature_extraction.transform(input_your_mail)
prediction = model.predict(input_data_features)
print(prediction)
if(prediction[0]==1):
print('Ham Mail')
else:
print('Spam Mail')
OUTPUT: 1(Ham Mail)
