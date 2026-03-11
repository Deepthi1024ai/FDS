import pandas as pd

data = {
    'Product ID': [101, 102, 103, 104, 105],
    'Product Name': ['Apple', 'Banana','Orange','Banana','Apple']
}
df = pd.DataFrame(data)

print("Original Dataset")
df['Product Name'] = df['Product Name'].str.lower()
