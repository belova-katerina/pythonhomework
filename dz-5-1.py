f = open('file_task1.txt', 'w', encoding='utf-8')
line = input('Enter the text:\n')
while line:
    f.writelines(line)
    line = input('Enter the text:\n')
    if not line:
        break
f.close()

f = open('file_task1.txt', 'r', encoding='utf-8')
for content in f:
    print(f'You entered: {content}\n')
f.close()


