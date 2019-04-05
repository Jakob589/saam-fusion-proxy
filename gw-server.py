#!/usr/bin/env python3

import ssl
import json
import zerorpc
import paho.mqtt.client as mqtt

class GwRPC(object):
	def set_data(self, device_id, source_id, measurements):
		try:
			client.publish("saam/data/"+device_id+"/"+source_id, json.dumps(measurements))
			return True
		except:
			return False

	def set_health(self, device_id):
		try:
			client.publish("saam/health", json.dumps({ device_id: "up" }))
			return True
		except:
			return False

client = mqtt.Client(transport="websockets")
client.ws_set_options("/mqtt")
client.tls_set('/etc/ssl/certs/DST_Root_CA_X3.pem', tls_version=ssl.PROTOCOL_TLSv1_2)
client.username_pw_set("user", "secret")
client.connect("localhost", 443)
client.loop_start()

s = zerorpc.Server(GwRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
