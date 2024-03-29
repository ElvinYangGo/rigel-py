from generator.plain_class_accessor_generator.plain_pair_map_accessor_writer import PlainPairMapAccessorWriter
from generator.plain_class_accessor_generator.plain_map_accessor_writer import PlainMapAccessorWriter
from generator.plain_class_accessor_generator.plain_list_accessor_writer import PlainListAccessorWriter
from generator.plain_class_accessor_generator.plain_list_map_accessor_writer import PlainListMapAccessorWriter
from generator.plain_class_accessor_generator.plain_global_list_accessor_writer import PlainGlobalListAccessorWriter
from generator.plain_class_accessor_generator.plain_global_sorted_set_accessor_writer import PlainGlobalSortedSetAccessorWriter
from generator.plain_class_accessor_generator.plain_sorted_set_accessor_writer import PlainSortedSetAccessorWriter
from generator.plain_class_accessor_generator.plain_global_id_accessor_writer import PlainGlobalIDAccessorWriter

class PlainClassAccessorWriter(object):
	def __init__(self, file_name, table_desc_array):
		self.file_name = file_name
		self.table_desc_array = table_desc_array

	def write(self):
		with open(self.file_name, 'w') as f:
			self.write_class_head(f)
			self.write_class_body(f)
			f.flush()
	
	def write_class_head(self, f):
		f.write('#This file is generated by program. DO NOT EDIT IT MANUALLY!\n')
		self.write_import_declaration(f)
		f.write('class PlainClassAccessor(object):\n')
	
	def write_import_declaration(self, f):
		f.write('from redis_client.redis_accessor import RedisAccessor\n')
		f.write('from redis_client.redis_key import RedisKey\n')
		for table_desc in self.table_desc_array:
			table_type = table_desc['table_type']
			if table_type == 'map':
				plain_map_accessor_writer = PlainMapAccessorWriter(table_desc, f)
				plain_map_accessor_writer.write_import_declaration()
			elif table_type == 'list':
				plain_list_accessor_writer = PlainListAccessorWriter(table_desc, f)
				plain_list_accessor_writer.write_import_declaration()
			elif table_type == 'list_map':
				plain_list_map_accessor_writer = PlainListMapAccessorWriter(table_desc, f)
				plain_list_map_accessor_writer.write_import_declaration()
		f.write('\n')
					
	def write_class_body(self, f):
		self.write_init_function(f)
		for table_desc in self.table_desc_array:
			table_type = table_desc['table_type']
			if table_type == 'map':
				plain_map_accessor_writer = PlainMapAccessorWriter(table_desc, f)
				plain_map_accessor_writer.write()
			elif table_type == 'list':
				plain_list_accessor_writer = PlainListAccessorWriter(table_desc, f)
				plain_list_accessor_writer.write()
			elif table_type == 'list_map':
				plain_list_map_accessor_writer = PlainListMapAccessorWriter(table_desc, f)
				plain_list_map_accessor_writer.write()
			elif table_type == 'global_list':
				plain_global_list_accessor_writer = PlainGlobalListAccessorWriter(table_desc, f)
				plain_global_list_accessor_writer.write()
			elif table_type == 'global_sorted_set':
				plain_global_sorted_set_accessor_writer = PlainGlobalSortedSetAccessorWriter(table_desc, f)
				plain_global_sorted_set_accessor_writer.write()
			elif table_type == 'sorted_set':
				plain_sorted_set_accessor_writer = PlainSortedSetAccessorWriter(table_desc, f)
				plain_sorted_set_accessor_writer.write()
			elif table_type == 'pair_map':
				plain_pair_map_accessor_writer = PlainPairMapAccessorWriter(table_desc, f)
				plain_pair_map_accessor_writer.write()
			elif table_type == 'global_id':
				plain_global_id_accessor_writer = PlainGlobalIDAccessorWriter(table_desc, f)
				plain_global_id_accessor_writer.write()

	def write_init_function(self, f):
		f.write('\tdef __init__(self):\n')
		f.write('\t\tself.redis_accessor = RedisAccessor()\n')
		f.write('\t\tself.redis_key = RedisKey()\n\n')
