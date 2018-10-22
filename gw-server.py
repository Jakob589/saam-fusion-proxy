import json
import zerorpc
import paho.mqtt.client as mqtt

class GwRPC(object):
	def set_data(self, device_id, source_id, measurements):
		try:		
			client.publish("saam_data/"+device_id+"/"+source_id, json.dumps(measurements))
			return True
		except:
			return False

client = mqtt.Client()
client.connect("localhost")

s = zerorpc.Server(GwRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()