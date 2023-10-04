source_file = open('source.txt', 'r')
dest_file = open('dest.txt', 'w')

content = source_file.read()
dest_file.write(content)

source_file.close()
dest_file.close()
