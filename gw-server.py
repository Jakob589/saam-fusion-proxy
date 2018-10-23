#!/usr/bin/env python3

import json
import zerorpc
import paho.mqtt.client as mqtt

class GwRPC(object):
	def set_data(self, device_id, source_id, measurements):
		try:
			client.publish("saam/"+device_id+"/"+source_id, json.dumps(measurements))
			return True
		except:
			return False

client = mqtt.Client()
client.connect("localhost")
client.loop_start()

s = zerorpc.Server(GwRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
