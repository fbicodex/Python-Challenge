import os
import csv

pypoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv") 

with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvfile)
 
    #Defining our arrays and variables
    canadites = []
    canadite_votes = []
    votes_total = 0
    vote_percent = 0
    index = 0

    for row in csvreader:
    #If the name is not in canadites, add to the array; canadite votes needs to be appended with value 0 as a starting value
        if row[2] not in canadites:
            canadites.append(row[2])
            canadite_votes.append(0)

    #for every row, add a vote
        votes_total = votes_total + 1
    #created index function -> saying I want index of canadites with the parameter being the name of current row in column 3
        index = canadites.index(row[2])
    #on current row -> looks to see what the canadite is, then adds a vote for that canadite (sees Khan, adds one to Khan)
        canadite_votes[index] =  canadite_votes[index] + 1

    #Start printing with Headers and Total Votes to text file and terminal
    f = open("poll_output.txt", "a")

    print("-------------------------------------",file=f)
    print("Election Results",file=f)
    print("-------------------------------------",file=f)
    print(f"Total Votes: {votes_total}",file=f)
    print("-------------------------------------",file=f)


    print("-------------------------------------")
    print("Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {votes_total}")
    print("-------------------------------------")

    #Making While loop -> setting i to 0 and winner canadites[0] -> this is to initalize to a canadites name (go to the first variable in the array)
    i = 0
    winner = canadites[0]

    #while loops will go through the length of the array and will stop once the array is complete
    while i < len(canadites):
    #vote perct will be what the current position of i is in the canadite votes array divided by total votes
        vote_percent = canadite_votes[i]/votes_total
    #formating vote percent to be -> 0.000%
        vote_percent = "{:.3%}".format(vote_percent)
    #starting if statement with finding index of winner in canadites array -> with winner starting in first postion; so canadites will start with first postion 
    #then finding the position for canadiate votes through candaties array -> if the value of the votes is less than the current iteration's position -> must be winner 
        if canadite_votes[canadites.index(winner)] < canadite_votes[i]:
            winner = canadites[i]
    #printing the current iteration's canadites, vote percent for that canadite, and vote for that canadite to text file and terminal
        print(f"{canadites[i]}:  {vote_percent}  ({canadite_votes[i]}) ",file=f)

        print(f"{canadites[i]}:  {vote_percent}  ({canadite_votes[i]}) ")
    #add one to i to move on to the next postion; once the length of canadites has been met -> end while loop
        i = i + 1
    #print out winner to text file and terminal 
    print("-------------------------------------",file=f)
    print(f"The winner is: {winner}",file=f)

    print("-------------------------------------")
    print(f"The winner is: {winner}")

    f.close()

