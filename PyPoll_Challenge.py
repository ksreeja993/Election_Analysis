# Open the data.
# Write down the names of all candidates
# Add a vote count for each candidates
# Get the total votes for each cancidate
# Get the total votes cast for the election
import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
county_options =[]
candidate_votes ={}
county_votes ={}



winning_candidate = ""
winning_county = ""

winning_count = 0
county_count = 0
winning_percentage = 0
winning_cpercentage = 0


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------")
    print(election_results, end="")    
    # txt_file.write(election_results)


    # for candidate_name in candidate_votes:
    #     votes = candidate_votes[candidate_name]
    #     vote_percentage = float(votes) / float(total_votes) *100
    #     candidate_results = (f"\n{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
    #     print(candidate_results)
    #     txt_file.write(candidate_results)

    #     if (votes > winning_count) and (vote_percentage > winning_percentage):
    #         winning_count = votes
    #         winning_candidate = candidate_name
    #         winning_percentage = vote_percentage
    #     # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    #     winning_candidate_summary = (
    #         f"----------------------------\n"
    #         f"Winner:{winning_candidate}\n"
    #         f"Winning Vote Count: {winning_count:,}\n"
    #         f"Winning Percentage: {winning_percentage:.1f}%\n"
    #         f"------------------------\n"
    #     )
    # print(winning_candidate_summary)
    
    
    # txt_file.write(winning_candidate_summary)

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        

        county_name = row[1]

        if county_name not in county_options:

            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

with open(file_to_save,"w") as txt_file:
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        candidate_results = (f"\n{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner:{winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n"
        )
    print(winning_candidate_summary)
    
    
    txt_file.write(winning_candidate_summary)
    county_results = (f"\nCounty Votes\n")
  
    print(county_results, end ="")
    # txt_file.write(election_results)
    txt_file.write(county_results)

    for county_name in county_options:
        cvotes = county_votes[county_name]
        cvotes_percentage = float(cvotes) / float(total_votes) *100
        county_results = (f"{county_name}:{cvotes_percentage:.1f}% ({cvotes:,})\n")
        
        print(county_results)
        txt_file.write(county_results)
        
        
        # txt_file.write(county_results)
        if (cvotes > county_count) and (cvotes_percentage > winning_cpercentage):
            county_count = cvotes
            winning_county = county_name
            winning_cpercentage = cvotes_percentage
         # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        winning_county_summary = (f"\n--------------------\n"
            f"Largest County Turnout:{winning_county}\n"
            f"--------------------\n")
        
    print(winning_county_summary) 
    
    

    txt_file.write(winning_county_summary)
    
    # txt_file.write(winning_candidate_summary)


        








