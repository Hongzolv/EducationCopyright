
from Data import data_loader as dl
from Data import pre_processing as pp

from DocumentClassification import predict
from Evaluation import eval

class DocSeg():
    def __init__(self,dir, param):
        self.dir = dir
        self.param = param

    # block segmentation 알고리즘
    def block_seg(self, dataset):
        # x-y cut algorithm
        # margin 제거
        return

    def block_group(self, blocks):
        return

    def run(self):

        #data load
        dataset = dl.data_load(self.dir)
        gt_dataset = dl.data_load(self.dir)

        #data preprocessing
        dataset = pp.pre_precessing(dataset)

        #block segmengation
        blocks = block_seg(dataset)

        #block group
        seg_groups,images = block_group(blocks)
        #loyout block group 성능 평가
        seg_mean_iou = eval.block_eval(seg_groups, gt_dataset.group)
        print(seg_mean_iou)

        #group classification 성능 평가
        cls_groups = predict.classify(images)
        seg_mean_iou = eval.block_eval(cls_groups, gt_dataset.group)
        print(seg_mean_iou)

        return



    