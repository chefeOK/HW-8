import os
import shutil
import random

# Parameters
train_ratio = 0.8  # 80% of data for training, 20% for validation
image_dir = 'path/to/your/images'
label_dir = 'path/to/your/labels'
dataset_dir = 'dataset'

# Create dataset directories
os.makedirs(os.path.join(dataset_dir, 'images/train'), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, 'images/val'), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, 'labels/train'), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, 'labels/val'), exist_ok=True)

# Get list of files
images = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
random.shuffle(images)

# Split data
train_count = int(train_ratio * len(images))
train_images = images[:train_count]
val_images = images[train_count:]

def move_files(file_list, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for file in file_list:
        base_name = os.path.splitext(file)[0]
        img_src = os.path.join(src_img_dir, file)
        lbl_src = os.path.join(src_lbl_dir, base_name + '.txt')
        img_dest = os.path.join(dest_img_dir, file)
        lbl_dest = os.path.join(dest_lbl_dir, base_name + '.txt')

        shutil.copyfile(img_src, img_dest)
        if os.path.exists(lbl_src):
            shutil.copyfile(lbl_src, lbl_dest)

# Move files to train and val directories
move_files(train_images, image_dir, label_dir, os.path.join(dataset_dir, 'images/train'), os.path.join(dataset_dir, 'labels/train'))
move_files(val_images, image_dir, label_dir, os.path.join(dataset_dir, 'images/val'), os.path.join(dataset_dir, 'labels/val'))

print('Dataset organized successfully.')
