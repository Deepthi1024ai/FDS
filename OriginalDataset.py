import pandas as pd
from dateutil.parser import parse

data = {
    'Event ID': [1, 2, 3, 4, 5],
    'Event Date': ['01/12/2023', 'December 2,2023', '2023-12-03', '12.04.2023', '5th Dec 2023']
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df, '\n')
