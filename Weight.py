import pandas as pd
import re

data = {
    'Sample ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'Weight': ['70kg', '154 lbs', '68 kg', '100 pounds', '72 kilogram']
}

df = pd.DataFrame(data)

def extract_weight(weight_str):
    # Extract numeric part
    value = float(re.findall(r'\d+\.?\d*', weight_str)[0])

    # Convert to kg if needed
    if 'lb' in weight_str.lower() or 'pound' in weight_str.lower():
        return value * 0.453592  # pounds → kg
    else:
        return value  # already in kg

# Apply function
df['Weight_kg'] = df['Weight'].apply(extract_weight)

print("Final Dataset")
print(df)
