class ProtocolIDWriter:
	def __init__(self, file_name, id_list):
		self.id_list = id_list
		self.file_name = file_name

	def write(self):
		if not self.id_list:
			return
		
		with open(self.file_name, 'w') as f:
			f.write('class ProtocolID:\n')
			protocol_value = 1
			for protocol_id in self.id_list:
				f.write('\t' + protocol_id + ' = ' + str(protocol_value) + '\n')
				protocol_value += 1
			f.flush()
