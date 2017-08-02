import numpy as np
import pandas as pd
import cv2
import os
import json
#타겟 이미지 레이블링 파싱
attritubes = ["#filename", "file_size", "file_attributes", "region_count", "region_id", "region_shape_attributes",
              "region_attributes"]
scan_size = [840, 1188]  # width , height
path = "data/via_region_data.csv"

def make_seg_data(path):
    csv_data = pd.read_csv(path)
    im_list = []
    gt_im_list = []
    for i in range(len(csv_data)):

        dir_path = os.path.dirname(path)
        im_path = csv_data.ix[i][attritubes[0]]
        im = cv2.imread(os.path.join(dir_path, im_path))
        gt_path = os.path.join(dir_path, (os.path.basename(im_path).split('.')[0] + '_gt.png'))
        width_ratio = scan_size[0] / float(im.shape[1])
        height_ratio = scan_size[1] / float(im.shape[0])
        # image 영상크기 조절
        resized_im = cv2.resize(im, dsize=(scan_size[0], scan_size[1]))

        # 기존에 있는 ground-truth 영상 읽기
        if os.path.exists(gt_path):
            gt_im = cv2.imread(gt_path, 0)
        else:
            gt_im = np.zeros((scan_size[1], scan_size[0], 1), np.uint8)
            im_list.append(resized_im)
            gt_im_list.append(gt_im)


        region_shape_data = csv_data.ix[i][attritubes[5]]
        shape_json = json.loads(region_shape_data)

        pt1 = (int(float(shape_json['x']) * width_ratio), int(float(shape_json['y']) * height_ratio))
        pt2 = (int((float(shape_json['x']) + float(shape_json['width'])) * width_ratio),
               int((float(shape_json['y']) + float(shape_json['height'])) * height_ratio))

        region_data = csv_data.ix[i][attritubes[6]]
        region_json = json.loads(region_data)
        if 'figure' == region_json['name']:
            color = 255
        else:
            color = 128
        cv2.rectangle(gt_im, pt1, pt2, color, -1)
        cv2.imwrite(gt_path, gt_im)
    return csv_data,im_list,gt_im_list

import unittest
class TestMakeData(unittest.TestCase):
    def test_make_seg_data(self):
        path = "data/via_region_data.csv"
        _, im_list, gt_im_list = make_seg_data(path)
        self.assertEqual(len(im_list),len(gt_im_list))
        for i in range(len(im_list)):
            self.assertEqual(im_list[i].shape,gt_im_list[i].shape)
if __name__ == '__main__':
    unittest.main()

