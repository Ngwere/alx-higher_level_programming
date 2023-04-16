#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
	"""search and update

	Args:
		filename (str) - filename
		search_string (str) - the search string
		new_string (str) - new string
	"""
	read = []
	with open(filename, "r", encoding="utf-8") as f:
		read = f.readlines()
		index = 0

		while index < len(read):
			if search_string in read[index]:
				read[index:index + 1] = [read[index], new_string]
				index += 1
			index += 1

	with open(filename, "w", encoding="utf-8") as file:
		file.writelines(read)
