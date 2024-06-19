
def write_file(file_name, file_content):
    
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as newfile:
        newfile.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as newfile:
        newfile.write(append_content)

def read_file(file_name):
    # textfile = open(f'{file_name}.txt', encoding='utf-8')
    # print(textfile.read())
    with open(f'{file_name}.txt', encoding='utf-8') as textfile:
        for line in textfile:
            print(line)
            return line
