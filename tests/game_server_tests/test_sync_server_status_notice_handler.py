import unittest
import tests.auxiliary
import protocol.server_message_pb2
import protocol.server_data_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from common.server_manager import ServerManager
from mock import Mock
from game_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler
from common.global_data import GlobalData

class SyncServerStatusNoticeHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = SyncServerStatusNoticeHandler()
		
	def test_handle_running_server(self):
		server_net = protocol.server_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.AUTH_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = protocol.server_data_pb2.Server()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_RUNNING
		
		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = ServerManager()
		
		self.handler.handle_running_server(server_net)
		self.handler.handle_running_server(server_net2)
		
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 1)
		self.assertEqual(GlobalData.inst.server_manager.servers.get('sb').get_name(), 'sb')
		self.assertEqual(GlobalData.inst.server_manager.servers.get('sb').get_type(), ServerType.GATEWAY_SERVER)
		self.assertEqual(GlobalData.inst.server_manager.servers.get('sb').get_status(), ServerStatus.SERVER_STATUS_RUNNING)

	def test_handle_closed_server(self):
		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = ServerManager()
		GlobalData.inst.server_manager.add_server('sa', ServerType.GATEWAY_SERVER, ServerStatus.SERVER_STATUS_RUNNING)
		
		server_net = protocol.server_data_pb2.Server()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
	
		self.handler.handle_closed_server(server_net)
		
		self.assertEqual(len(GlobalData.inst.server_manager.servers), 0)
		
	def test_handle_message(self):
		message = protocol.server_message_pb2.SyncServerNotice()
		server_net = message.servers.add()
		server_net.name = 'sa'
		server_net.type = ServerType.GATEWAY_SERVER
		server_net.status = ServerStatus.SERVER_STATUS_RUNNING
		server_net2 = message.servers.add()
		server_net2.name = 'sb'
		server_net2.type = ServerType.GATEWAY_SERVER
		server_net2.status = ServerStatus.SERVER_STATUS_CLOSED
		
		channel_buffer = ChannelBuffer(message.SerializeToString())
		self.handler.handle_closed_server = Mock()
		self.handler.handle_running_server = Mock()
		
		self.handler.handle_message(1, channel_buffer, channel_name=u'test_channel')
		
		self.handler.handle_running_server.assert_called_with(server_net)
		self.handler.handle_closed_server.assert_called_with(server_net2)

def get_tests():
	return unittest.makeSuite(SyncServerStatusNoticeHandlerTest)

if '__main__' == __name__:
	unittest.main()