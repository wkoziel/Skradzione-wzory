from PIL import Image, ImageChops
import imagehash, os
#pip install Pillow

def Check(path1, path2):
    img1 = Image.open("images/"+path1)
    img2 = Image.open("images/"+path2)

    hash0 = imagehash.average_hash(img1)
    hash1 = imagehash.average_hash(img2)

    cutoff = 10
    diff = hash0 - hash1
    if diff < cutoff:
        print(path1+" i "+path2+" są podobne")

names = os.listdir('images')

for i in names:
    for j in names:
        Check(i, j)

