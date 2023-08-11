def read_last_10_lines(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        return lines[-10:]

file_name = "database\chat_log.txt"
last_10_lines = read_last_10_lines(file_name)
for line in last_10_lines:
    print(line,end="")