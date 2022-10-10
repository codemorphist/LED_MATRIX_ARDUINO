from PIL import Image

def convert(img):
    arr = ''
    i = img.load()
    for r in range(8):
        row = ''
        for c in range(8):
            if i[c,r] == 1: row+='0'
            else: row+='1'
        arr+=f'B{row},'
    print(arr)

img = Image.open('8bit_art.png')

x = int(input('Col: '))
y = int(input('Row: '))

p = 62
area = (p*x,p*y,p*x+32,p*y+32)
img = img.crop(area)
size = 8,8
img.thumbnail(size,Image.ANTIALIAS)
print('\n',img)
# img.save(f'hero_{x}_{y}.png')

convert(img)
