import os
import shutil
from myfunctions import progress_bar
from mycolors import *

tool_namekey = bright_yellow("pyautokit-02")

# delete an empty folder
def delete_empty_folders(path):
	deleted_folders = 0
	all_dirs = [root for root, dirs, files in os.walk(path, topdown=False)]  # collect dirs first

	for root in progress_bar(all_dirs, prefix=f"[{tool_namekey}] scanning: ", size=40):
		if not os.listdir(root):  # folder is empty
			try:
				os.rmdir(root)
				deleted_folders += 1
			except Exception as e:
				print(f"\n[{tool_namekey}] could not delete {root}: {e}")

	return deleted_folders

# validate an input path if existing folder
def validate_path(path):
	if not os.path.exists(path):
		print(f"[{tool_namekey}] ERROR: not a valid path")
		exit()
	if not os.path.isdir(path):
		print(f"[{tool_namekey}] ERROR: not a valid folder")
		exit()

# main function to run
def main():
	target_folder = input(f"[{tool_namekey}] input target folder ~: ")
	validate_path(target_folder)   # added validation before scanning
	total_deleted_folders = delete_empty_folders(target_folder)

	if total_deleted_folders == 0:
		print(f"\n[{tool_namekey}] no empty folders found")

	print(f"\n[{tool_namekey}] successfully deleted {total_deleted_folders} empty folders")
	print(f"[{tool_namekey}] process done!")

if __name__ == '__main__':
	main()
