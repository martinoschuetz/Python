import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from PIL import Image
from skimage.io import imread
import matplotlib.pyplot as plt
from multiprocessing import Pool
from skimage.util.montage import montage2d as montage
montage_rgb = lambda x: np.stack([montage(x[:, :, :, i]) for i in range(x.shape[3])], -1)
import gc; gc.enable()

try:
    os.mkdir('/home/sasdemo01/airbus_ship_detection/masks/')
except:
    None
masks = pd.read_csv('/home/sasdemo01/airbus_ship_detection/train_ship_segmentations_v2.csv')
images_with_masks = masks.dropna().groupby('ImageId').agg('count').reset_index()['ImageId']
images_without_masks = masks[masks['EncodedPixels'].isnull()].groupby('ImageId').agg('count').reset_index()['ImageId']

from skimage.morphology import label
def multi_rle_encode(img):
    labels = label(img[:, :, 0])
    return [rle_encode(labels==k) for k in np.unique(labels[labels>0])]

# ref: https://www.kaggle.com/paulorzp/run-length-encode-and-decode
def rle_encode(img):
    '''
    img: numpy array, 1 - mask, 0 - background
    Returns run length as string formated
    '''
    pixels = img.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return ' '.join(str(x) for x in runs)

def rle_decode(mask_rle, shape=(768, 768)):
    '''
    mask_rle: run-length as string formated (start length)
    shape: (height,width) of array to return 
    Returns numpy array, 1 - mask, 0 - background
    '''
    s = mask_rle.split()
    starts, lengths = [np.asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
    starts -= 1
    ends = starts + lengths
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    for lo, hi in zip(starts, ends):
        img[lo:hi] = 1
    return img.reshape(shape).T  # Needed to align to RLE direction

def masks_as_image(in_mask_list):
    # Take the individual ship masks and create a single mask array for all ships
    all_masks = np.zeros((768, 768), dtype = np.int16)
    #if isinstance(in_mask_list, list):
    for mask in in_mask_list:
        if isinstance(mask, str):
            all_masks += rle_decode(mask)
    return np.expand_dims(all_masks, -1)
def save_masks(file):
    rle_0 = masks.query('ImageId==' + '"' + file + '"')['EncodedPixels']
    img_0 = masks_as_image(rle_0)
    rle_1 = multi_rle_encode(img_0)
    img_1 = masks_as_image(rle_1)
    img = Image.fromarray(img_1.astype(np.uint8).reshape(768,768))
    img.save('/home/sasdemo01/airbus_ship_detection/masks/' + file, format='PNG')
    
empty_mask = Image.fromarray(np.zeros((768,768,1), dtype=np.uint8).reshape(768,768))
def save_empty_masks(file):
    empty_mask.save('/home/sasdemo01/airbus_ship_detection/masks/' + file, format='PNG')
    
p = Pool(processes=40)
p.map(save_masks, images_with_masks)
p.map(save_empty_masks, images_without_masks)