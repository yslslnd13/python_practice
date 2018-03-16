import os
import time
import random

class Map:
	def __init__(self, raw_number, symbol_number):

		self.raw_number = raw_number
		self.symbol_number = symbol_number

		#creating table
		self.table = [self.random_list(raw_number) for x in range(5)]
		self.string_list = []
		

		self.tmp_raw = []
		self.tmp_column = []


	
	#generate random raw_list
	def random_list(self, number):
		result_list = []
		for i in range(number):
			result_list.append(random.randint(1, self.symbol_number))
		return result_list


	def convert_to_negative_raw(self):

	#changing consequence value
		for i in range(self.raw_number, 2, -1):
			for k in range(1, self.symbol_number+1):
				c_num = str(k) * i
				changed_c_num = '0' * i
				if self.tmp_raw == []:
					for j in range(self.raw_number):
						self.tmp_raw.append(self.string_list[j].replace(c_num, changed_c_num))
				else:
					for j in range(self.raw_number):
						self.tmp_raw[j] = self.tmp_raw[j].replace(c_num, changed_c_num)
			
	def convert_to_negative_column(self):

		tmp_table = self.raw_to_column(self.table)
		tmp_string_list = self.table_to_string_list(tmp_table)

		#changing consequence value
		for i in range(self.raw_number, 2, -1):
			for k in range(1, self.symbol_number+1):
				c_num = str(k) * i
				changed_c_num = '0' * i
				
				if self.tmp_column == []:
					for j in range(self.raw_number):
						self.tmp_column.append(tmp_string_list[j].replace(c_num, changed_c_num))
				else:
					for j in range(self.raw_number):
						self.tmp_column[j] = self.tmp_column[j].replace(c_num, changed_c_num)

	def table_to_string_list(self, t1):
		#convert list to string method
		tmp_string_list = [] 
		for i in range(self.raw_number):
				tmp_string_list.append(''.join(str(x) for x in t1[i]))
		return tmp_string_list
			
			

	def string_to_list(self, type1):
		if type1 == 'raw':
			if self.tmp_raw is []:
				for i in range(self.raw_number):
					self.tmp_raw.append(list(self.string_list[i]))
			else:
				for i in range(self.raw_number):
					self.tmp_raw[i] = list(self.string_list[i])

		elif type1 == 'column':
			pass
	def raw_to_column(self, table):

		tmp_table = table[:]
		for i in range(self.raw_number):
					tmp_table[i] = [table[x][i] for x in range(self.raw_number)] 
		return tmp_table

	def combine(self):
		for i in range(self.raw_number):
			for j in range(self.raw_number):
				if self.tmp_raw[i][j] == '0' or self.tmp_column[j][i] == '0':
					self.table[i][j] = 0

	def sorting_zero(self):
		reversed_table = self.raw_to_column(self.table)

		for i in range(self.raw_number):
			count = reversed_table[i].count(0)
			for j in range(count):
				reversed_table[i].remove(0)
			add = [0 for x in range(count)]
			add += reversed_table[i]
			reversed_table[i] = add[:]
		return self.raw_to_column(reversed_table)
		


	def include_new_number(self):
		for i in range(self.raw_number):
			for j in range(self.raw_number):
				if self.table[i][j] == 0:
					self.table[i][j] = random.randint(1, self.symbol_number)


class Anipang:
	#create random list table
	def __init__(self):

		#raw_number for length, symbol_number for number of symbol
		self.raw_number = 5
		self.symbol_number = 3

		#create map table
		self.map1 = Map(self.raw_number, self.symbol_number)


	def master_pang(self):

		print_and_sleep()

		self.raw_pang()
		self.column_pang()
		self.combine()

		print_and_sleep()

		self.generate_new()                       
		
	def raw_pang(self):
		self.map1.string_list = self.map1.table_to_string_list(self.map1.table)         	# list raw to string
		self.map1.convert_to_negative_raw()     	# if there is above three consequence 
												# number, convert to zero

	def column_pang(self):
		self.map1.convert_to_negative_column()    	# consequence number to negative
		#self.map1.column_to_raw()         	# recover column to raw
	def combine(self):
		self.map1.combine()

	def generate_new(self):
		self.map1.table = self.map1.sorting_zero()
		print_and_sleep()
		self.map1.include_new_number()
		print_and_sleep()

def print_and_sleep():
	os.system('clear')
	print(a.map1.table[0])
	print(a.map1.table[1])
	print(a.map1.table[2])
	print(a.map1.table[3])
	print(a.map1.table[4])
	print('\n\n')
	time.sleep(10)


a = Anipang()

while True:
	a.master_pang()


# print("========tmp_raw=====================================\n")
# print(a.map1.tmp_raw[0])
# print(a.map1.tmp_raw[1])
# print(a.map1.tmp_raw[2])
# print(a.map1.tmp_raw[3])
# print(a.map1.tmp_raw[4])
# print("=====================================================\n")

# print("========tmp_column=====================================\n")
# print(a.map1.tmp_column[0])
# print(a.map1.tmp_column[1])
# print(a.map1.tmp_column[2])
# print(a.map1.tmp_column[3])
# print(a.map1.tmp_column[4])
# print("=====================================================\n")

# print("========table=====================================\n")
# print(a.map1.table[0])
# print(a.map1.table[1])
# print(a.map1.table[2])
# print(a.map1.table[3])
# print(a.map1.table[4])
# print("=====================================================\n")
#print(a.map1.tmp_raw)
#print(a.map1.tmp_column)
