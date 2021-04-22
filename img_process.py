import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse

from utils import Preprocess

pre = Preprocess()
img = cv2.cvtColor(cv2.imread("img_test.jpg"), cv2.COLOR_BGR2RGB)
# face alignment and segmentation
face_rgba = pre.process(img)
cv2.imwrite("result111"+ '.png',cv2.cvtColor(face_rgba, cv2.COLOR_RGB2BGR))
if face_rgba is not None:
    # change background to white
    face = face_rgba[:, :, :3].copy()
    mask = face_rgba[:, :, 3].copy()[:, :, np.newaxis] / 255.
    face_white_bg = (face * mask + (1 - mask) * 255).astype(np.uint8)

    cv2.imwrite("result"+ '.png',cv2.cvtColor(face_white_bg, cv2.COLOR_RGB2BGR))