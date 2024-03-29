import json

class ProtocolIDWriter(object):
	def __init__(self, desc_file_name, out_file_name, out_class_name, prefix, suffix, comment):
		self.desc_file_name = desc_file_name
		self.out_file_name = out_file_name
		self.out_class_name = out_class_name
		self.prefix = prefix
		self.suffix = suffix
		self.comment = comment

	def write(self):
		desc_file = open(self.desc_file_name)
		desc = json.load(desc_file)
		with open(self.out_file_name, 'w') as f:
			f.write('{}This file is generated by program. DO NOT EDIT IT MANUALLY!\n'.format(self.comment))
			self.write_class_head(f)
			self.write_id_type(desc, f)
			self.write_id_value(desc, f)
			self.write_class_tail(f)
			f.flush()
			
	def write_class_head(self, f):
		pass
	
	def write_class_tail(self, f):
		pass

	def write_id_type(self, desc, f):
		f.write('\t{}ID_TYPE_MAGIC = 0xff00{}\n\n'.format(self.prefix, self.suffix))
		for direction_key, direction_value in desc.items():
			if direction_value.has_key('id_prefix'):
				f.write(
					'\t{}ID_TYPE_{} = {}{}\n'.format(
							self.prefix, direction_key.upper(), direction_value['id_prefix'], self.suffix)
					)
		f.write('\n')
	
	def write_id_value(self, desc, f):
		for direction_key, direction_value in desc.items():
			self.write_direction(direction_key, direction_value, f)
			f.write('\n')
		
	def write_direction(self, direction_key, direction_value, f):
		f.write('\t{}{} id_start:{}\n'.format(self.comment, direction_key, direction_value['id_start']))
		f.write(
			'\t{}{}_ID_START = {}{}\n'.format(
				self.prefix, direction_key.upper(), direction_value['id_start'], self.suffix)
			)
		id_index = int(direction_value['id_start'], 16)
		for id_desc in direction_value['id_list']:
			f.write(
				'\t{}P_{} = {:#06x}{}\n'.format(self.prefix, id_desc['id'], id_index, self.suffix)
				)
			if id_desc.has_key('result'):
				self.write_protocol_result(id_desc['result'], id_desc['id'], id_index, f)
			id_index += 1

	def write_protocol_result(self, result_list, id_name, id_index, f):
		result_index = 1
		result_value = (id_index << 16) + result_index
		f.write(
			'\t{}R_{}_SUCCESS = {:#010x}{}\n'.format(self.prefix, id_name, result_value, self.suffix)
			)
		result_index += 1
		result_value = (id_index << 16) + result_index
		f.write(
			'\t{}R_{}_FAILURE = {:#010x}{}\n'.format(self.prefix, id_name, result_value, self.suffix)
			)
		result_index += 1
		for result in result_list:
			result_value = (id_index << 16) + result_index
			f.write(
				'\t{}R_{}_{} = {:#010x}{}\n'.format(self.prefix, id_name, result, result_value, self.suffix)
				)
			result_index += 1