import fileOperations as fo

# Example usage
file_path = "D:\\Playwright_Python_Notes\\myfile.txt"

# Write to file
fo.write_to_file(file_path, "Welcome to Python \n File Handling")

# Append to file
fo.append_to_file(file_path, "\nThis line is appended.")

# Read file
print(fo.read_file(file_path, "all"))

# Rename file
fo.rename_file(file_path, "D:\\Playwright_Python_Notes\\myfile1.txt")

# Delete file
fo.delete_file("D:\\Playwright_Python_Notes\\myfile1.txt")

# Directory operations
dir_path = "D:\\Playwright_Python_Notes\\mydirectory"
fo.create_directory(dir_path)
print("Directory exists:", fo.check_directory_exists(dir_path))
fo.rename_directory(dir_path, "D:\\Playwright_Python_Notes\\mydirectory1")
fo.remove_directory("D:\\Playwright_Python_Notes\\mydirectory1", force=False)

# Current working directory
print("CWD:", fo.get_current_working_directory())
