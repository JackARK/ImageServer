import os

from PIL import Image


def compress_image(input_path, output_path, quality):
    image = Image.open(input_path)
    image.save(output_path, optimize=True, quality=quality)


def get_file_size(file_path):
    if not os.path.isfile(file_path):
        return 0
    file_size = os.path.getsize(file_path)
    return file_size


# 示例用法
input_path = 'input.jpg'
output_path = 'output.jpg'
quality = 90
file_names = []
for file_name in os.listdir("./images"):
    if os.path.isfile(os.path.join("./images", file_name)):
        file_names.append(file_name)
for file_name in file_names:
    input_path = "./images/" + file_name
    output_path = "./zipped/" + file_name
    size = get_file_size(input_path)
    if 2097152 < size:
        quality = int(2097152 / size * 100)
    else:
        quality = 100
    compress_image(input_path, output_path, quality)
    print("A image has been zipped: " + file_name + " as size: " + str(size) + " from " + os.path.getsize(
        "./zipped/" + file_name).__str__())
    if os.path.getsize("./zipped/" + file_name) > 2097152:
        # os.remove("./zipped/" + file_name)
        # print("It is too big,deleted: " + file_name)
        os.rename("./images/"+file_name,"./sobig/"+file_name)
        print("So fucking big,move to ./sobig folder" + file_name)