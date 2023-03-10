import pytesseract
import os


custom_config = r'--oem 3 --psm 6'

directory = 'images'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    text = pytesseract.image_to_string(f, config=custom_config)

    print("text: ", text)

    file = open("results.txt", "a")

    file.write(text)
    file.write("\n")

