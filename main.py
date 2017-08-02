

import glob
import os
from DocumentSegmentation.Data import data_loader as DoCSegDataLoader
from DocumentSegmentation.Data import pre_processing as DoCSegPreProcessing

from DocumentClassification import predict
from DocumentSegmentation.DocSegmentation import DocSeg
import pandas as pd


class App():
    def __init__(self,param,dir):#,gt_dir):
        self.param = param
        self.dir = dir
        # self.gt_dir = gt_dir
        self.dataset = DoCSegDataLoader.load_dataset(dir)
        # self.gt_dataset, self.gt_inform_list = data_loader.load_target_data(gt_dir)
        self.doc_segment = DocSeg(seg_param=None)
        # self.doc_predict = predict.DocumentClassification()

    def run(self):
        for im in self.dataset:
            seg_groups = self.doc_segment.run(im)   #seg_groups: 분할된 그룹정보들 im_patchs: 분류할 이미지들
            # cls_groups = self.doc_predict.run(im_patchs) #seg_groups: 분류된 이미지 정보
            # seg_mean_iou = eval.block_eval(seg_groups, self.gt_inform_list)
            # cls_mean_iou = eval.block_eval(cls_groups, self.gt_inform_list)
            return seg_groups#, [seg_mean_iou,cls_mean_iou]

def demo_case(dir):
    seg_group = App(param=None,dir=dir).run()
    return "결과이미지", "정확도"
def demo():
    print("데모 시작")
    #csv 형태로 입력
    # from optparse import OptionParser
    # parser = OptionParser()
    # parser.add_option("-c", "--csv", action="store_true", dest="data/dataset.csv", default=True, help="dataset")
    # (options, args) = parser.parse_args()
    # print(options)
    # dir_list = pd.read_csv(args.csv)
    dir_list = ["./DocumentSegmentation/Data/Basic","./DocumentSegmentation/Data/Intermediate", "./DocumentSegmentation/Data/Advanced"]
    #문제 testcase 별 데모
    for dir in dir_list:
        result_im , precision = demo_case(dir)
        # result_im.show()
        # os.wait()
        # precision.view()
    print("데모 종료")
if __name__ =="__main__":
    demo()