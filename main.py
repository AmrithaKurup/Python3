import shutil
import re
import os

shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip')
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)


def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


results = []
for folder, sub_folders, files in os.walk(os.getcwd() + "\\extracted_content"):

    for f in files:
        full_path = folder + '\\' + f

        results.append(search(full_path))
for r in results:
    if r != '':
        print(f'The number {r.group()} is present in the location {full_path}')
