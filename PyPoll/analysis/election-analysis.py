import os
import csv
import sys

election_data = os.path.join('..', 'Resources','election_data.csv')

with open(election_data) as election_data_csv:
    reader = csv.reader(election_data_csv, delimiter=',')
    next(reader)
    row_count = 0
    votes = 0
    cand_tally = {}
    winner = ''
    
    
    for row in reader:
        row_count +=1
        try:
            last_name = row[2]
            if last_name in cand_tally:
                cand_tally[last_name] +=1
            if  last_name not in cand_tally:
                cand_tally[last_name] = 1                  
        except ValueError:
            continue

    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes:{(row_count)-1}')
    print(f'-------------------------')
    for candidate in cand_tally:
        vote_count = cand_tally[candidate]
        vote_p = round((vote_count / (row_count-1) *100), 4)
        print(f'{candidate}: {(vote_p)}% ({(vote_count)})')
        if winner is '' or cand_tally[candidate] > cand_tally[winner]:
            winner = candidate
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')


# Write to text file
    sys.stdout = open("election-analysis.txt", "w")
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes:{(row_count)-1}')
    print(f'-------------------------')
    for candidate in cand_tally:
        vote_count = cand_tally[candidate]
        vote_p = round((vote_count / (row_count-1) *100), 4)
        print(f'{candidate}: {(vote_p)}% ({(vote_count)})')
        if winner is '' or cand_tally[candidate] > cand_tally[winner]:
            winner = candidate
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')
    sys.stdout.close()



