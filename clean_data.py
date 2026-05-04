import pandas as pd

df = pd.read_csv('incd.csv', skiprows=8)

print(df.columns.tolist())
print(df.head())

# Remove the Iowa and US summary rows, keep only counties
df = df[~df['County'].str.contains('Iowa|US')]

# Clean county names - remove the (7) at the end
df['County'] = df['County'].str.replace(r'\(.*\)', '', regex=True).str.strip()

# Drop rows where FIPS is NaN first, then filter to Iowa counties
df = df.dropna(subset=['FIPS'])
df = df[df['FIPS'].between(19001, 19199)]

print(f"Total counties: {len(df)}")
print(df.tail(5))

# Rename columns to something clean and usable
df = df.rename(columns={
    'Age-Adjusted Incidence Rate([rate note]) - cases per 100,000': 'incidence_rate',
    '2023 Rural-Urban Continuum Codes([rural urban note])': 'rural_urban',
    'Average Annual Count': 'avg_annual_count',
    'Recent Trend': 'trend',
    'FIPS': 'fips'
})

# Keep only the columns we actually need
df = df[['County', 'fips', 'rural_urban', 'incidence_rate', 'avg_annual_count', 'trend']]

print(df.head())
print(df.dtypes)

# Convert fips to integer so it looks like 19029 not 19029.0
df['fips'] = df['fips'].astype(int)

# Also clean the incidence_rate column - strip any spaces
df['incidence_rate'] = df['incidence_rate'].astype(str).str.strip().astype(float)

print(df.head())
print(df.dtypes)