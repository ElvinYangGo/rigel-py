from master_server.master_global_data import MasterGlobalData
from common.server_initializer import ServerInitializer
from master_server.server_manager import ServerManager
from mq_client.rmq import RMQ
from common.channel_name import ChannelName
from master_server.heart_beat_monitor import HeartBeatMonitor
from common.global_data import GlobalData

class MasterServerInitializer(ServerInitializer):
	def __init__(self, pub_address, sub_address, server_name, pipeline, server_option_reader):
		super(MasterServerInitializer, self).__init__(pub_address, sub_address, server_name, pipeline)
		self.server_option_reader = server_option_reader
			
	def init_global_data(self):
		GlobalData.instance = MasterGlobalData()
		super(MasterServerInitializer, self).init_global_data()
		GlobalData.instance.server_manager = ServerManager()
		GlobalData.instance.server_option_reader = self.server_option_reader
		
		self.init_heart_beat_monitor()
	
	def init_rmq(self):	
		self.rmq = RMQ(self.pub_address, self.sub_address, GlobalData.instance.zmq_context, self.pipeline)
		self.rmq.subscribe(ChannelName.SERVER_INITIALIZATION)
	
		GlobalData.instance.rmq = self.rmq
	
		self.rmq.start()

		#move to another function
		self.rmq.subscribe(ChannelName.HEART_BEAT)

	def init_heart_beat_monitor(self):
		heart_beat_interval = self.server_option_reader.get_server_option_config().get_heart_beat_interval()
		heart_beat_timeout = self.server_option_reader.get_server_option_config().get_heart_beat_timeout()
		GlobalData.instance.heart_beat_monitor = HeartBeatMonitor(heart_beat_interval, heart_beat_timeout)
		GlobalData.instance.heart_beat_monitor.start()
	