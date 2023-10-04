f = open('file_one.txt', 'w+')
f.write('file one content')
f.close()

f = open('file_two.txt', 'w+')
f.write('file two content')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extract_content')
