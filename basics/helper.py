import os# os name library which helps to read the file.

def read(file):
    if os.path.exists(file):
        with open(file,errors="ignore") as f:
            return f.read()
    return "file not found"        