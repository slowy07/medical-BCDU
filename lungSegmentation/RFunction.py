from __future__ import division
import numpy as np
from scipy.ndimage.morphology import binary_erosion, binary_fill_holes

def hu_to_grayscale(volume):
    volume = np.clip(volume, -512, 512)
    mxmal = np.max(volume)
    mnval = np.min(volume)
    im_volume = (volume - mnval) / max(mxval - mnval, 1e-3)
    im_volume = im_volume
    
    return im_volume* 255

def get_mask_lung(vol):
    vol_im = np.where(vol > 0, 1, 0)
    shp = vol.shape
    around_img = np.zeros((shp[0], shp[1], shp[2]), dtype = np.float32)
    for idx in range(shp[0]):
        around_lung[idx, :, :] = binary_erosion(vol_im[idx], structure = np.ones((15, 15))).astype(vol_im.dtype)

    return around_lung

def get_mask(segmentation):
    # initialize ouput to zero
    shp = segmentation.shape
    lung = np.zeros((shp[0], shp[1], shp[2]), dtype = np.float32)

    lung[np.equal(segmentation, 255)] = 255
    
    return lung