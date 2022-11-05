import os

source = ""
content = []

# open the source file and read entirely
with open(source, 'r') as f_in:
    content = f_in.read()

content_clean = content.replace("****|||***END****|||***\n",'')
content_clean = content_clean.split("****|||***START****|||***\n")

for clean_data in content_clean[1:]:
    content_list = clean_data.split('\n')
    destination = content_list[0]
    # final_content_list = content_list[1:]
    final_content_list = clean_data.replace(destination, '')
    
    destination_list = destination.split("\\")
    destination_file_name = destination_list.pop()
    destination_dir = '\\'.join(destination_list)

    # print(final_content_list)

    try:
        os.makedirs(destination_dir)
    except:
        pass

    with open(destination, 'a+', encoding = 'utf-8') as f_out:
        f_out.write(final_content_list)