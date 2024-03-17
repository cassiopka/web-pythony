import os
import sys

def find_file(filename, start_dir=None):
    if start_dir is None:
        start_dir = os.path.abspath(os.curdir)

    for root, _, files in os.walk(start_dir):
        if filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.readlines()
                print("\n".join(lines[:5]))
            return True

    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_search.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if not find_file(filename):
        print(f"Файл {filename} не найден")
