import threading
import time
from common.channel_name import ChannelName
from protocol.server_protocol_id import ServerProtocolID
import protocol
from common.global_data import GlobalData

class HeartBeat(threading.Thread):
	def __init__(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
		threading.Thread.__init__(self, name='heart_beat')
		
	def run(self):
		while True:
			message = protocol.server_message_pb2.HeartBeatNotice()
			message.name = GlobalData.inst.server_name
			GlobalData.inst.heart_beat_rmq_pub.send_message(
				message, ChannelName.HEART_BEAT, ServerProtocolID.P_HEART_BEAT_NOTICE
				)
			time.sleep(self.heart_beat_interval/1000)
			
	def set_heart_beat_interval(self, heart_beat_interval):
		self.heart_beat_interval = heart_beat_interval
