import os
import sys

def sort_files_by_extension(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    sorted_files = sorted(files, key=lambda x: (x.split('.')[-1], x))
    return sorted_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python files_sort.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)

    sorted_files = sort_files_by_extension(directory)
    for file in sorted_files:
        print(file)
