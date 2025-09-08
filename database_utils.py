import sqlite3
import numpy as np
import pandas as pd

# Generera en databas med heltal.

DB_FILE = "data.db"
conn = sqlite3.connect(DB_FILE)

def make_database():
    """
    Skapar en databas för heltal, om det inte redan finns en.
    """
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS training_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER,
        label INTEGER0
    )
    """)
    conn.commit()

def generate_data(start, n=10):
    """
    Simulerar ny data bestående av heltal.
    Tar emot startvärde (int) och returnerar en panda-dataframe bestående av heltal och märkning om de är udda eller jämnt
    X är heltalet, y är 1 (jämn) eller 0 (udda)
    """
    X = np.arange(start, start+n)
    y = (X % 2 == 0).astype(int) # jämt=True=1, udda=False=0
    return pd.DataFrame({"number": X, "label": y})
    
def insert_data(df):
    """
    Lägger in den nya datan i databasen.
    """
    df.to_sql("training_data", conn, if_exists="append", index=False)
    