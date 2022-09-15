# coding=utf-8
from __future__ import absolute_import, division, print_function

import logging
import argparse
import os
import random
import numpy as np
import time

from datetime import timedelta

from PIL import Image
from torchvision import transforms

import torch
import torch.distributed as dist

from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
from apex import amp
from apex.parallel import DistributedDataParallel as DDP

from models.modeling import VisionTransformer, CONFIGS
from utils.scheduler import WarmupLinearSchedule, WarmupCosineSchedule
from utils.data_utils import get_loader
from utils.dist_util import get_world_size

import os







def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname




def valid_new(args, model):
    # Validation!
    
    # _, test_loader = get_loader(args)


    flag = 0

    folder_dir='./INat2017/train_val_images/'
    dirs_archive=[]
    file_archive=[]

    for i in findAllFile(folder_dir):
        #print(i)
        file_archive.append(i)

    for i in range(len(file_archive)):
        # transform ori image and save

        path_img = file_archive[i]


        img = Image.open(path_img).convert('RGB')

        transform=transforms.Compose([transforms.Resize((304, 304), Image.BILINEAR),
                                    #transforms.CenterCrop((448, 448)),
                                    ])
        
        imgt = transform(img)
        new_image = './new_images/'+"{:09d}".format(i)+'.jpg'
        print(new_image)
        imgt.save(new_image)

        img = Image.open(path_img).convert('RGB')
        transform=transforms.Compose([transforms.Resize((304, 304), Image.BILINEAR),
                                    #transforms.CenterCrop((448, 448)),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

        img = transform(img).unsqueeze(0)
        img = img.to(args.device)

        model.eval()
        with torch.no_grad():
            _, attn = model(img)
        
        attn = attn.squeeze()        
        attn = torch.sum(attn, dim=0)


        new_npy = './new_images_attention/'+"{:09d}".format(i)+'.npy'
        np.save(new_npy, attn.cpu().numpy())
        



    return flag















if __name__ == "__main__":
    valid_new(args, model)
