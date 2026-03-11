import pandas as pd
from dateutil.parser import parse

def parse_date(date_str):
    try:
        return parse(date_str, dayfirst=False)
    except ValueError:
        return pd.NaT

# Apply date parsing
df['Event Date'] = df['Event Date'].apply(parse_date)

# Format date as YYYY-MM-DD
df['Event Date'] = df['Event Date'].dt.strftime("%Y-%m-%d")

print("Dataset after parsing and formatting")
print(df)
