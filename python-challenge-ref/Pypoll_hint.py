import os
import csv

#choose 1 or 2
file_num = 1

# Identifies file with poll data
file = os.path.join("/Users/miiinaa223/Desktop/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

#gets data file
with open(file, newline="") as csvfile:
    csvread = csv.reader(csvfile,delimiter=",")
    

    #skips header line
    next(csvread, None)

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvread: # can pull the data in csv by row
        total_votes += 1
        if row[2] in poll.keys(): # .keys() is the method to pull keys from the dictionary. e.g If we already counted Khan in the dictionary ..
            poll[row[2]] = poll[row[2]] + 1 # count votes
        else:
            poll[row[2]] = 1 # e.g If Khan does not include in the dictionary yet, starts from 1.
 
#create empty list for candidates and his/her vote count
candidates = []
num_votes = []

# create dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key) # show the names
    num_votes.append(value) # show the number of their votes

# creates vote percent list
vote_percentage = []
for i in num_votes:
    vote_percentage.append(i/total_votes*100)

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percentage)) # zip: gets more than one elements at that same time

#creates winner_list to put winners
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ', ' + winner_list[w]

#prints to file
#output_file = os.path.join('Output', 'election_results_' + str(file_num) +'.txt')

#with open(output_file, 'w') as txtfile:
print('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------')
for entry in clean_data:
    print(entry[0] + ': ' + str(round(entry[2],1)) +'%  (' + str(entry[1]) + ')')

print('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
# with open(output_file, 'r') as readfile:
#    print(readfile.read())