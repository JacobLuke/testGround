#!/usr/bin/python

import urllib
import httplib
import random
from PIL import Image

mult4 = lambda n: int(math.ceil(n/4))*4
mult8 = lambda n: int(math.ceil(n/8))*8
lh = lambda n: struct.pack("<h", n)
li = lambda n: struct.pack("<i", n)

conn = httplib.HTTPSConnection('www.random.org')

def getRandNumbers(count):
    def getRandInner(num):
        params = urllib.urlencode({'min': 0, 'max': 255, 'format': 'plain', 'num': 1000, 'rnd': 'new', 'col': 1, 'base': 10})
        conn.request('GET', '/integers/?' + params)
        response = conn.getresponse().read()
        return [random.randrange(256) for i in range(count)]
    ret = []
    while count > 1000:
        ret.extend[getRandInner(1000)]
        count -= 1000
    if count:
        ret.extend(getRandInner(count))
    return ret

def getRandPixels(numPixels):
    randValues = getRandNumbers(numPixels * 3)
    return [tuple(randValues[3*i:3*i+3]) for i in range(numPixels)]

def getImage(width, height):
    img = Image.new( 'RGB', (width, height), "black")
    pixels = img.load()
    randPixels = [getRandPixels(width) for i in range(height)]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = randPixels[i][j]
    img.save('out.bmp')

if '__name__' == 'main':
    getImage(256, 256)
