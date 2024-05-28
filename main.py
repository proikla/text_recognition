import pytesseract
import os
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
    x = input('write names of the images (without .jpg), x to exit: \n')
    out = []
    while x != 'x':
        out.append(x)
        x = input()
    return out

def text_format():
    with open('out.txt', "r") as r:
        text = r.read()
    # Perform the replacement and assign the result back to the text variable
    text = text.replace('-\n', '')
    
    with open('out.txt', 'w') as w:
        w.write(text)



if __name__ == '__main__':
    ...
    images = get_image_list()
    print(f'your images are: {', '.join(images)}.')
    if os.path.exists('out.txt'):
        print(f'out.txt already exists. Deleting...')
        try:
            os.remove('out.txt')
        except Exception as e:
            print(f'An exception occured. Perhaps the file is open, try to close it.')
    for image in images:
        recognize_text_from_image(f'images/{image}.jpg')
    text_format()
        
    