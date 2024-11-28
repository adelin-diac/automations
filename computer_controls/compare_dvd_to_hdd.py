import os

def list_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the relative path of the file with respect to the root directory
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            file_list.append(relative_path)
    return file_list

def find_missing_files(source_dir, target_dir):
    source_files = list_files_in_directory(source_dir)
    target_files = list_files_in_directory(target_dir)

    # Use a set for quick lookup of files in the target directory
    target_files_set = set(target_files)

    # Find files that are in the source but not in the target
    missing_files = [file for file in source_files if file not in target_files_set]
    return missing_files

# Specify the directories
cd_directory = r"D:/"          # Replace with the path to your CD directory
hard_drive_directory = r"F:/HDD-1 Backup [25-04-2024]/Toate Poze/Poze Botez"  # Replace with the path to your hard drive directory

# Find the missing files
missing_files = find_missing_files(cd_directory, hard_drive_directory)

# Output the missing files
if missing_files:
    print("Files missing from the hard drive:")
    for file in missing_files:
        print(file)
else:
    print("No files are missing from the hard drive.")
