

.PHONY: install all getdataset train evaluate reproduce

install: 
	@echo "Installing dependencies"
	pip install -r yolov5/requirements.txt
	pip install gdown
	pip install googledrivedownloader

getdataset: datasets/Digits/test datasets/Digits/train datasets/Digits/validate
	@echo "Downloading datasets..."

train: yolov5/runs/train/exp
	@echo "Training..."

inference: yolo/runs/train/exp/weights/best.pt
	@echo "Evaluating..."
	python inference.py --model yolov5/runs/train/exp/weights/best.pt 

reproduce:
	@echo downloading model.pth from google drive
	gdown "https://drive.google.com/uc?id=13KMwvYO4WZFlfM6IxOW6IXefdFKW_7pP"
	@echo "Reproducing answer.json..."
	cd yolov5 && python ../inference.py --model ../model.pth

datasets/Digits/test datasets/Digits/train:
	python3 Download_Digits_COCO.py

datasets/Digits/validate:
	python3 Sample_Validations.py

yolov5/runs/train/exp: 
	@echo "Training..."
	python3 yolov5/train.py --img-size 640 \
	                        --dataset Digits.yaml \
							--epochs 80 \
							--batch-size 16 \
							--weights yolov5/weights/yolov5l.pth \
							--multi-scale  \
							--hyp hyp.digits.json


