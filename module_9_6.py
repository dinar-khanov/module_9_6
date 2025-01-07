def all_variants(text: str):
    length = len(text)
    for size in range(1, length + 1):
        for n in range(length - size + 1):
            yield text[n:n + size]

a = all_variants("abc")
for i in a:
    print(i)