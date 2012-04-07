import unittest
import tests.auxiliary
from authentication_server.authentication_server_initializer import AuthenticationServerInitializer
from mock import Mock
from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2
from common.server_type import ServerType
from authentication_server.global_data import GlobalData

class AuthenticationServerInitializerTest(unittest.TestCase):
	def setUp(self):
		self.server_initializer = AuthenticationServerInitializer('localhost:34510', 'localhost:34511')
		
	def test_construction(self):
		self.assertEqual(self.server_initializer.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.sub_address, 'localhost:34511')
		self.assertTrue(self.server_initializer.global_data is None)
		self.assertTrue(self.server_initializer.rmq is None)
		self.assertTrue(self.server_initializer.server_handler_dispatcher is None)
		
	def test_init_server_handler_dispatcher(self):
		self.server_initializer.init_server_handler_dispatcher()
		self.assertEqual(len(self.server_initializer.server_handler_dispatcher.handlers), 2)
		
	def test_init_global_data(self):
		self.server_initializer.init_global_data()
		self.assertEqual(len(self.server_initializer.global_data.server_manager.servers), 0)
		self.assertEqual(self.server_initializer.global_data.server_name, 'authentication_server')
		
	def test_init_rmq(self):
		self.server_initializer.init_global_data()
		self.server_initializer.init_rmq()
		self.assertEqual(self.server_initializer.global_data.rmq.pub_address, 'localhost:34510')
		self.assertEqual(self.server_initializer.global_data.rmq.sub_address, 'localhost:34511')
		self.assertEqual(self.server_initializer.global_data.rmq, self.server_initializer.rmq)
		self.assertEqual(self.server_initializer.rmq.global_data, self.server_initializer.global_data)

	def test_send_init_request(self):
		self.server_initializer.rmq = Mock()
		self.server_initializer.rmq.send_message_string = Mock()
		self.server_initializer.global_data = GlobalData()
		self.server_initializer.global_data.server_name = 'authentication_server'
		self.server_initializer.send_init_request()
		
		message = protocol.protocol_message_pb2.StartServerInitRequest()
		message.name = 'authentication_server'		
		message.type = ServerType.AUTHENTICATION_SERVER
		self.server_initializer.rmq.send_message_string.assert_called_with(message, 'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

def get_tests():
	return unittest.makeSuite(AuthenticationServerInitializerTest)

if '__main__' == __name__:
	unittest.main()