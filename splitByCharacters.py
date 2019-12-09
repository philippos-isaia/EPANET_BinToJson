import json

json_file=open('Virtual_City_WaterNetworkStopAfter3_bin.json')
data = json.load(json_file)
data=str(data)
n = 110
line= [(data[i:i+n]) for i in range(0, len(data), n)] 
f= open("splittedNEWText.txt","w+") 
for lines in line:
	f.write(lines+"\n")
f.close()