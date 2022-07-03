# Open the data.
# Write down the names of all candidates
# Add a vote count for each candidates
# Get the total votes for each cancidate
# Get the total votes cast for the election
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    


