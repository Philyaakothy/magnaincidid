   import pandas as pd

   data = {'Name': ['John', 'Alice', 'Bob'],
           'Age': [25, 30, 35],
           'City': ['New York', 'Paris', 'London']}

   df = pd.DataFrame(data)

   df = df.rename(columns={'Name': 'First Name', 'Age': 'Age (years)', 'City': 'Residence'})
   