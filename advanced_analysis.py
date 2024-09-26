import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Используем встроенный набор данных Seaborn
df = sns.load_dataset('tips')

# Печать первых 5 строк данных
print(df.head())

# Построение графиков
sns.barplot(x='day', y='total_bill', data=df)
plt.title('Total Bill by Day')
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Total Bill Distribution by Day')
plt.show()
