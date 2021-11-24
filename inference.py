import torch
import os
import glob
from PIL import Image
import json
import tqdm

model = torch.hub.load('.', 'custom', path='runs/train/exp13/weights/best.pt',source='local')
# help(model)
print(model.conf, model.classes, model.iou)
"""
# Test your inference time
TEST_IMAGE_NUMBER = 100 # This number is fixed.
test_img_list = []

# Read image (Be careful with the image order)
data_listdir.sort(key = lambda x: int(x[:-4]))
for img_name in data_listdir[:TEST_IMAGE_NUMBER]:
  img_path = os.path.join("/content/mmdetection/test", img_name)
  img = cv2.imread(img_path)
  test_img_list.append(img)

start_time = time.time()
for img in tqdm(test_img_list):
    # your model prediction
    pred = inference_detector(model, img)

end_time  = time.time()
print("\nInference time per image: ", (end_time - start_time) / len(test_img_list))

# Remember to screenshot!

"""



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
    # read the image
    img_path = os.path.join(data_dir, img_name)
    img = Image.open(img_path)
    w, h = img.size[0], img.size[1]
    # your model prediction
    pred = model(img, size=640)
  
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

with open("answer.json", "w") as outfile:
    outfile.write(json_object)
