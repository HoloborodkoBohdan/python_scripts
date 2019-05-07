import os
import tempfile

from pdf2image import convert_from_path

folder = 'pdf' #folder with pdfs. You need to create it manually.
save_dir = 'saved' #folder dor images. You need to create it manually.

log = open("log.txt", "a")

for r, d, f in os.walk(folder):
    for filename in f:
        print(f'./{folder}/{filename}')
        log.write(filename + "\n")

        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(f'./{folder}/{filename}', dpi=200, output_folder=path)

        base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'

        for page in images_from_path:
            index = images_from_path.index(page)
            name = f'{base_filename}_{index}.jpg'
            print(name)

            page.save(os.path.join(save_dir, name), 'JPEG')

log.close()

# Script Info

# Break pdf into JPG pictures. Images log would be saved in log.txt. 
# Python 3
# pip install pdf2image (library: https://github.com/Belval/pdf2image)
