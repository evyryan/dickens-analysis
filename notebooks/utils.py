import re
import csv

def get_text(filename):
    # Open the file and read the text
    with open(filename, 'r') as file:  # Replace 'filename.txt' with your actual filename
        text = file.read()
    return text

def prepare_text(text):
  # tokenize into paragraphs
  paragraphs = text.split("\n\n")
  # remove newlines within paragraphs
  paragraphs = [re.sub(r'[\n]', ' ', doc) for doc in paragraphs]
  return paragraphs

def save_interactions(interactionsList, filename="interactions.csv"):
    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the header
        writer.writerow(['Item1', 'Item2', 'Time',"Book"])
        # Write the tuples
        for tuple in interactionsList:
            writer.writerow(tuple)