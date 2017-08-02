

import numpy as np
from DocumentClassification import predict
from Evaluation import eval

class Block():
    def __init__(self,label = 'text', bbox =(10,20,100,100), image= np.random.randint(0,255,(100-20,100-10))):
        #######from param#######
        #self.label = param.label
        self.label = label
        self.bbox = bbox
        self.image =  image

class DocSeg():
    def __init__(self, seg_param):
        self.seg_param = seg_param
    # block segmentation 알고리즘
    # 텍스트/ 비 텍스트 분할

    def block_segmentation(self, im):
        # x-y cut algorithm
        # margin 제거
        #임의의 10개 블록 생성
        blocks = []
        for i in range(10):
            blocks.append(Block())
        print("텍스트 / 비 텍스트 분할")
        return blocks
    # block grouping 알고리즘
    # 텍스트 / 캡션 분할

    def block_grouping(self, blocks):
        #-2개 block으로 그룹핑
        blocks = blocks[:-2]
        print("블록 그룹핑/ 텍스트 캡션 분할(OCR)/")
        return blocks
    def run(self,im = np.random.randint(0,255,(200,300))):
        print("도큐먼트 세그멘테이션 시작")
        # block segmengation
        blocks = self.block_segmentation(im)
        # block group
        block_group = self.block_grouping(blocks)
        print("도큐먼트 세그멘테이션 완료")
        return block_group



    