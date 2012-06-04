#This file is generated by program. DO NOT EDIT IT MANUALLY!
class RedisTable(object):
	def get_user_key(self, id_string):
		return 'user:' + id_string

	def get_user_table_user_id_field(self):
		return 'user_id'

	def get_user_table_user_name_field(self):
		return 'user_name'

	def get_item_list_key(self, id_string):
		return 'item_list:' + id_string

	def get_friend_list_key(self, id_string):
		return 'friend_list:' + id_string

	def get_friend_key(self, id_string):
		return 'friend:' + id_string

	def get_friend_table_user_id_field(self):
		return 'user_id'

	def get_friend_table_user_name_field(self):
		return 'user_name'

	def get_online_player_list_key(self):
		return 'online_player_list'

	def get_level_rank_key(self):
		return 'level_rank'

	def get_race_score_rank_key(self, id_string):
		return 'race_score_rank:' + id_string

