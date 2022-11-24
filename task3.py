import os

file_dict = {}
fin_file = 'result.txt'
for file in os.listdir():
    if ".txt" in file and fin_file not in file:
        file_dict[file] = len(open(file, 'r', encoding='utf-8').readlines())

sort_file = [(string_count, file_dict[string_count]) for string_count in
             sorted(file_dict, key=file_dict.get, reverse=False)]
print(sort_file)

with open(fin_file, 'w') as fw:
    for file, string_count in sort_file:
        with open(file, 'r', encoding='utf-8') as fr:
            fw.write('\n' + file + '\n')
            fw.write(str(string_count) + '\n')
            for strings in fr.readlines():
                fw.write(strings)