#!/usr/bin/env python
import csv

# updates avaialble at http://www.football-data.co.uk/mmz4281/1516/E0.csv
# wget < http://www.football-data.co.uk/mmz4281/1516/E0.csv
# save as current.csv

dfile = open('donor.csv', "rb")
reader = csv.reader(dfile)

club = []
old_club = []
for row in reader:
 old_club.append(row[0])
 club.append(row[1])

dfile.close()

ofile = open('previous.csv', "rb")
oreader = csv.reader(ofile)
board = [[' ']*20 for _ in range(20)]

firstLine = 1
for row in oreader:
 if firstLine:
   firstLine = 0
   continue
 hclub = old_club.index(row[2])
 aclub = old_club.index(row[3])
 board[hclub][aclub] = row[6]

ofile.close() 

ocfile = open('previousC.csv', "rb")
ocreader = csv.reader(ocfile)

for row in ocreader:  # substitute English football League Championships results for epl donors
 hclub = club.index(row[2])
 aclub = club.index(row[3])
 board[hclub][aclub] = row[6]

ocfile.close()


club_away_points = []
for i in range(0,20):
 club_away_points.append(0)

slide = 0
club_home_points = []

for i in range(0,20):
 club_home_points.append(0)
 for j in range(0,20):
   if board[i][j] == 'H':
     club_home_points[i] += 3
   elif board[i][j] == 'D':
     club_home_points[i] += 1
     club_away_points[j] += 1
   elif board[i][j] == 'A':
     club_away_points[j] += 3


new_points = []
difference = []
old_points = []
for i in range(0,20):
 old_points.append(club_home_points[i] + club_away_points[i])
 new_points.append(old_points[i])
 difference.append(0)

cfile = open('current.csv', "rb")
creader = csv.reader(cfile)


firstLine = 1
for row in creader:
 if firstLine:
   firstLine = 0
   continue
 if board[club.index(row[2])][club.index(row[3])] == row[6]:  # same result
   continue
 if board[club.index(row[2])][club.index(row[3])] == 'H':
   if row[6] == 'D':
     new_points[club.index(row[2])] -= 2
     difference[club.index(row[2])] -= 2
     new_points[club.index(row[3])] += 1
     difference[club.index(row[3])] += 1
   elif row[6] == 'A':
     new_points[club.index(row[2])] -= 3
     difference[club.index(row[2])] -= 3
     new_points[club.index(row[3])] += 3
     difference[club.index(row[3])] += 3
 elif board[club.index(row[2])][club.index(row[3])] == 'D':
   if row[6] == 'H':
     new_points[club.index(row[2])] += 2
     difference[club.index(row[2])] += 2
     new_points[club.index(row[3])] -= 1
     difference[club.index(row[3])] -= 1
   elif row[6] == 'A':
     new_points[club.index(row[2])] -= 1
     difference[club.index(row[2])] -= 1
     new_points[club.index(row[3])] += 2
     difference[club.index(row[3])] += 2
 elif board[club.index(row[2])][club.index(row[3])] == 'A':
   if row[6] == 'H':
     new_points[club.index(row[2])] += 3
     difference[club.index(row[2])] += 3
     new_points[club.index(row[3])] -= 3
     difference[club.index(row[3])] -= 3
   elif row[6] == 'D':
     new_points[club.index(row[2])] += 1
     difference[club.index(row[2])] += 1
     new_points[club.index(row[3])] -= 2
     difference[club.index(row[3])] -= 2

cfile.close()

for i in range(0,20):
 print '%s,%d,%d' % (club[i], difference[i], new_points[i])
