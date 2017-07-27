

def block_eval(est_block, gt_block):
    mean_iou = 0.0
    for i in range(len(gt_block)):
        size_est_block= (est_block[i].x2 - est_block[i].x1) *  (est_block[i].y2 - est_block[i].y1)
        size_gt_block = (gt_block[i].x2 - gt_block[i].x1) * (gt_block[i].y2 - gt_block[i].y1)

        inter = (min(est_block[i].x2,gt_block[i].x2 ) - max(est_block[i].x1,gt_block[i].x1)) * (min(est_block[i].y2,gt_block[i].y2 ) - max(est_block[i].y1,gt_block[i].y1))
        union = size_est_block + size_gt_block - inter

        iou = inter / union
        mean_iou +=iou

    mean_iou /= len(gt_block)
    return mean_iou

