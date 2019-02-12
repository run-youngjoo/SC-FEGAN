# SC-FEGAN
SC-FEGAN : Face Editing Generative Adversarial Network with User's Sketch and Color
Youngjoo Jo, Jongyoul Park

![Teaser Image](imgs/teaser.png)

## Overview
We learn to edit face image with a deep network. Our network SC-FEGAN is well suited to generate high quality synthetic image using intuitive user inputs with sketch and color. We used SN-patchGAN discriminator and Unet-like generator with gated convolutional layers.

## Dependencies
- tensorflow
- numpy
- Python3
- PyQt5

## Usage
First, download the model from [Google drive](https://drive.google.com/open?id=1VPsYuIK_DY3Gw07LEjUhg2LwbEDlFpq1).

Basic usage is:
  ```
  mv /${HOME}/FC-FEGAN.ckpt.* /${HOME}/ckpt/
  python3 demo.py
  ```
  
Select the number of GPU by editing demo.yaml file (not support multi-GPUs).
  ```
  GPU_NUM: 1 (the number you want to use)
  #GPU_NUM: (if you want to use only CPU, erase the number)
  ```
  
You can use our network with simple GUI.

## Example Results
### Face editing
![Face editing](imgs/face_edit.jpg)

### Edit earring
![Earring](imgs/earring.jpg)

### Face restoration
![restore1](imgs/restoration.jpg)

### Face restoration (with totally erased image)
![restore2](imgs/restoration2.jpg)

## License
CC 4.0 Attribution-NonCommercial International

The software is for educaitonal and academic research purpose only.
