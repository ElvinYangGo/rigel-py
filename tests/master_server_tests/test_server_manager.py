import unittest
import tests.auxiliary
from master_server.server_manager import ServerManager
from master_server.server import Server
import protocol.server_message_pb2
from common.server_status import ServerStatus
from common.server_type import ServerType
from mock import Mock

class ServerManagerTest(unittest.TestCase):
	def setUp(self):
		self.server_manager = ServerManager()
		
	def test_add_server(self):
		self.server_manager.add_server('aaa', ServerType.GATEWAY_SERVER)
		server = self.server_manager.get_server('aaa')
		self.assertTrue(server.starting())
		self.assertEqual(server.get_name(), 'aaa')
		self.assertEqual(server.get_type(), ServerType.GATEWAY_SERVER)

		ServerManager.Server = Mock()
		server.set_status(ServerStatus.SERVER_STATUS_CLOSED)
		self.server_manager.add_server('aaa', ServerType.GATEWAY_SERVER)
		self.assertFalse(ServerManager.Server.called)
		self.assertEqual(server.get_status(), ServerStatus.SERVER_STATUS_STARTING)
		
	def test_running_server_to_net(self):
		self.server_manager.add_server('aaa', ServerType.GATEWAY_SERVER)
		self.server_manager.add_server('bbb', ServerType.GATEWAY_SERVER)
		server = self.server_manager.get_server('aaa')
		server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
		net_string = self.server_manager.running_server_to_net()
		self.assertEqual(len(net_string.servers), 1)
		self.assertEqual(net_string.servers[0].name, 'aaa')
		self.assertEqual(net_string.servers[0].status, ServerStatus.SERVER_STATUS_RUNNING)
		self.assertEqual(net_string.servers[0].type, ServerType.GATEWAY_SERVER)

def get_tests():
	return unittest.makeSuite(ServerManagerTest)

if '__main__' == __name__:
	unittest.main()