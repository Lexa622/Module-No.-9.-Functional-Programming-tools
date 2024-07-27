def all_variants(text):
    b = ''
    for j in range(1, len(text) + 1):
        for k in range(0, len(text) - (j - 1)):
            b += text[k: k + j] + '\n'
    yield b


a = all_variants("abc")
for i in a:
    print(i)
