import os
for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("Files:")
        for filenme in files:
            print(filenme)

for root, dires, files in os.walk("../ppnp-2-10-Przemek"):
    for file in files:
        if file == 'api_get_xml.py':
            file_path = os.path.join(root, file)
            print(file_path)

