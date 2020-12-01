# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:04:05 2020

@author: HP
"""

import pandas as pd
import matplotlib as mt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

train= pd.read_csv('titanic/train.csv')
test= pd.read_csv('titanic/test.csv')

train.columns

#knowing how many survived and how many died
train['Survived'].value_counts()

train.select_dtypes('object').columns

train.columns


#exploring sex column

train['Sex'].value_counts()#577m,314f

g=sns.FacetGrid(train,col='Sex')
g.map(plt.hist,'Survived')
#more male died than female

train.select_dtypes('object').columns

#exploring ticket

train['Ticket'].describe()
#consist 891 tickets but many duplicated #681
#will drop ticket
train=train.drop('Ticket',axis=1)
test=test.drop('Ticket',axis=1)

train.select_dtypes('object').columns
#explorung cabin
train['Cabin'].describe()#total 204 #unique 147
train['Cabin'].value_counts()

#muliple people sharing one cabing, so it should now play much role

train=train.drop('Cabin',axis=1)
test=test.drop('Cabin',axis=1)

train.select_dtypes('object')

#exploring Embarked

train['Embarked'].describe()#categorical val..hmmm

g=sns.FacetGrid(train,col='Embarked')
g.map(plt.hist,'Survived')
#people embarked from S has a great chances of surviving


g=sns.FacetGrid(train,col='Survived')
g.map(plt.hist,'Age',bins=15)

g=sns.FacetGrid(train,col='Embarked',row='Survived',hue='Sex')
g.map(plt.hist,'Pclass')
g.add_legend()



#knowing relationship thru tables

train[['Embarked','Survived']].groupby('Embarked',as_index=False).mean()

train[['Pclass','Survived']].groupby('Pclass',as_index=False).mean()

train[['Sex','Survived']].groupby('Sex',as_index=False)['Survived'].mean()


train[['Embarked','Pclass','Survived']].groupby('Embarked',as_index=False)['Survived'].mean()


#filling missing values

g=sns.FacetGrid(train,col='Pclass',row='Survived')
g.map(sns.distplot,'Age',hist=False,rug=True)

def cal_med_mean(s,g):
    median=train.groupby('Pclass').get_group(g).query(f'Survived =={s}')['Age'].median()
    mean=  train.groupby('Pclass').get_group(g).query(f'Survived =={s}')['Age'].mean()
    return print("median: {} mean:{}".format(median,mean))

cal_med_mean(1,3)
import math

for i in range(0,len(train)):
    if (train['Survived'].iloc[i]==0) & (train['Pclass'].iloc[i]==1):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 45.25
        continue
            
    if (train['Survived'].iloc[i]==0) & (train['Pclass'].iloc[i]==2):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 30.5
        continue

    if (train['Survived'].iloc[i]==0) & (train['Pclass'].iloc[i]==3):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 25.0
        continue
            
    if (train['Survived'].iloc[i]==1) & (train['Pclass'].iloc[i]==1):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 35.0
        continue
    
    if (train['Survived'].iloc[i]==1) & (train['Pclass'].iloc[i]==2):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 27.0
        continue
    
    if (train['Survived'].iloc[i]==1) & (train['Pclass'].iloc[i]==3):
        if math.isnan(train['Age'].iloc[i]):
            train['Age'].iloc[i]= 22.0
        continue
test['Age']=test['Age'].fillna(train['Age'].mean())


#optimizing ages by checking which group survived most

train['ageband']=pd.cut(train['Age'],5)
train[['ageband','Survived']].groupby('ageband',as_index=False).mean()

for i in range(len(train)):
    if train['Age'][i]<=16.336:
        train['Age'][i]=0
    if (train['Age'][i]>16.336) & (train['Age'][i]<=32.252):
        train['Age'][i]=1
    if (train['Age'][i]>32.252) & (train['Age'][i]<=48.168):
        train['Age'][i]=2
    if (train['Age'][i]>48.168) & (train['Age'][i]<=64.084):
        train['Age'][i]=3
    if (train['Age'][i]>64.084) & (train['Age'][i]<=80.0):
        train['Age'][i]=4
    

test['Ageband']= pd.cut(test['Age'],5)
for i in range(len(test)):
    if test['Age'][i]<=15.336:
        test['Age'][i]=0
    if (test['Age'][i]>15.336) & (test['Age'][i]<=30.502):
        test['Age'][i]=1
    if (test['Age'][i]>30.502) & (test['Age'][i]<=45.668):
        test['Age'][i]=2
    if (test['Age'][i]>45.668) & (test['Age'][i]<=60.834):
        test['Age'][i]=3
    if (test['Age'][i]>60.834) & (test['Age'][i]<=76.0):
        test['Age'][i]=4

train=train.drop('ageband',axis=1)
test= test.drop('Ageband',axis=1) 

train['FamileSize']=train['SibSp']+train['Parch']+1
train[['FamileSize','Survived']].groupby('FamileSize').mean()
train['Alone']=train['FamileSize']<2

train=train.drop(['FamileSize','SibSp','Parch'],axis=1)

test['FamileSize']=test['SibSp']+test['Parch']+1
test['Alone']= test['FamileSize']<2
test=test.drop(['FamileSize','SibSp','Parch'],axis=1)

train['Alone']= train['Alone'].map({True:1,False:0})

train=train.dropna()
train.isna().sum()

train=train.drop(['PassengerId','Name'],axis=1)
pid=test['PassengerId']


test= test.drop(['PassengerId','Name'],axis=1)
test['Fare']=test['Fare'].fillna(train['Fare'].mean())
test.isna().sum()


train['Sex']=train['Sex'].map({'male':1,'female':0})
test['Sex']=test['Sex'].map({'male':1,'female':0})

train['Embarked']= train['Embarked'].map({'S':1,'C':2,'Q':3})
test['Embarked']= test['Embarked'].map({'S':1,'C':2,'Q':3})

train.info()

from sklearn.model_selection import train_test_split

X=train.drop('Survived',axis=1)
y=train['Survived']

train_x,val_x,test_y,val_y=train_test_split(X,y)

from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(train_x, test_y)
Y_pred = random_forest.predict(val_x)
random_forest.score(train_x, test_y)
acc_random_forest = round(random_forest.score(train_x,test_y) * 100, 2)

acc_random_forest

y_pred=random_forest.predict(test)

submission=pd.DataFrame({'PassengerId':pid,'Survived':y_pred})
submission.to_csv('Submission.csv',index=False)