import random
import os
from torchvision.io import read_image

random.seed(1123)
with open('annotation.txt') as f:
    for line in f:
        fields = line.strip().split(',')
        img_name, bboxes = fields[1], fields[2:]
        img_name = img_name.split(':')[1]
        bboxes = [list(map(int, bb.split(':'))) for bb in bboxes]

        # get image size
        img = read_image(os.path.join('train/images', img_name))
        h, w = img.shape[1], img.shape[2]
        # convert bbox coordinate to releative coordinate
        bbox_relative = []
        for bbox in bboxes:
            top, left, heigt, width, class_label = bbox
            xc = (left + width / 2) / w
            yc = (top + heigt / 2) / h
            wr = width / w
            hr = heigt / h
            bbox_relative.append([class_label, xc, yc, wr, hr])
        # write to file
        with open('train/labels/' + img_name.split('.')[0] + '.txt', 'w') as fw:
            for bbox in bbox_relative:
                fw.write(' '.join(map(str, bbox)) + '\n')
        
