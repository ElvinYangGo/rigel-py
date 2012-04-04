import zmq
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from network.twisted_protocol_factory import TwistedProtocolFactory 
from network.channel_pipeline_factory import ChannelPipelineFactory
from network.buffer_head_codec import BufferHeadCodec
from common.handler_dispatcher import HandlerDispatcher

from common.server_handler_dispatcher import ServerHandlerDispatcher
from mq_client.rmq import RMQ
from protocol.protocol_id import ProtocolID
from network.channel_buffer import ChannelBuffer
from authentication_server.global_data import GlobalData
from authentication_server.start_server_init_response_handler import StartServerInitResponseHandler 
from authentication_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler 
from authentication_server.server_manager import ServerManager
from common.server_type import ServerType
import protocol.protocol_message_pb2
def init_rmq():	
	global_data = GlobalData()
	global_data.server_manager = ServerManager()
	
	server_handler_dispatcher = ServerHandlerDispatcher()
	server_handler_dispatcher.append_handler(
		ProtocolID.START_SERVER_INIT_RESPONSE,
		StartServerInitResponseHandler()
		)
	server_handler_dispatcher.append_handler(
		ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
		SynchronizeServerStatusNotificationHandler()
		)
	rmq = RMQ('tcp://localhost:34510', 'tcp://localhost:34511', server_handler_dispatcher)
	rmq.subscribe('server_initialization')
	#rmq.subscribe('server_status')
	#rmq.subscribe('')
	
	global_data.rmq = rmq
	rmq.set_global_data(global_data)
	
	rmq.start()
	send_init_request(rmq)

def send_init_request(rmq):
	message = protocol.protocol_message_pb2.StartServerInitRequest()
	message.name = 'authentication_server'		
	message.type = ServerType.AUTHENTICATION_SERVER
	channel_buffer = ChannelBuffer()
	channel_buffer.append(message.SerializeToString())
	rmq.send(channel_buffer, 'server_initialization', ProtocolID.START_SERVER_INIT_REQUEST)

if __name__ == '__main__':
	print 'started'
	
	init_rmq()
	
	channel_pipeline_factory = ChannelPipelineFactory()
	channel_pipeline_factory.append_handler('buffer_head_codec', BufferHeadCodec())
	channel_pipeline_factory.append_handler('handler_dispatcher', HandlerDispatcher())
	
	endpoint = TCP4ServerEndpoint(reactor, 34500)
	endpoint.listen(TwistedProtocolFactory(channel_pipeline_factory))
	reactor.run()
	
	print 'authentication started'
	
