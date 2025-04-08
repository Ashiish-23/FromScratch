import pandas as pd
import sqlite3

def extract():
    csv_data = pd.read_csv('Prog01/data.csv')
    json_data = pd.read_json('Prog01/data.json')
    db_conn = sqlite3.connect('Prog01/data.db')
    db_data = pd.read_sql("SELECT * FROM users", db_conn)
    db_conn.close()
    return csv_data, json_data, db_data

def clean(df):
    df = df.dropna()
    df = df.apply(lambda x: x.str.strip().str.lower() if x.dtype == "object" else x)
    return df.reset_index(drop=True)

def transform(csv, json, db):
    return clean(csv), clean(json), clean(db)

def load(*dfs, output_path='Prog01/data_warehouse.csv'):
    combined = pd.concat(dfs, ignore_index=True)
    combined.to_csv(output_path, index=False)
    print(f"ETL done. Data saved to {output_path}")

if __name__ == "__main__":
    csv_data, json_data, db_data = extract()
    csv_clean, json_clean, db_clean = transform(csv_data, json_data, db_data)
    load(csv_clean, json_clean, db_clean)
