import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='rus')
    with open('out.txt', "a") as f:
        f.write(text)
        f.close()
        print(f'wrote text from {image_path} to {f.name}')

def get_image_list():
    x = input('write names of the images (without .jpg), x to exit: ')
    out = []
    while x != 'x':
        out.append(x)
        x = input()
    return out

if __name__ == '__main__':
    ...
    images = get_image_list()
    print(f'your images are: {','.join(images)}.')
    for image in images:
        recognize_text_from_image(f'{image}.jpg')
        
    