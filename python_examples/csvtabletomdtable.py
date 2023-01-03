import csv

# Open the CSV file and read the rows
with open('data.csv', 'r') as f:
  reader = csv.reader(f)
  
  # Extract the field names from the first row
  field_names = next(reader)
  
  # Create the table header
  header = ' | '.join(field_names)
  header = f'| {header} |'
  separator = '---|' * len(field_names)
  
  # Initialize an empty list to store the table rows
  rows = []
  
  # Iterate over the rows
  for row in reader:
    # Convert the row to a string and add it to the list
    rows.append(' | '.join(row))
  
  # Join the rows with newline characters
  rows = '\n'.join(rows)
  
  # Assemble the final table
  table = f'{header}\n{separator}\n{rows}'
  
  # Print the table
  print(table)