import os
import shutil
import sys


def scan_and_copy(source_dir, destination_dir):
    # Check if the destination directory exists, create it if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Scan files and folders inside the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        dest_path = os.path.join(destination_dir, item)

        # Check if it's a file
        if os.path.isfile(item_path):
            # Check if the file already exists in the destination directory, skip if it exists
            if not os.path.exists(dest_path):
                shutil.copy2(item_path, dest_path)
                print(f"Copied file: {item}")
            else:
                print(f"Skip: {item} already exists")

        # Check if it's a directory
        elif os.path.isdir(item_path):
            # Check if the directory already exists in the destination directory, skip if it exists
            if not os.path.exists(dest_path):
                print(f"Copied folder: {item}")
            else:
                print(f"Skip: {item} already existsg")
            scan_and_copy(item_path, dest_path)

def copy(new_dir):
    # Check if directory "a" exists, create it if it doesn't exist
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # Scan and copy files and folders inside the "example" directory to directory "a"
    scan_and_copy("example", new_dir)

# Get the input directory "new_dir"
if len(sys.argv) >= 2:
    new_dirs = sys.argv[1:]
elif len(sys.argv) == 1:
    new_dirs = [input("Please enter the path of directory which want to create: ")]
else:
    raise Exception("Error: Please enter only one argument.")

for new_dir in new_dirs:
    if not new_dir:
        raise Exception("Error: Please enter a valid directory path.")
    print("-"*20+f"{new_dir}"+'-'*20)
    copy(new_dir)


print("Completed!")
