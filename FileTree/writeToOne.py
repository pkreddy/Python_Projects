import os

def list_files(startpath: str) -> list:
    count = 0
    file_list = []
    for root, dirs, files in os.walk(startpath):
        # print(root, dirs, files)
        if len(dirs) != 0:
            for f in files:
                # print(root + '\\' + f)
                file_list.append(root + '\\' + f)
            count += len(files)
        
        if len(dirs) == 0:
            for f in files:
                # print(root + '\\' + f)
                file_list.append(root + '\\' + f)
            count += len(files)

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        # print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        # for f in files:
        #     print('{}{}'.format(subindent, f))
        #     count += 1
    # print(count)
    return file_list

source = ""
fs = list_files(source)

destination = ""

for f in fs:
    rfile = open(f, "r")
    afile = open(destination)

    content = rfile.readlines()
    afile.write("****|||***START****|||***\n")
    afile.write(f+"\n")
    afile.writelines(content)
    afile.write("\n****|||***END****|||***\n")

    rfile.close()
    afile.close()