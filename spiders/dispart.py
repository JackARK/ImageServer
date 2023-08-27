from PIL import Image
import os


def disparate(folder_path, file_name):
    image_path = folder_path+file_name
    image = Image.open(image_path)
    width, height = image.size
    image.close()
    if width < height:
        # os.rename(folder_path+file_name, "./phone/" + file_name)
        os.remove(folder_path+file_name)
        print("It is a phone pic")
    else:
        print("This pic is for PC")


folder_path = "./zipped/"
file_names = []
for file_name in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, file_name)):
        file_names.append(file_name)
for file in file_names:
    disparate(folder_path, file)
