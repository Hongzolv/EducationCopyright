
from Data import data_loader as dl
from Data import pre_processing as pp

class DocSeg():
    def __init__(self,dir, param):
        self.dir = dir
        self.param = param

    # block segmentation 알고리즘
    def block_seg(self, dataset):
        self.param
        # x-y cut algorithm
        # margin 제거
        return

    def block_group(self, blocks):
        return

    def run(self):

        #data load
        dataset = dl.data_load(self.dir)

        #data preprocessing
        dataset = pp.pre_precessing(dataset)

        #block segmengation
        blocks = block_seg(dataset)

        #block group
        groups = block_group(blocks)


        return



    