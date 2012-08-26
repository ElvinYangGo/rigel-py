from common.server import Server
import protocol.protocol_message_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from common.global_data import GlobalData

class SyncServerStatusNoticeHandler:
	def handle_message(self, message_id, channel_buffer, **kwargs):
		pass
	"""
		message = protocol.protocol_message_pb2.SynchronizeServerNotification.FromString(channel_buffer.read_all_data())
		for server_net in message.servers:
			if server_net.status == ServerStatus.SERVER_STATUS_RUNNING:
				self.handle_running_server(GlobalData.instance, server_net)
			elif server_net.status == ServerStatus.SERVER_STATUS_CLOSED:
				self.handle_closed_server(GlobalData.instance, server_net)
				
	def handle_running_server(self, GlobalData.instance, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER:
			server = Server(server_net.name, server_net.type, server_net.status)
			GlobalData.instance.server_manager.add_server(server)
	
	def handle_closed_server(self, GlobalData.instance, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER:
			GlobalData.instance.server_manager.remove_server(server_net.name)
	"""