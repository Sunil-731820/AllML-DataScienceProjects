import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report,accuracy_score,confusion_matrix
import seaborn as sns

# First Laod the using the CSv files

url = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv")
colummns = ['Pregnancies','Glucose','BloodPressure','']