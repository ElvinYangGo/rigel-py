import unittest
import tests.auxiliary
from master_server.heart_beat_notice_handler import HeartBeatNoticeHandler
import protocol
from network.channel_buffer import ChannelBuffer
from common.global_data import GlobalData
from master_server.master_server_manager import MasterServerManager
from common.server_type import ServerType
from common.server_status import ServerStatus

class HeartBeatNoticeHandlerTest(unittest.TestCase):
	def setUp(self):
		self.handler = HeartBeatNoticeHandler()
	
	def test_handle_message(self):
		message = protocol.server_message_pb2.HeartBeatNotice()
		message.name = u'sa'
		channel_buffer = ChannelBuffer(message.SerializeToString())
		
		GlobalData.inst = GlobalData()
		GlobalData.inst.server_manager = MasterServerManager()
		GlobalData.inst.server_manager.add_server('sa', ServerType.AUTH_SERVER)
		GlobalData.inst.server_manager.get_server('sa').set_status(ServerStatus.SERVER_STATUS_CLOSED)
		
		self.handler.handle_message(1, channel_buffer, channel_name='test_channel')
		self.assertTrue(GlobalData.inst.server_manager.get_server('sa').get_heart_beat_time() != 0)
		
def get_tests():
	return unittest.makeSuite(HeartBeatNoticeHandlerTest)

if '__main__' == __name__:
	unittest.main()