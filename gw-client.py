import csv
import time
import socket
import zerorpc
import subprocess

def get_service(service_name):
	while True:
		avahi = subprocess.check_output(["avahi-browse","-rptk","_remote._tcp"])
		avahi = csv.reader(avahi.decode().split('\n'), delimiter=';')
		for row in avahi:
			if row and row[0] == "=" and service_name in row:
				try:
					socket.inet_aton(row[7])
					srv = row[7] + ":" + row[8]
					print("Service " + service_name + " discovered: " + srv)
					return srv
				except socket.error:
					pass

		time.sleep(10)

service_name = "saam-gw"
service = get_service(service_name)
c = zerorpc.Client()
c.connect("tcp://%s" % service)

for request in range (10):
	print(c.set_data("id", "feature", {"some": "thing"}))
	time.sleep(1)
