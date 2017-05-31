from Myro import *
init("COM3")

foto = 0
while foto < 10:
    speak("Waleeeeeeeeeeeeeeee")
    wait(1)
    speak("tomando foto")
    setPictureSize("large")
    img = takePicture("jpeg")
    show(img)
    turnRight(1, 2)
    foto += 1