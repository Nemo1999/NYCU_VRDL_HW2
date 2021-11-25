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