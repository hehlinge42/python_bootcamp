from csvreader import CsvReader

if __name__ == "__main__":
	with CsvReader('good.csv') as file:
		header = file.getheader()
		data = file.getdata()
		print("header")
		print(header)
		for line in data:
			print(line)
print()
if __name__ == "__main__":
	with CsvReader('bad.csv') as file:
		pass
