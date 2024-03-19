import pyspark
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('customers-100.csv')
print(dataset.to_string())