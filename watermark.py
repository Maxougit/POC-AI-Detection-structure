import cv2
from imwatermark import WatermarkEncoder
from imwatermark import WatermarkDecoder

def watermark_image(name):
    bgr = cv2.imread('Red bike in the forest.png')
    wm = 'abcd'

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', wm.encode('utf-8'))
    bgr_encoded = encoder.encode(bgr, 'dwtDctSvd')

    cv2.imwrite(name, bgr_encoded)


def watermark_decoder(name):
    bgr = cv2.imread(name)

    decoder = WatermarkDecoder('bytes', 32)
    watermark = decoder.decode(bgr, 'dwtDctSvd')
    # print(watermark.decode('utf-8', errors='ignore'))
    return watermark.decode('utf-8', errors='ignore')
