class CsvReader:

	def __init__(self, filename, sep=',', header=True, skip_top=1, skip_bottom=1):
		
		self.filename = filename
		self.sep = sep
		self.has_header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
	
		try:
			file = open(self.filename, mode='r')
			self.file = file
			data = []
			len_line = -1
			for line in file:
				line_list = line.split(sep=self.sep)
				if len_line == -1:
					len_line = len(line_list)
				if len_line != len(line_list):
					raise ValueError
				data.append(line_list)
			self.data = data
			if self.has_header is True:
				self.header = self.data.pop(0)
			else:
				self.header = None
			nb_lines_skipped = 0
			while nb_lines_skipped < self.skip_top:
				self.data.pop(0)
				nb_lines_skipped += 1
			nb_lines_skipped = 0
			while nb_lines_skipped < self.skip_bottom:
				self.data.pop(-1)
				nb_lines_skipped += 1

		except OSError:
			self.file = None
			print("Unable to open file '%s'" %(filename))

		except ValueError:
			self = None
			print("File is corrupted")
		else:
			return self


	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.file and not self.file.closed:
			self.file.close()

	def getdata(self):
		return self.data

	def getheader(self):
		return self.header
