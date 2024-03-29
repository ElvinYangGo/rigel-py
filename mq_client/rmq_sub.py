import zmq
import threading
from network.channel_buffer import ChannelBuffer
import common.utf8_codec

class RMQSub(threading.Thread):
	def __init__(self, sub_address, context, pipeline):
		self.sub_address = sub_address
		self.pipeline = pipeline

		self.sub_socket = context.socket(zmq.SUB)
		self.sub_socket.connect('tcp://' + self.sub_address)

		threading.Thread.__init__(self, name='rmq')

	def subscribe(self, channel_name):
		self.sub_socket.setsockopt_unicode(zmq.SUBSCRIBE, channel_name)

	def run(self):
		while True:
			message = self.sub_socket.recv()
			#print message
			more = self.sub_socket.getsockopt(zmq.RCVMORE)
			if more:
				channel_name = common.utf8_codec.utf8_decode(message)
				if channel_name == u'server_init':
					print 'channel name: %s' % (channel_name)
			else:
				if channel_name == u'server_init':
					print 'channel name: %s, message: %s' % (channel_name, message)
				channel_buffer = ChannelBuffer(message)
				self.pipeline.handle_upstream(channel_buffer, channel_name=channel_name)
				channel_name = u''
