import random
import os
import shutil
import subprocess
from torchvision.io import read_image
import gdown
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test-only', action='store_true', help='Only download test data')
opt = parser.parse_args()

# create empty dataset folder for Digits dataset
if os.path.exists('datasets/Digits'):
    shutil.rmtree('datasets/Digits')
os.mkdir('datasets/Digits')

# download dataset from google drive
# training data
if not opt.test_only:
    url = 'https://drive.google.com/uc?id=1lrKueI4HrySQDGvpkilQN9BfaMUN7hZi'
    output = 'datasets/Digits/train.zip'
    gdown.download(url, output, quiet=False)
    subprocess.run("unzip -q datasets/Digits/train.zip -d datasets/Digits/", shell=True)
    shutil.rmtree('datasets/Digits/__MACOSX')
    os.mkdir('datasets/Digits/train/images')
    os.mkdir('datasets/Digits/train/labels')
    subprocess.run("mv datasets/Digits/train/*.png datasets/Digits/train/images/", shell=True)
    subprocess.run("rm datasets/Digits/train/*.mat datasets/Digits/train/*.m", shell=True)

# testing data
url = 'https://drive.google.com/uc?id=1Fm-avdeNgzhPxhvia0iw9yZzcoOggy7I'
output = 'datasets/Digits/test.zip'
gdown.download(url, output, quiet=False)
subprocess.run("unzip -q datasets/Digits/test.zip -d datasets/Digits/", shell=True)
shutil.rmtree('datasets/Digits/__MACOSX')
os.mkdir('datasets/Digits/test/images')
os.mkdir('datasets/Digits/test/labels')
subprocess.run("mv datasets/Digits/test/*.png datasets/Digits/test/images/", shell=True)


if not opt.test_only:
    # download preprocessed annotation.txt file from my google drive 
    url = 'https://drive.google.com/uc?id=1KV5tboKuQY5ZZKdvWEb3HCkAn5C1eTUz'
    output = 'datasets/Digits/annotation.txt'
    gdown.download(url, output, quiet=False)


    with open('datasets/Digits/annotation.txt') as f:
        for line in f:
            fields = line.strip().split(',')
            img_name, bboxes = fields[1], fields[2:]
            img_name = img_name.split(':')[1]
            bboxes = [list(map(int, bb.split(':'))) for bb in bboxes]

            # get image size
            img = read_image(os.path.join('datasets/Digits/train/images', img_name))
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
            with open('datasets/Digits/train/labels/' + img_name.split('.')[0] + '.txt', 'w') as fw:
                for bbox in bbox_relative:
                    fw.write(' '.join(map(str, bbox)) + '\n')
        
