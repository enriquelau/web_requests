import csv, time, subprocess, atexit, sys, os

def closeConnection():
	subprocess.call(["sudo", "killall openvpn"])
	
def openConnection(argument):
	subprocess.call(["sudo", "openvpn", argument])

if __name__ == "__main__":

	filePath = os.path.join(sys.path[0], 'proton_server_names.csv')
	
	atexit.register(closeConnection)
	
	with open(filePath) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		argList = list(csv_reader)
		
	i = 0	
	
	if len(sys.argv) > 1:
		if sys.argv[1].isnumeric():
			timeToSleep = 60*int(sys.argv[1])
	
	else:
		timeToSleep = 60*7
	
	while True:
	
		openConnection(argList[i][0])
		i += 1
		if i == len(argList):
			i = 0
		time.sleep(timeToSleep)
		closeConnection()
