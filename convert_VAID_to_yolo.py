# vai iterar pelo dataset vaid e vai criar um dataset VAID_yolo com um data.yaml


# names:
# - sedan
# - minibus
# - truck
# - pickup
# - bus
# - cement truck
# - trailer
# nc: 7
# train: mnt/hd/Projects_Datasets/GlobalDrones/PRF/VAID_yolo/train/images
# val: mnt/hd/Projects_Datasets/GlobalDrones/PRF/VAID_yolo/val/images



import os
import yaml
import glob
import random
from tqdm import tqdm
from pprint import pprint

# path to VAID dataset
VAID_path = "/mnt/hd/Projects_Datasets/GlobalDrones/PRF/VAID_dataset"

# path to VAID_yolo dataset
VAID_yolo_path = "/mnt/hd/Projects_Datasets/GlobalDrones/PRF/VAID_yolo"

# no dataset do vai tem as pastas
# Annotations -> contem os arquivos xml no estilo

# <annotation>
# <folder>DJI_0015</folder>
# <filename>000001.jpg</filename>
# <path>C:\Users\ChihYi\Downloads\image\190321\DJI_0015\000001.jpg</path>
# <source>
# <database>Unknown</database>
# </source>
# <size>
# <width>1137</width>
# <height>640</height>
# <depth>3</depth>
# </size>
# <segmented>0</segmented>
# <object>
# <name>1</name>
# <pose>Unspecified</pose>
# <truncated>0</truncated>
# <difficult>0</difficult>
# <bndbox>
# <xmin>387</xmin>
# <ymin>348</ymin>
# <xmax>439</xmax>
# <ymax>367</ymax>
# </bndbox>
# </object>
# <object>
# <name>1</name>
# <pose>Unspecified</pose>
# <truncated>0</truncated>
# <difficult>0</difficult>
# <bndbox>
# <xmin>598</xmin>
# <ymin>350</ymin>
# <xmax>643</xmax>
# <ymax>371</ymax>
# </bndbox>
# </object>
# <object>
# <name>1</name>
# <pose>Unspecified</pose>
# <truncated>0</truncated>
# <difficult>0</difficult>
# <bndbox>
# <xmin>844</xmin>
# <ymin>352</ymin>
# <xmax>890</xmax>
# <ymax>371</ymax>
# </bndbox>
# </object>
# </annotation>


# JPEGImages -> contem as imagens jpg


# cria as pastas
os.makedirs(VAID_yolo_path + "/train/images", exist_ok=True)
os.makedirs(VAID_yolo_path + "/train/labels", exist_ok=True)
os.makedirs(VAID_yolo_path + "/val/images", exist_ok=True)
os.makedirs(VAID_yolo_path + "/val/labels", exist_ok=True)

# as labels que eu vou criar tem que ser em .txt no estilo (cada uma)

# 2 0.46875 0.4483173076923077 0.057692307692307696 0.055288461538461536
# 2 0.22302737343962556 0.34655865144234915 0.12603786430086927 0.10569810514656047
# 2 0.9675480769230769 0.9543269230769231 0.06009615384615385 0.08653846153846154


# cria o arquivo data.yaml
data_yaml = {}
data_yaml["names"] = [
    "sedan",
    "minibus",
    "truck",
    "pickup",
    "bus",
    "cement truck",
    "trailer"
]
data_yaml["nc"] = 7
data_yaml["train"] = VAID_yolo_path + "/train/images"
data_yaml["val"] = VAID_yolo_path + "/val/images"

# cria o arquivo data.yaml
with open(VAID_yolo_path + "/data.yaml", 'w') as outfile:
    yaml.dump(data_yaml, outfile, default_flow_style=False)

# lista os arquivos xml e jpg e verifica se tem o mesmo nome
xml_list = glob.glob(VAID_path + "/Annotations/*.xml")
jpg_list = glob.glob(VAID_path + "/JPEGImages/*.jpg")

# separa em train e val as imagens
# 80% train e 20% val de forma aleatoria
random.shuffle(jpg_list)
train_list = jpg_list[:int(len(jpg_list)*0.8)]
val_list = jpg_list[int(len(jpg_list)*0.8):]

def get_info_from_xml(xml_path):
    # retorna o size e os objects do xml
    # pega as tags objects
    objects = []
    size_lines = []

    found_obj_tag = False
    object_lines = []

    found_size_tag = False
    with open(xml_path) as f:
        for line in f:
            # print(line)
            if "<object>" in line or found_obj_tag:
                found_obj_tag = True
                object_lines.append(line)
                if("</object>" in line):
                    found_obj_tag = False
                    # pprint(object_lines)
                    objects.append(object_lines)
                    object_lines = []
                    continue
                else:
                    continue
                
            if "<size>" in line or found_size_tag:
                found_size_tag = True
                size_lines.append(line)
                if("</size>" in line):
                    found_size_tag = False
    return size_lines, objects

def convert_to_yolo(size_lines, objects):
    # pega o width e height da imagem
    width = 0
    height = 0
    for line in size_lines:
        if "<width>" in line:
            width = int(line.replace("<width>", "").replace("</width>", ""))
        if "<height>" in line:
            height = int(line.replace("<height>", "").replace("</height>", ""))
    # o name é o numero da classe na tag object
    # o xmin, ymin, xmax, ymax é o bounding box na tag object
    objects_yolo = []
    for object_lines in objects:
        name = 0
        xmin = 0
        ymin = 0
        xmax = 0
        ymax = 0
        for line in object_lines:
            if "<name>" in line:
                name = int(line.replace("<name>", "").replace("</name>", ""))
            if "<xmin>" in line:
                xmin = int(line.replace("<xmin>", "").replace("</xmin>", ""))
            if "<ymin>" in line:
                ymin = int(line.replace("<ymin>", "").replace("</ymin>", ""))
            if "<xmax>" in line:
                xmax = int(line.replace("<xmax>", "").replace("</xmax>", ""))
            if "<ymax>" in line:
                ymax = int(line.replace("<ymax>", "").replace("</ymax>", ""))
    
        # print(f"width: {width}, height: {height}, name: {name}, xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}")
        # converte para o formato yolo
        # classe x y w h
        x = (float(xmin) + float(xmax)) / 2
        y = (float(ymin) + float(ymax)) / 2
        w = float(xmax) - float(xmin)
        h = float(ymax) - float(ymin)

        x = x / float(width)
        y = y / float(width)
        w = w / float(width)
        h = h / float(width)

        objects_yolo.append([int(name)-1, x, y, w, h])
    return objects_yolo

def convert_list(img_list, list_name):
    print(f"convertendo {list_name}")
    # cria as labels do train
    for image in tqdm(img_list):

        # pega o size e os objects do xml
        # pega as tags objects
        # print(image.split('.')[0])
        size_lines, objects = get_info_from_xml(image.replace("JPEGImages", "Annotations").replace(".jpg", ".xml"))    

        
                
        
        objects_yolo = convert_to_yolo(size_lines, objects)
        for object_yolo in objects_yolo:
            # cria o arquivo txt
            with open(image.replace(VAID_path,VAID_yolo_path).replace("JPEGImages", f"{list_name}/labels").replace(".jpg", ".txt"), 'a') as f:
                f.write(f"{object_yolo[0]} {object_yolo[1]} {object_yolo[2]} {object_yolo[3]} {object_yolo[4]}\n")
        
        # copia a imagem para a pasta train
        os.system(f"cp {image} {image.replace(VAID_path,VAID_yolo_path).replace('JPEGImages', f'{list_name}/images')}")



convert_list(train_list, "train")
convert_list(val_list, "val")




