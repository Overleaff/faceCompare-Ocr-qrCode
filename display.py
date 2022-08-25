import cv2

def displayBbox(im, bbox):
    if bbox is not None:
    #    n = len(bbox[0][0])
        pt1 = (int(bbox[0][0][0]),int(bbox[0][0][1]))
        pt2 = (int(bbox[0][2][0]),int(bbox[0][2][1]))
        color = (0,0,255)
        im = cv2.rectangle(im, pt1, pt2, color, 3)
        print(im)
    return im