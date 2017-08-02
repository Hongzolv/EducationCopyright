

def block_eval(est_blocks, gt_blocks):
    mean_iou = 0.0
    for i in range(len(gt_blocks)):
        size_est_block= (est_blocks[i].x2 - est_blocks[i].x1) *  (est_blocks[i].y2 - est_blocks[i].y1)
        size_gt_block = (gt_blocks[i].x2 - gt_blocks[i].x1) * (gt_blocks[i].y2 - gt_blocks[i].y1)

        inter = (min(est_blocks[i].x2,gt_blocks[i].x2 ) - max(est_blocks[i].x1,gt_blocks[i].x1)) * (min(est_blocks[i].y2,gt_blocks[i].y2 ) - max(est_blocks[i].y1,gt_blocks[i].y1))
        union = size_est_block + size_gt_block - inter

        iou = inter / union
        mean_iou +=iou

    mean_iou /= len(gt_blocks)
    return mean_iou

