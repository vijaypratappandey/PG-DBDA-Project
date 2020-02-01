# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:45:55 2020

@author: dbda
"""

import pandas as pd

acd = pd.read_csv(r'F:\sai\final_zero_nulls.csv',engine='python')

acd = acd.replace({'Accident_Severity': {'Slight':0, 'Serious':1,'Fatal':1}})

acd.info

X = acd.drop(['Accident_Severity','make','Date','Local_Authority_(District)','Police_Force'],axis=1)
X = pd.get_dummies(X)
y = acd['Accident_Severity']

#Slight     1505502
#Serious     232666
#Fatal        25029


y.value_counts()
X.info
X.dtypes
l =X.columns
for i in l:
    print(i,' ',type(i))
#pd.value_counts(y)
#A fatal injury is one resulting in death while a serious injury incident is one that results in life threatening injuries, or an incident involving multiple casualties with major injuries.

#Slight     1505502
#Serious     232666
#Fatal        25029


from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=2020)
X_resampled, y_resampled = ros.fit_resample(X, y)

#pd.value_counts(y_resampled)
#Serious    1505502
#Fatal      1505502
#Slight     1505502



from sklearn import metrics 
from collections import Counter

from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler, NearMiss, TomekLinks, EditedNearestNeighbours

predictions = None
results = {'ordinary': {},
               'class_weight': {},
               'oversample': {},
               'undersample': {}}

def model_resampling_pipeline(X_train, X_test, y_train, y_test, model):
    
    
    # ------ No balancing ------
    model.fit(X_train, y_train)
    predictions = model.predict_proba(X_test)[:,1]
    print(predictions)
    
    print(predictions.dtype)
    
    accuracy = metrics.accuracy_score(y_test, predictions)
    precision, recall, fscore, support = metrics.precision_recall_fscore_support(y_test, predictions)
    print(metrics.confusion_matrix(y_test, predictions).ravel())
    xxx =  metrics.confusion_matrix(y_test, predictions).ravel()
    tn = xxx[0]
    fp = xxx[1] 
    fn = xxx[2]
    tp = xxx[3]
    print(predictions)
    fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
    auc = metrics.auc(fpr, tpr)
    
    results['ordinary'] = {'accuracy': accuracy, 'precision': precision, 'recall': recall, 
                          'fscore': fscore, 'n_occurences': support,
                          'predictions_count': Counter(predictions),
                          'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn,
                          'auc': auc}
    
    print(results)
    
    
    # ------ Class weight ------
    if 'class_weight' in model.get_params().keys():
        model.set_params(class_weight='balanced')
        model.fit(X_train, y_train)
        predictions = model.predict_proba(X_test)[:,1]
        accuracy = metrics.accuracy_score(y_test, predictions)
        precision, recall, fscore, support = metrics.precision_recall_fscore_support(y_test, predictions)
        xxx =  metrics.confusion_matrix(y_test, predictions).ravel()
        tn = xxx[0]
        fp = xxx[1] 
        fn = xxx[2]
        tp = xxx[3]
        fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
        auc = metrics.auc(fpr, tpr)

        results['class_weight'] = {'accuracy': accuracy, 'precision': precision, 'recall': recall, 
                                  'fscore': fscore, 'n_occurences': support,
                                  'predictions_count': Counter(predictions),
                                  'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn,
                                  'auc': auc}

    
    # ------------ OVERSAMPLING TECHNIQUES ------------
    print('------ Oversampling methods ------')
    techniques = [RandomOverSampler(),
                  SMOTE(),
                  ADASYN()]
    
    for sampler in techniques:
        technique = sampler.__class__.__name__
        print(f'Technique: {technique}')
        print(f'Before resampling: {sorted(Counter(y_train).items())}')
        X_resampled, y_resampled = sampler.fit_sample(X_train, y_train)
        print(f'After resampling: {sorted(Counter(y_resampled).items())}')

        model.fit(X_resampled, y_resampled)
        predictions = model.predict_proba(X_test)[:,1]
        accuracy = metrics.accuracy_score(y_test, predictions)
        precision, recall, fscore, support = metrics.precision_recall_fscore_support(y_test, predictions)
        xxx =  metrics.confusion_matrix(y_test, predictions).ravel()
        tn = xxx[0]
        fp = xxx[1] 
        fn = xxx[2]
        tp = xxx[3]
        fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
        auc = metrics.auc(fpr, tpr)

        results['oversample'][technique] = {'accuracy': accuracy, 
                                            'precision': precision, 
                                            'recall': recall,
                                            'fscore': fscore, 
                                            'n_occurences': support,
                                            'predictions_count': Counter(predictions),
                                            'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn,
                                            'auc': auc}

    
    # ------------ UNDERSAMPLING TECHNIQUES ------------
    print('------ Undersampling methods ------')
    techniques = [RandomUnderSampler(),
                  NearMiss(version=1),
                  TomekLinks(),
                  EditedNearestNeighbours()]
    
    for sampler in techniques:
        technique = sampler.__class__.__name__
        if technique == 'NearMiss': technique+=str(sampler.version)
        print(f'Technique: {technique}')
        print(f'Before resampling: {sorted(Counter(y_train).items())}')
        X_resampled, y_resampled = sampler.fit_sample(X_train, y_train)
        print(f'After resampling: {sorted(Counter(y_resampled).items())}')

        model.fit(X_resampled, y_resampled)
        predictions = model.predict_proba(X_test)[:,1]
        accuracy = metrics.accuracy_score(y_test, predictions)
        precision, recall, fscore, support = metrics.precision_recall_fscore_support(y_test, predictions)
        xxx =  metrics.confusion_matrix(y_test, predictions).ravel()
        tn = xxx[0]
        fp = xxx[1] 
        fn = xxx[2]
        tp = xxx[3]
        fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
        auc = metrics.auc(fpr, tpr)

        results['undersample'][technique] = {'accuracy': accuracy, 
                                            'precision': precision, 
                                            'recall': recall,
                                            'fscore': fscore, 
                                            'n_occurences': support,
                                            'predictions_count': Counter(predictions),
                                            'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn,
                                            'auc': auc}
        

    return results


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
results = model_resampling_pipeline(X_train, X_test, y_train, y_test, model)

df = pd.DataFrame.from_dict([results])
df.to_csv(r'F:\sai\results_reshampling.csv',index =False)


