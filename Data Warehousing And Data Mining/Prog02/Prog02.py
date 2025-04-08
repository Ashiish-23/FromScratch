import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold

df1 = pd.read_csv('Prog02/dataset1.csv').dropna()
df2 = pd.read_csv('Prog02/dataset2.csv').ffill()
df = pd.merge(df1, df2, on='ID')

cols = ['value1', 'value2']
df[cols] = MinMaxScaler().fit_transform(df[cols])

features = df.select_dtypes(include=['float64', 'int64']).drop(columns=['ID'], errors='ignore')
selector = VarianceThreshold(threshold=0.04)
reduced = selector.fit_transform(features)

selected_cols = features.columns[selector.get_support()]
reduced_df = pd.DataFrame(reduced, columns=selected_cols)

if 'ID' in df.columns:
    reduced_df.insert(0, 'ID', df['ID'])

print("✅ Reduced DataFrame:")
print(reduced_df)
