import random
import os
import glob

random.seed(1123)
train_images = glob.glob('/home/nemo/VRDL2021/HW2_Detection/datasets/Digits/train/images/*.png')
print(train_images)
val_images = random.sample(train_images, len(train_images) // 10)
for img in val_images:
    label = img.replace('images', 'labels').replace('.png', '.txt')
    os.rename(img, img.replace('train', 'validate'))
    os.rename(label, label.replace('train', 'validate'))