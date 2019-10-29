from PIL import Image, ImageFilter

img = Image.open('./Pokemons/charmelon.png')
filtered_Img = img.filter(ImageFilter.BLUR)

#print(img)
filtered_Img.save("./Pokemons/blur.png", 'png')