

"""!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install Pillow==9.0.0"""


from google.colab import files

uploaded = files.upload()

import pytesseract
from PIL import Image
extractedInformation = pytesseract.image_to_string(Image.open('/content/test2.png'))

print(extractedInformation)
     