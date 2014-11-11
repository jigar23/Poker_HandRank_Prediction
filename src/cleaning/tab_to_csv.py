import sys
import re

if (len(sys.argv) != 3):
	print "ERROR: Check usage"
	print "python tab_to_csv.py <option> <input_filename>"
	print "option : "
	print "-hdb     for Hand file"
	print "-hroster  number of playes info"
	print "-player  specific player info" 
	print ""
	print "E.g. Run the file as follows:"
	print "python tab_to_csv.py -hdb hdb"
	sys.exit()

filename = sys.argv[2] + '.csv'
fcsv = open(filename,'w+')

line_hdb = 'gameid	dealer	noOfhands	players	flop	turn	river	showdown	firstcard	secondcard	thirdcard	fourthcard	fifthcard'
line_hroster = 'GameId	noOfPlayers	Player1	Player2	Player3	Player4	Player5	Player6	Player7	Player8'
line_player = 'player	gameId	noOfPlay	pos	prflop	flop	turn	river	bankroll	action	winnings	playercard1 playercard2'

# Write the first line
if (sys.argv[1] == '-hdb'):
	line = ','.join(re.findall('\"[^\"]*\"|\S+', line_hdb)) + '\n'
	fcsv.write(line)
elif (sys.argv[1] == '-hroster'):
	line = ','.join(re.findall('\"[^\"]*\"|\S+', line_hroster)) + '\n'
	fcsv.write(line)
elif (sys.argv[1] == '-player'):
	line = ','.join(re.findall('\"[^\"]*\"|\S+', line_player)) + '\n'
	fcsv.write(line)
else:
	print "ERROR: incorrect option specified"
	print "Exiting ..."
	sys.exit()

# Replace spaces/tabs with comma and write it to new file
with open(sys.argv[2],'r') as f:
	for line in f:
		line = ','.join(re.findall('\"[^\"]*\"|\S+', line)) + '\n'
		fcsv.write(line)

print "Created file " + filename
fcsv.close()