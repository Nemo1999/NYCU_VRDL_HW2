# Demo for VRDL HW2

## References

- [yolov5 Github Repo](https://github.com/ultralytics/yolov5)

## Prerequists
- python >= 3.6.0
- torch >= 1.7
## Use Instructions
Example using Anaconda: 
### Create and activate new environmeent:　
```bash
conda create -n hw2_demo python>=3.6.0 
conda activate hw2_demo
```
### Install torch and torchvision

```bash
conda install pytorch>=1.7 torchvision cudatoolkit={your cuda version} -c pytorch
```

### Install additional dependencies

```bash
make install
```
### Download Digit datasets and Generate COCO-Style annotation

```bash
make getdataset
```
This script download training data from TA's google drive, and arrange it into COCO format.
I also host a preprocessed annotation file in my own google drive, so the `.mat` file is ignored.

### Reproduce answer.json
```bash
make reproduce
```  
This will download model weights from my google drive and reproduce answer.json

### Train the model (fine-tune)
```bash
make train
```

If the training is interrupted, you can resume the training by:
```bash
cd yolov5/ && python train.py --resume
```


The training result will be stored in the `./yolov5/runs/train/exp` directory. 

(If you want to restart the trainning, you need to rename or delete the directory.)

To visualize the training result, you can use the following command:
```bash
tensorboard --logdir=./yolov5/runs/train/exp
```

### Test the model

Test the model by running the following command:
```bash
make inference
```
This will use the best model in the `./yolov5/runs/train/exp` directory by default.

You can also specify the model by:
```bash
cd yolov5/ && python inference.py --model_path={path to the model}
```
## Inference Results

![](https://i.imgur.com/yfIhwIX.jpg) 
![](https://i.imgur.com/ZkmNwoU.jpg)

## Training Process
![](https://i.imgur.com/aTm5Lew.png)


## Statistics
![](https://i.imgur.com/ObGD9Pj.png)
![](https://i.imgur.com/yaYYL8R.png)
![](https://i.imgur.com/zo9YBjF.png)
