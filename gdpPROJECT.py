#importing pandas and numpy libraries
import numpy as np
import pandas as pd

#The URL provided is the Wikipedia page containing a table of countries by GDP
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
#pd.read_html reads html table from specified URL
tables = pd.read_html(url)

# Select Table 3 containing the GDP data(table 3 is fourth table)
df = tables[3]


df = df.iloc[1:, [0, 2]]  # Skip the header row and select the first and third columns
df.columns = ['COUNTRY', 'GDP(USD)']  # Rename columns for clarity

# Convert GDP values from strings to numeric
df['GDP(USD)'] = df['GDP(USD)']  
df['GDP(USD)'] = pd.to_numeric(df['GDP(USD)'], errors='coerce')  #errors = 'coerce'parameter ensures that any non-numeric values are converted to NaN (Not a Number)

# Convert GDP from million USD to billion USD
df['GDP(Billion USD)'] = df['GDP(USD)'] / 1000

# Round GDP values to 2 decimal places
df['GDP(Billion USD)'] = np.round(df['GDP(Billion USD)'],2)


# Save the cleaned DataFrame to CSV
df.to_csv('TESTeconomies.csv', index=False)  

print(df)
