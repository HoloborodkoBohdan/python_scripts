import os
import tempfile

from pdf2image import convert_from_path

folder = 'pdf'
save_dir = 'saved'

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
