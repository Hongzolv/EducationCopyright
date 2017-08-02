import os
import glob
import numpy as np
def load_dataset(dir):
    dataset = []
    for im_path in glob.iglob(os.path.join(dir,'*.png')):
        dataset.append(imread(im_path))
    return dataset
def load_target_data(dir):
    dataset = []
    gt_inform_list = []
    for im_path in glob.iglob(os.path.join(dir,'*.png')):
        gt_inform_list.append(str(os.path.basename(im_path)[-4]) + '.txt')
        dataset.append(imread(im_path))
    return dataset, gt_inform_list

#library tool 사용
def imread(path):
    return np.random.randint(0,255,(100,200))
