#Built with ChatGPT's help
#Change {your_file_name} to your filename.

import csv

# Open the CSV file and read the rows
with open('your_file_name', 'r') as f:
  reader = csv.reader(f)
  
  # Iterate over the rows
  for row in reader:
    # Extract the values from the row and replace special characters with their escaped versions
    title1 = row[0].replace('/', '\\/').replace('?', '\\?')
    title2 = row[1].replace('/', '\\/').replace('?', '\\?')
    description1 = row[2].replace('/', '\\/').replace('?', '\\?')
    description2 = row[3].replace('/', '\\/').replace('?', '\\?')
    
    # Create the Markdown heading using the titles
    heading = f'## {title1} - {title2}'
    
    # Create the bullet point list with the descriptions
    bullet_points = f'- {description1}\n- {description2}'
    
    # Create the Markdown content by combining the heading and bullet points
    markdown = f'{heading}\n{bullet_points}'
    
    # Create the filename by concatenating the titles
    filename = f'{title1}-{title2}.md'
    
    # Write the Markdown to a file
    with open(filename, 'w') as out:
      out.write(markdown)
