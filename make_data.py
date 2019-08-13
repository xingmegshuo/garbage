#!/usr/bin/env python
# coding=utf-8
# Author: xiaomayi
# Mail:  xm.chnb@gmail.com
# Created Time: 2019年08月04日 星期日 18时40分52秒
# ps: 预处理数据，用于生成迭代器供深度学习训练加载数据。0.0版本,适用本次数据


from PIL import Image
import numpy as np
import os
import random


data_dir = 'Trainset/Trainset/'

train_data_dir = 'data/train/'
vilad_data_dir = 'data/vialid/'

img_list = os.listdir(data_dir)
random.shuffle(img_list)


def change_dir(pic_list, file):
    os.makedirs(file+'garbage')
    os.makedirs(file+'no_garbage')
    for i in pic_list:
        if i[:2] == '10':
            img = Image.open(data_dir+i)
            img = img.convert('RGB')
            img = img.resize((400,400),Image.ANTIALIAS)
            img.save(file+'garbage/'+i)
            print(np.array(img).shape)
        elif i[:2] == '00':
            img = Image.open(data_dir+i)
            img = img.convert('RGB')
            img = img.resize((400,400),Image.ANTIALIAS)
            img.save(file+'no_garbage/'+i)

if __name__ == '__main__':
    change_dir(img_list[:int(len(img_list) * 0.8)], train_data_dir)
    change_dir(img_list[int(len(img_list) * 0.8):], vilad_data_dir)
