import math
import numpy as np
import math
import wave
from PIL import Image

def individualPixelsSummedNormally(pixelVals, duration, framerate, filepath):

    finalarr = np.zeros(duration*framerate)
    for frame in range(0, duration*framerate):
            totamplitude = 0
            currtime = frame/framerate
            for pixel in range(0, len(pixelVals)):
                relfreq = ((pixelVals[pixel]/255)*14000)+1000
                totamplitude += math.sin(2*math.pi*relfreq*currtime)+1
            val = int(((totamplitude)/(len(pixelVals)))*255/2)
            finalarr[frame] = val

    with wave.open(filepath, mode="wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(1)
        #with 2 it was 4 seconds long, 8kb
        #with 1 it was 8 seconds long, 8kb
        wav.setframerate(framerate)
        for i in finalarr:
             wav.writeframes(int(i).to_bytes(1, 'big'))            

def convertImageToArray(filepath):
    im = Image.open(filepath)
    ims = im.load()
    x, y = im.size

    img = np.array([0 for i in range(0, (x-1)*(y-1))])
    
    for i in range(0, y-1):
        for j in range(0, x-1):
            sum = ims[j, i][0] + ims[j, i][1] + ims[j, i][2]
            img[j+(i*(x-1))] = sum/3
    return img

print(int(255).to_bytes(1, 'big'))
arrs = convertImageToArray("milt.jpg")
individualPixelsSummedNormally(arrs, 1, 1000, "milt.wav")


