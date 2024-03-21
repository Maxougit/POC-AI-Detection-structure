import cv2
import time
from imwatermark import WatermarkEncoder
from imwatermark import WatermarkDecoder

def watermark_image(name):
    bgr = cv2.imread(name)
    wm = 'abcd'

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', wm.encode('utf-8'))

    start_time = time.time()
    bgr_encoded = encoder.encode(bgr, 'dwtDctSvd')
    end_time = time.time()

    cv2.imwrite(name, bgr_encoded)

    processing_time = end_time - start_time
    print(f"Temps d'encodage : {processing_time} secondes")


def watermark_decoder(name):
    bgr = cv2.imread(name)

    decoder = WatermarkDecoder('bytes', 32)

    start_time = time.time()
    watermark = decoder.decode(bgr, 'dwtDctSvd')
    end_time = time.time()

    decoding_time = end_time - start_time
    print(f"Temps de décodage : {decoding_time} secondes")

    return watermark.decode('utf-8', errors='ignore')

# watermark_image("Red bike in the forest.png")
# print(watermark_decoder("Red bike in the forest.png"))