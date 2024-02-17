import tensorflow as tf
import pandas as pd

from sklearn.preprocessing import LabelEncoder

file = pd.read_csv("student-por.csv")
label_encoder = LabelEncoder()
columns = file.columns
for i in columns:
    file[i] = label_encoder.fit_transform(file[i])
x = file.drop(columns=["G1", "G2", "G3"])
y = file[["G1", "G2", "G3"]]
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
