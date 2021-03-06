

.PHONY: install all getdataset train evaluate reproduce

install: 
	@echo "Installing dependencies"
	pip install -r yolov5/requirements.txt
	pip install gdown

getdataset: datasets/Digits/train datasets/Digits/validate
	@echo "Downloading datasets..."

train: yolov5/runs/train/exp 
	@echo "Training..."

inference: datasets/Digits/test yolov5/runs/train/exp/weights/best.pt
	@echo "Evaluating..."
	cd yolov5 && python ../inference.py --model runs/train/exp/weights/best.pt 

reproduce: datasets/Digits/test
	@echo downloading model.pth from google drive
	gdown "https://drive.google.com/uc?id=13KMwvYO4WZFlfM6IxOW6IXefdFKW_7pP"
	@echo "Reproducing answer.json..."
	cd yolov5 && python ../inference.py --model ../model.pth

datasets/Digits/train: 
	python3 Download_Digits_COCO.py

datasets/Digits/test: 
	python3 Download_Digits_COCO.py --test-only

datasets/Digits/validate:
	python3 Sample_Validations.py

yolov5/runs/train/exp: getdataset
	@echo "Training..."
	cd yolov5 && python3 train.py --img-size 512 \
	                        --data ../Digits.yaml \
							--epochs 80 \
							--batch-size 16 \
							--weights yolov5l.pt \
							--hyp ../hyp.digits.yaml


