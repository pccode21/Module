import pyscreenshot as ImageGrab
import os
os.chdir(r'.\Module\pyscreenshot')
if __name__ == '__main__':
    # im = ImageGrab.grab()  # grab fullscreen
    im = ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
    im.save('screenshot.png')  # save image file
    im.show()  # show image in a window
