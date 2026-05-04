import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='halloween',
    database='iowa_cancer'
)

print("Connected to MySQL successfully")

cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS county_incidence (
        id INT AUTO_INCREMENT PRIMARY KEY,
        county VARCHAR(100),
        fips INT,
        rural_urban VARCHAR(20),
        incidence_rate FLOAT,
        avg_annual_count FLOAT,
        trend VARCHAR(20)
    )
""")

# Load and clean the data
df = pd.read_csv('incd.csv', skiprows=8)
df = df[~df['County'].str.contains('Iowa|US')]
df['County'] = df['County'].str.replace(r'\(.*\)', '', regex=True).str.strip()
df = df.dropna(subset=['FIPS'])
df = df[df['FIPS'].between(19001, 19199)]
df = df.rename(columns={
    'Age-Adjusted Incidence Rate([rate note]) - cases per 100,000': 'incidence_rate',
    '2023 Rural-Urban Continuum Codes([rural urban note])': 'rural_urban',
    'Average Annual Count': 'avg_annual_count',
    'Recent Trend': 'trend',
    'FIPS': 'fips'
})
df = df[['County', 'fips', 'rural_urban', 'incidence_rate', 'avg_annual_count', 'trend']]
df['fips'] = df['fips'].astype(int)

# Insert each row into MySQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO county_incidence (county, fips, rural_urban, incidence_rate, avg_annual_count, trend)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['County'], row['fips'], row['rural_urban'], row['incidence_rate'], row['avg_annual_count'], row['trend']))

conn.commit()
print(f"Loaded {len(df)} counties into MySQL")
conn.close()