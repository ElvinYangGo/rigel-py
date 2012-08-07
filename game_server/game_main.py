from game_server.game_server_initializer import GameServerInitializer
from common.mq_reader import MQReader
from game_server.game_handler_dispatcher import GameHandlerRegister
from game_server.game_global_data import GameGlobalData

if __name__ == '__main__':
	mq_reader = MQReader('../config/mq.xml')
	mq_reader.parse()
	mq_config = mq_reader.get_mq_config_list()[0]

	server_initializer = GameServerInitializer(
		mq_config.get_pub_address(), 
		mq_config.get_sub_address(),
		u'game_server',
		GameHandlerRegister(),
		GameGlobalData
		)
	server_initializer.initialize()

	print u'game started'
