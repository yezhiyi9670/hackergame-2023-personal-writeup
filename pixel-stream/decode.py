import os
from PIL import Image

output_path = 'video_stream_restore/output/'

if not os.path.exists(output_path):
    os.mkdir(output_path)

fp = open('./video_stream_restore/video.bin', 'rb')

# 45048896 = 2^6 * 409 * 1721

frameWidth = 427
frameHeight = 759
depth = 3

t = 0
def dump_image_1():
    global t
    t += 1
    # fp.seek(0, 0)
    stream = fp.read(frameWidth * frameHeight * depth)
    img = Image.frombytes('RGB', ( frameWidth, frameHeight ), stream)
    img.save(output_path + 'frame-' + str(t) + '.png')

while True:
    dump_image_1()
