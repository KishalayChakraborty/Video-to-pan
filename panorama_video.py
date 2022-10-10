import cv2 as cv
import numpy as np
# https://www.geeksforgeeks.org/opencv-panorama-stitching/
# https://pyimagesearch.com/2016/01/25/real-time-panorama-and-image-stitching-with-opencv/
modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)

# enter filename
filename = 'sample-cut.mp4'  # 'VID20221010173222.mp4'

# init VideoCapture
cp = cv.VideoCapture(filename)

n_frames = int(cp.get(cv.CAP_PROP_FRAME_COUNT))
print("Number of frames in the input video: {}".format(n_frames))

# get properties of the video for output video
width = int(cp.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cp.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cp.get(cv.CAP_PROP_FPS)

# uncomment to print frames per seconds
print("FPS: {}".format(fps))

# read first frame
success, prev = cp.read()

# initialize ORB image descriptor
orb = cv.ORB_create()

count = 0
index = 0

stitcher = cv.Stitcher.create(cv.Stitcher_PANORAMA)
imgCount = 0
imlist = []

while 1:
    print("Processing frame: {}".format(int(cp.get(cv.CAP_PROP_POS_FRAMES))))
    cp.set(cv.CAP_PROP_POS_FRAMES, count)
    succ, curr = cp.read()
    if succ == False:
        break

    imlist.append(curr)
    height, width, channels = curr.shape
    #print(height, width, channels, prev.shape)
    #status, pano = stitcher.stitch([prev, curr])
    '''
    if(status != cv.Stitcher_OK):
        imgCount += 1
        count += 1
        #cv.imwrite("images/ERR{}.png".format(str(imgCount).zfill(2)), prev)
        #cv.imwrite("images/ERR2{}.png".format(str(imgCount).zfill(2)), curr)
        prev = curr
        continue
    '''
    imgCount += 1
    #prev = pano
    count += 40


stitchy = cv.Stitcher.create()
(dummy, output) = stitchy.stitch(imlist)

if dummy != cv.STITCHER_OK:
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')

# final output
output = cv.resize(output, (0, 0), fx=0.4, fy=0.4)
cv.imshow('final result', output)

cv.waitKey(0)

#cv.imwrite("images/{}.png".format(str(imgCount).zfill(2)), pano)

cp.release()
