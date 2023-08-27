import os

files = []
for file in os.listdir("./zipped"):
    files.append(file)

for file in files:
    file_path = "./zipped/" + file
    if os.path.getsize(file_path) > 2097152:
        print("File is too big:", file_path)
        try:
            # os.remove(file_path)
            new_path = "./sobig/" + file
            os.rename(file_path, new_path)
            print("Moved to:", new_path)
        except OSError as e:
            print("Error moving file:", str(e))
    else:
        print("File is within size limit, skipping:", file_path)
