import os
import shutil
import mycolors

tool_namekey = bright_yellow("pyautokit-02")

# validate an input path if existing folder
def validate_path(path):
	if not os.path.exists(path):
		print(f"[{tool_namekey}] ERROR: not a valid path")
		exit()
	if not os.path.isdir(path):
		print(f"[{tool_namekey}] ERROR: not a valid folder")
		exit()

# list and filters file
def get_files(directory):
	files_and_dirs = os.listdir(directory)
	files = [file for file in files_and_dirs if os.path.isfile(file)]
	return files

# get the file extensions without "."
def get_extension(file):
	extension = os.path.splitext(file)[1]
	return extension[1:].upper() if extension else "OTHERS"

# move the file to its respective extension
def move_file(file, folder):
	shutil.move(file, os.path.join(folder, file))
	print(f"moved to {folder}: {file}")

# check if a folder exists already
def is_exists(folder):
	exists = os.path.exists(folder)
	return exists

# create a folder
def create_folder(foldername):
	os.makedirs(foldername, exist_ok=True)
	print(f"folder {foldername} created")

# get the current file name
def get_working_file():
	current_file = os.path.abspath(__file__)
	return current_file

# main function to run
def main():
	path_to_filter = input(f"[{tool_namekey}] Input path to folder to sort ~: ")
	validate_path(path_to_filter)

	files = get_files(path_to_filter)
	working_file =  get_working_file()

	for file in files:
		if os.path.abspath(file) != working_file:
			extension = get_extension(file)

			if not is_exists(extension):
				create_folder(extension)

			move_file(file, extension)

	print(f"[{tool_namekey}] process done!")

# run when called
if __name__ == "__main__":
	main()