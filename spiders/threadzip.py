import os
from concurrent.futures import ThreadPoolExecutor

from PIL import Image


def compress_image(input_path, output_path, quality):
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)


def get_file_size(file_path):
    if not os.path.isfile(file_path):
        return 0
    file_size = os.path.getsize(file_path)
    return file_size


def process_image(file_name):
    input_path = "./images/" + file_name
    output_path = "./zipped/" + file_name
    size = get_file_size(input_path)
    if 2097152 < size:
        quality = int(2097152 / size * 100)
    else:
        quality = 100
    compress_image(input_path, output_path, quality)
    print("A image has been zipped: " + file_name + " as size from " + os.path.getsize(
        "./zipped/" + file_name).__str__()) + "to" + str(size)
    if os.path.getsize("./zipped/" + file_name) > 2097152:
        os.rename("./images/" + file_name, "./sobig/" + file_name)
        os.remove("./images/" + file_name)
        print("So fucking big,move to ./sobig folder" + file_name)


# 示例用法
file_names = []
for file_name in os.listdir("./images"):
    if os.path.isfile(os.path.join("./images", file_name)):
        file_names.append(file_name)

with ThreadPoolExecutor(max_workers=16) as executor:
    executor.map(process_image, file_names)
