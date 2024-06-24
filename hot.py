import pandas as pd

# Исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание двух столбцов для one hot encoding
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

# Удаляем исходный столбец 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()


data.to_csv('one_hot_encoded_data.csv', index=False)