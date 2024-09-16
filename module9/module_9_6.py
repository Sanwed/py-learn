def all_variants(text):
    count = 1
    while count <= len(text):
        for j in range(len(text) - count + 1):
            yield text[j:j + count]
        count += 1


a = all_variants("abcd")
for i in a:
    print(i)
