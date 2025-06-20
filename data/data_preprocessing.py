import pandas as pd

# Load the data 3 csv files
data_1 = pd.read_csv('data/daily_sales_data_0.csv')
data_2 = pd.read_csv('data/daily_sales_data_1.csv')
data_3 = pd.read_csv('data/daily_sales_data_2.csv')

# Concatenate the data
data = pd.concat([data_1, data_2, data_3])

# Drop the rows where product is not 'pink morsel'
data = data[data['product'] == 'pink morsel']

# Drop the product column
data = data.drop(columns=['product'])

# add column name 'sales' and remove the dollar sign and convert to float and drop the quantity & price column
data['price'] = data['price'].str.replace('$', '').astype(float)

data['sales'] = data['price'] * data['quantity']
data = data.drop(columns=['quantity', 'price'])

# save the data to a csv file
data.to_csv('data/daily_sales_data.csv', index=False)






