# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Bad file extension:', fname)
    quit()
for lines in fh:
    lines=lines.rstrip()
    print(lines.upper())
