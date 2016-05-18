import re,sys,os

#check the number of arguments
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename"%sys.argv[0])

filename = sys.argv[1]

if not os.path.exists("%s.txt"%filename):
	sys.exit("Error: File '%s' not found"%sys.argv[1])

#filename = "cardinals-1940"
#read the file from the directory
f = open("%s.txt"%filename)
#set the regular expression to extract the main information
regex = re.compile(r"^([A-Z][A-Za-z ]*) batted (\d+) times with (\d+) hits and (\d+) runs$")

def find_info(test):
	#do the match
	match = regex.match(test)
	if match is not None:
		return (match.group(1),float(match.group(2)),float(match.group(3)),float(match.group(4)))
	else:
		return ("",0,0,0)

#do the match for every person
bat = {}
hit = {}
for line in f:
	(name,bats,hits,runs) = find_info(line.rstrip())
	if name != "":
		if name in bat.keys():
			bat[name] = bat[name]+bats
			hit[name] = hit[name]+hits
		else:
			bat[name] = bats
			hit[name] = hits

f.close()

#compute the average batting for every person
battingavg = {}
for name,perbat in bat.items():
	battingavg[name] = round(hit[name]/perbat,3)

#write the result to the file
with open("%s-new.txt"%filename, 'w') as f:
	#sort the result by average
	for name in sorted(battingavg,key = battingavg.get,reverse=True):
		s = "%s: %.3f\n"%(name,battingavg[name])
		print s
		f.write(s)

print "end"