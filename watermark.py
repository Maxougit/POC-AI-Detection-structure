import cv2
from imwatermark import WatermarkEncoder
from imwatermark import WatermarkDecoder

def watermark_image():
    bgr = cv2.imread('Red bike in the forest.png')
    wm = 'abcd'

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', wm.encode('utf-8'))
    bgr_encoded = encoder.encode(bgr, 'dwtDctSvd')

    cv2.imwrite('test_wm.png', bgr_encoded)


def watermark_decoder():
    bgr = cv2.imread('test_wm.png')

    decoder = WatermarkDecoder('bytes', 32)
    watermark = decoder.decode(bgr, 'dwtDctSvd')
    print(watermark.decode('utf-8', errors='ignore'))

watermark_image()
watermark_decoder()
