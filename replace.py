# Program to replace bullet points with tabs in a text file

fin = open("accounts.txt", "r", encoding="utf8")
fout = open("accounts-file.txt", "w+", encoding="utf-8")

# To be replaced
key = "*"

# To replace by
new = "\t"

for line in fin:
    line = line.replace(key, new)

fin.close()
fout.flush()
fout.close()
