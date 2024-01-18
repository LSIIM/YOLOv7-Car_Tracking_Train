# testa a conversão

import os
from tqdm import tqdm
VAID_dataset_dir = "/mnt/lsiim/home/ralph/prf/VAID_yolo"

# teste do train

for file in tqdm(os.listdir(VAID_dataset_dir + '/train/labels')):
    if(not os.path.exists(VAID_dataset_dir + '/train/images/' + file.split('.')[0] + '.jpg')):
        print(f"O arquivo {file.split('.')[0]}.jpg não existe no /train/images mas existe no /train/labels")
    
    if(os.path.exists(VAID_dataset_dir + '/val/labels/' + file)):
        print(f"O arquivo {file} esta repetido entre val e train")

for file in tqdm(os.listdir(VAID_dataset_dir + '/train/images')):
    if(not os.path.exists(VAID_dataset_dir + '/train/labels/' + file.split('.')[0] + '.txt')):
        print(f"O arquivo {file.split('.')[0]}.jpg não existe no /train/labels mas existe no /train/images")

# teste do val

for file in tqdm(os.listdir(VAID_dataset_dir + '/val/labels')):
    if(not os.path.exists(VAID_dataset_dir + '/val/images/' + file.split('.')[0] + '.jpg')):
        print(f"O arquivo {file.split('.')[0]}.jpg não existe no /val/images mas existe no /val/labels")

    if(os.path.exists(VAID_dataset_dir + '/train/labels/' + file)):
        print(f"O arquivo {file} esta repetido entre val e train")

for file in tqdm(os.listdir(VAID_dataset_dir + '/val/images')):
    if(not os.path.exists(VAID_dataset_dir + '/val/labels/' + file.split('.')[0] + '.txt')):
        print(f"O arquivo {file.split('.')[0]}.jpg não existe no /val/labels mas existe no /val/images")