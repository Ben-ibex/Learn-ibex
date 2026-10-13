import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent.parent / 'Datasource' / 'stud.csv'
sd = pd.read_csv(csv_path)
print(sd)
