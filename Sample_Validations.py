import random
import os
import shutil
import glob

# create validate folder for Digits dataset
if os.path.exists('datasets/Digits/validate'):
    shutil.rmtree('datasets/Digits/validate')
os.mkdir('datasets/Digits/validate')
os.mkdir('datasets/Digits/validate/images')
os.mkdir('datasets/Digits/validate/labels')

# move 10% of the images with annotations to validate folder
random.seed(1123)
train_images = glob.glob('datasets/Digits/train/images/*.png')
val_images = random.sample(train_images, len(train_images) // 10)
for img in val_images:
    label = img.replace('images', 'labels').replace('.png', '.txt')
    os.rename(img, img.replace('train', 'validate'))
    os.rename(label, label.replace('train', 'validate'))