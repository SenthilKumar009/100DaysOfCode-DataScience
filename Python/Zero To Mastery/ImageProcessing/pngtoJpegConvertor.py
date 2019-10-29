import sys, os
from PIL import Image

#grab first and second arguments
image_Folder = sys.argv[1]
output_folfer = sys.argv[2]

#check the new folder, else create a new one.
if not os.path.exists(output_folfer):
    os.makedirs(output_folfer)

#loop through pokemon
for filename in os.listdir(image_Folder):
    img = Image.open(f'{image_Folder}{filename}')
    cleanName = os.path.splitext(filename)
    print(cleanName)
    img.save(f'{output_folfer}{cleanName[0]}.png', 'png')
    print('All done!!!')
#convert into png to jpeg

#save them into new folder

