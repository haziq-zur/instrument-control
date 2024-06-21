import pyvisa

class InstrumentController: 
	def __init__(self):
		self.resource_manager = pyvisa.ResourceManager()

	def get_resource_list(self):
		return self.resource_manager.list_resources()
	
	def open_connection(self, resource_id):
		try:
			self.instr = self.resource_manager.open_resource(resource_id)
			print("Success! Instrument is connected.")
			print(self.instr.resource_name)
		except:
			print("An exception occured! Unable to open connection to instrument.")

	def query(self, query_str):
		return self.instr.query(query_str)
	
	def write(self, cmd_str):
		self.instr.write(cmd_str)
	
	def read(self):
		return self.instr.read()
	
	def query_image(self, cmd_str):
		# Get binary block for image file and store it as byte array block
		instr_data = self.instr.query_binary_values(cmd_str, delay=2, datatype='B', is_big_endian=False, container=bytearray)

		# Write image file
		with open(f'.\image.bmp', 'wb') as target:
			target.write(instr_data)
		print("Image was save as BMP.")