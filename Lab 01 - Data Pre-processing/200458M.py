# Data Pre-processing Lab Assignment

# **----- Import all libraries here -----**

import pandas as pd
import numpy as np

# Import the dataset into a data frame -----------------------------------
dataset = pd.read_csv('diabetes.csv')

# Code to pre-process the dataset goes here --------------------------------

# Remove duplicates if any
columns = dataset.columns.to_list()
columns.pop(0)
# Keeps the first occurrence of each set of duplicates and removes any subsequent occurrences
# Based on all columns except 'Patient_ID' column
dataset = dataset.drop_duplicates(subset=columns)

# Fill missing values (if any) without deleting any record
# Fill missing values with the median value of each column
dataset = dataset.fillna(dataset.median())

# Resolve out-of-range values if any
# Get median of each column
median = dataset[columns].median()

preg_median = median[0]
dataset.loc[dataset['Pregncies'] < 0, 'Pregncies'] = preg_median
dataset.loc[dataset['Pregncies'] > 15, 'Pregncies'] = preg_median

glucose_median = median[1]
dataset.loc[dataset['Glucose'] <= 0, 'Glucose'] = glucose_median

blood_pres_median = median[2]
dataset.loc[dataset['BloodPressure'] <= 0, 'BloodPressure'] = blood_pres_median
dataset.loc[dataset['BloodPressure'] >= 120, 'BloodPressure'] = blood_pres_median

skin_thick_median = median[3]
dataset.loc[dataset['SkinThickness'] <= 0, 'SkinThickness'] = skin_thick_median
dataset.loc[dataset['SkinThickness'] >= 40, 'SkinThickness'] = skin_thick_median

insulin_median = median[4]
dataset.loc[dataset['Insulin'] <= 30, 'Insulin'] = insulin_median
dataset.loc[dataset['Insulin'] >= 400, 'Insulin'] = insulin_median

BMI_median = median[5]
dataset.loc[dataset['BMI'] <= 18, 'BMI'] = BMI_median
dataset.loc[dataset['BMI'] >= 40, 'BMI'] = BMI_median

ped_fun_median = median[6]
dataset.loc[dataset['DiabetesPedigreeFunction'] <= 0, 'DiabetesPedigreeFunction'] = ped_fun_median
dataset.loc[dataset['DiabetesPedigreeFunction'] >= 2.99, 'DiabetesPedigreeFunction'] = ped_fun_median

# round off the values
dataset['DiabetesPedigreeFunction'] = dataset['DiabetesPedigreeFunction'].round(3)

cols_to_round = [col for col in columns if col not in ['DiabetesPedigreeFunction', 'Outcome']]
dataset[cols_to_round] = dataset[cols_to_round].apply(lambda x: round(x, 2))

# Write the pre-processed dataset into a csv file --------------------------------
pre_processed_dataset = dataset

student_id = "200458M.csv"

pre_processed_dataset.to_csv(student_id, index=False)

