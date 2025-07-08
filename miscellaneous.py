from PIL import Image

img = Image.open("images/model2.PNG")
width, height = img.size

print(f"Width: {width}px, Height: {height}px")


#python miscellaneous.py