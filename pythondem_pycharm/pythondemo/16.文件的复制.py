file_read=open("test.md")
file_write=open("test附件.md","w")

#读写

text=file_read.read()
file_write.write(text)

file_read.close()
file_write.close()