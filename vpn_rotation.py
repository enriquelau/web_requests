import subprocess
import csv
import pandas as pd

filename = "vpn_server_names.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)
        print(row[1])


'''
with open("vpn_server_names.csv", delimiter= ',') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
    for row in reader:
        array.append(row)
        print(array[1]) 
'''



'''
df = pd.read_csv(r'~/web_requests/vpn_server_names.csv')

print(df)

with open ('vpn_server_names.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)



profiles = 
for i in profiles:


subprocess.call(['ls','-l'], shell=True)
sudo openvpn us.protonvpn.com.udp.ovpn

The above command is how to use openvpn to connect to a 
vpn server

'''
