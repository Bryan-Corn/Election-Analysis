# Add dependencies
import csv
import os

# Assign a variable to load a file from the path.
file_to_load = os.path.join("Resources", "sample2.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "sample2_analysis.txt")

# Initialize a total vote counter.
total_players = 0

# Create Candidate Options list and Delcare the empty dictionary.
team_options = []
team_players = {}

# Create a county list and county votes dictionary.
position_list = []
position_players = {}

# Winning Candidate, Count, & percentage Tracker
biggest_team = ""
team_player_count = 0
winning_percentage = 0

# Track the largest county turnout and county percentage of voter turnout.
county_turnout_name = ""
county_most_votes = 0
county_percentage = 0

# Read the election results and create dictionaries.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row.
    headers = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_players = total_players + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in team_players:

            # Add the candidate name to the candidate list.
            team_players.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county name does not match any existing county name...
        if county_name not in county_list:

            # Add the county name to the county list.
            county_list.append(county_name)

            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_players:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes:\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    # Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # Retrieve the county vote count.
        votes_county = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        votes_county_percentage = float(votes_county) / float(total_players) * 100
        county_results = (
            f"{county_name}: {votes_county_percentage:.1f}% ({votes_county:,})\n")
        # Print the county results to the terminal.
        print(county_results)

        # Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes_county > county_most_votes) and (votes_county_percentage > county_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            county_most_votes = votes_county
            # Set the winning_percentage equal to the percentage of the winner's votes.
            county_percentage = votes_county_percentage
            # Set the winning_candidate equal to the county's name.
            county_turnout_name = county_name

    # 7: Print the county with the largest turnout to the terminal.
    county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {county_turnout_name}\n"
        f"-------------------------\n"
        f"\n")
    print(county_summary)

    #Save the county with the largest turnout to a text file.
    txt_file.write(county_summary)

    # Determine the percantage of votes for each candidate by looping through the counts
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes.get(candidate_name)
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_players) * 100
        # print out each candidate's name, vote count, and percentage of votes to the text file. (previously to terminal)
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
    #  print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)