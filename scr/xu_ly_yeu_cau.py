import sqlite3

db_name = 'database.db'

def query_two_parts(inp):
	global db_name
	conn = sqlite3.connect(db_name)
	cursor = conn.execute("SELECT * from VeXoSo where ThanhPho = '"+ inp[0] +"' AND VeSo = "+ inp[1] + " ")
	
	return cursor
def query_one_part(inp):
	conn = sqlite3.connect(db_name)
	cursor = conn.execute("SELECT * from VeXoSo where ThanhPho = '"+ inp[0] +"' ")
	
	return cursor

def input_is_valid(inp):
	global db_name
	conn = sqlite3.connect(db_name)
	city_names = conn.execute("SELECT distinct(ThanhPho) from VeXoSo")
	city_names = [name[0] for name in city_names]	
	conn.close()
	if inp[0] in city_names:
		return True
	return False

def get_cities():
	global db_name
	conn = sqlite3.connect(db_name)
	city_names = conn.execute("SELECT distinct(ThanhPho) from VeXoSo")
	city_names = [name[0] for name in city_names]
	return city_names 

def get_result(inp):
	
	inp = inp.split()

	# Gửi tên các thành phố chỉ cách truy vấn
	if inp[0].lower()=="h":
		return get_cities()
	if (not input_is_valid(inp)):		
		return 0

	# Nếu gửi theo cú pháp <Tỉnh thành> <Vé Số>
	if (len(inp) == 2):
		cursor = query_two_parts(inp)		

		row = list(cursor)
		if len(row) > 0:
			row = row[0]
			return ["Chúc mừng bạn đã trúng %s trị giá %s" % (row[2], row[3])]
		else:
			return ["Xin lỗi bạn không trúng giải nào cả!"]
	# Nếu gửi theo cú pháp <Tỉnh thành>
	elif (len(inp) == 1):
		cursor = list(query_one_part(inp))
		# Nếu có tỉnh thành 
		# Kiểm tra cho kĩ :Db
		if len(cursor) > 0:
			return cursor
		else:
			return ""



if __name__ == '__main__':
	
	print((get_result("BenTre 89")))
	
	input("Press any key to stop")