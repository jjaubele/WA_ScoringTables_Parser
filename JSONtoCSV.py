import pandas as pd
import json

with open('tablas_extraidas/mens_scoring_tables.json', 'r') as f:
    mens_scoring_tables = json.load(f)
with open('tablas_extraidas/womens_scoring_tables.json', 'r') as f:
    womens_scoring_tables = json.load(f)

points = [i for i in reversed(range(1, 1401))]
mens_scoring_tables_df  = pd.DataFrame(mens_scoring_tables, index=points)
womens_scoring_tables_df = pd.DataFrame(womens_scoring_tables, index=points)

mens_scoring_tables_df.to_csv('tablas_extraidas/mens_scoring_tables.csv', index_label='Points')
womens_scoring_tables_df.to_csv('tablas_extraidas/womens_scoring_tables.csv', index_label='Points')