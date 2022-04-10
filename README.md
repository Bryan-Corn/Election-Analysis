# Election-Analysis
Bootcamp challenge 3

## Project OVerview
To audit election results provided in a csv file, the Colorado Board of Elections has requested that a script is delivered that will calculate and report:
```
  • The total number of votes cast
  • A complete list of candidates that received votes
  • The total number of votes each candidate received
  • The percentage of votes won by each candidate
  • The winner of the election based on the popular vote
  
The Elections Board had a last-minute request to add a summary of the county vote data to include:
  • A complete list of all counties reporting votes
  • The total number of votes cast in each county
  • Each counties percantage of the toal vote
  • The name of the county with the highest voter turnout

```

  ## Resources
```
  • Data source: election_analysis.csv
  • Software: Python v3.7.6, Visual Studio Code v1.66.1, Git v2.35.1.windows.2
```

## Summary of the Code
This code origioanly reported the following to the terminal and creates a .txt file with the following:
```
  • Total votes
  • A list of each candidate, their % of the total vote, and their total number of votes
  • Election winner
  • Winning vote total 
  • Winning vote percentage
```  
The terminal output from the original code looked like this:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_terminal.png)
  
The .txt file looks like this:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_txt.png)
  
After the request to include county data in the output, the terminal output is the following:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_terminal2.png)

The text file generated by the script includes county reporting after the update:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_txt2.png)

### Election Audit Results

```
As shown in the opdated code output:
  • 369,711 votes were cast in this election in Jefferson, Denver, and Arapahoe counties
  • Jefferson County reported 38,855 votes for 10.5% of the total vote
  • Denver County reported the highest turnout at 306,055 votes for 82.8% of the total vote 
  • Arapahoe County reported 24,801 votes for 6.7% of the total vote
  • Charles Casper Stockham received 23% of the vote with 85,213 total votes
  • Diana DeGette, the winning candidate, received 73.8% of the vote with 272,892 votes
  • Raymon Anthony Doane received 3.1% of the vote with 11,606 votes  
```

## Further Utility of this Code

This code can be used, without modification, to analize vote count data from any election for a single race provided that the csv file is structured in the same column format and has a header row:
```
  • Column 0: Ballot ID
  • Column 1: County Name
  • Column 2: Candidate Name
```
 
The script will work with any number of counties and candidates winning votes for a single race. Replace the election_results.csv in the Resources folder with a new csv file of the same name and restructure the columns if needed.

To test this, I added sample data to the csv file to include additional counties and an additional candidate. Without changing any of the code, the output is the following in the terminal:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_terminal3.png)


The additional, modified data is reported in the text file output as such:

![image](https://github.com/Bryan-Corn/Election-Analysis/blob/main/Resources/election_analysis_output_txt3.png)
