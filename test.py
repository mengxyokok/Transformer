with open('data/english.txt', 'r', encoding='utf-8') as file:
    content = file.read().strip().split('\n')
print(content)