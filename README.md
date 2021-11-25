# Demo for VRDL HW2
## Create and activate new environmeent:　
```bash
conda create -n hw2_demo 
conda activate hw2_demo
```
## install torch and torchvision

```bash
conda install pytorch torchvision cudatoolkit={your cuda version} -c pytorch
```

## install additional dependencies

```bash
make install
```

##　download Digit datasets and Generate COCO-Style annotation

```bash
make getdataset
```

## Reproduce answer.json
```bash
make reproduce
```  
This will download model weights from my google drive and reproduce answer.json

## Train the model (fine-tune)
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

## Test the model

Test the model by running the following command:
```bash
make inference
```
This will use the best model in the `./yolov5/runs/train/exp` directory by default.

You can also specify the model by:
```bash
cd yolov5/ && python inference.py --model_path={path to the model}
```
