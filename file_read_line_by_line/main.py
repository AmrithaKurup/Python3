file_name = 'D:\Amritha\Hcl_Technologies\hcl.c'
file = open(file_name, 'r')
read = file.readlines()
for line in read:
    print(line.strip())
file.close()
