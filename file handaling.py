import csv
# from csv import reader, writer

# read method 

# file=open('filepy.txt','r')
# # file.seek()
# print(f"start postion {file.tell()}")
# print(file.read())
# print(f"end postion {file.tell()}")
# print(file.seek(0))
# print(file.read(0))
# # print(file.readlines())
# print(file.readline())
# print(file.readline())
# print(file.readline())



# print(file.tail())

# write method
# file=open('filecreate1.txt','w')
# print(file.write('this is new file created by the help of file handaling' ))

# file.close()
file1=open("filetry.csv")

csvfile_read=csv.reader(file1,delimiter=',')
for i in csvfile_read:
    for j in i:
        print(j,end=" ")
    print()    





