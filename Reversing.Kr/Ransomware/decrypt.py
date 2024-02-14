byteFile = bytearray(open("./file", "rb").read())
for i in range(len(byteFile)):
    byteFile[i] ^= 0xFF

open("file_new", "wb").write(byteFile)