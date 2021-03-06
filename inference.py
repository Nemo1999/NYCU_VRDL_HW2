import torch
import os
import glob
from PIL import Image
import json
import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='runs/train/exp/weights/best.pt', help='model path')
opt = parser.parse_args()

model = torch.hub.load('.', 'custom', path=opt.model, source='local')
# help(model)
print(model.conf, model.classes, model.iou)


# Use the results from your model to generate the output json file
# Read image (Be careful with the image order)

data_dir = "../datasets/Digits/test/images"
data_listdir = os.listdir(data_dir)
data_listdir.sort(key = lambda x: int(x[:-4]))
result_to_json = []

# for each test image
for img_name in tqdm.tqdm(data_listdir):
    # the image_name is as same as the image_id
    image_id = int(img_name[:-4])
    # image path
    img_path = os.path.join(data_dir, img_name)
    
    # your model prediction
    pred = model(img_path)
  
    #help(pred)
    pred = pred.xyxy[0].cpu().detach().numpy()

    # add each detection box infomation into list
    #your_model_detection_output[img_name] = all_det_boxes_in_this_image

    for box in pred:
        det_box_info = {}
        xmin, ymin, xmax, ymax, score, label = list(box)
        # An integer to identify the image
        det_box_info["image_id"] = image_id
        # A list ( [left_x, top_y, width, height] )
        det_box_info["bbox"] = [xmin.item(), ymin.item(), (xmax-xmin).item(), (ymax-ymin).item()]
        # A float number between 0 ~ 1 which means the confidence of the bbox
        det_box_info["score"] = score.item()
        
        # An integer which means the label class
        if int(label) == 10:
            label = 0
        det_box_info["category_id"] = int(label)
        
        result_to_json.append(det_box_info)
# Write the list to answer.json 
json_object = json.dumps(result_to_json, indent=4)

print("answer written to answer.json")
with open("../answer.json", "w") as outfile:
    outfile.write(json_object)
