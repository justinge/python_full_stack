file=open("test.md")
while True:
    text=file.readline()
    if not text:
        break
    print(text)
file.close()