#check is there any null value
null_columns=data.columns[data.isnull().any()]
data[null_columns].isnull().sum()
