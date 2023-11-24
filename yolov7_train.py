import torch
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob

# pega o caminho pro dataset do argumento
dataset_location = sys.argv[1]

print(dataset_location)
data_yaml_path = dataset_location + "/data.yaml"

import os
data_yaml_path = dataset_location + "/data.yaml"

# python train.py --batch 16 --epochs 55 --data '{data_yaml_path}' --weights 'yolov7.pt' --device 0
# verifica se o cuda esta disponivel
if torch.cuda.is_available():
    # se sim, treina com o cuda
    print("cuda is available")
    os.system(f"python yolov7/train.py --batch-size 4 --epochs 2 --data '{data_yaml_path}' --weights 'yolov7.pt' --device 0")
else:
    # se nao, treina com o cpu
    print("cuda is not available")
    os.system(f"python yolov7/train.py --batch-size 4 --epochs 2 --data '{data_yaml_path}' --weights 'yolov7.pt'")

# le o log do ultimo treino e gera os graficos e salva ma pasta do experimento


# pega o ultimo log
log_list = glob.glob("runs/train/*")
log_list.sort()
exp_path = log_list[-1]
# pega o nome do events.out.tfevents (lista os arquivos da pasta e pega o que começa com events)
event_file = glob.glob(exp_path + "/events*")[0]

# # usa o tensorboard para ler o log
# from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
# event_acc = EventAccumulator(event_file)
# event_acc.Reload()

# # pega os dados do log
# print(event_acc.Tags())
# # pega os dados de treino
# training_accuracies =   event_acc.Scalars('train/box_loss')
# training_losses =       event_acc.Scalars('train/obj_loss')
# training_precisions =   event_acc.Scalars('train/cls_loss')
# # pega os dados de validacao
# validation_accuracies = event_acc.Scalars('val/box_loss')
# validation_losses =     event_acc.Scalars('val/obj_loss')
# validation_precisions = event_acc.Scalars('val/cls_loss')

# # cria um dataframe com os dados de treino
# df = pd.DataFrame(columns=['epoch', 'metric', 'value'])

# # pega os dados de treino
# for item in training_accuracies:
#     df = df.append({'epoch': item.step, 'metric': 'training_accuracy', 'value': item.value}, ignore_index=True)
# for item in training_losses:
#     df = df.append({'epoch': item.step, 'metric': 'training_loss', 'value': item.value}, ignore_index=True)
# for item in training_precisions:
#     df = df.append({'epoch': item.step, 'metric': 'training_precision', 'value': item.value}, ignore_index=True)
    
# # pega os dados de validacao
# for item in validation_accuracies:
#     df = df.append({'epoch': item.step, 'metric': 'validation_accuracy', 'value': item.value}, ignore_index=True)
# for item in validation_losses:
#     df = df.append({'epoch': item.step, 'metric': 'validation_loss', 'value': item.value}, ignore_index=True)
# for item in validation_precisions:
#     df = df.append({'epoch': item.step, 'metric': 'validation_precision', 'value': item.value}, ignore_index=True)

# # para cada metrica faz um grafico
# for metric in df['metric'].unique():
#     # pega os dados da metrica
#     df_metric = df[df['metric'] == metric]
#     # pega o maximo da metrica
#     max_value = df_metric['value'].max()
#     # pega o epoch do maximo da metrica
#     max_epoch = df_metric[df_metric['value'] == max_value]['epoch'].values[0]
#     # pega o valor da metrica no epoch do maximo
#     max_value = df_metric[df_metric['epoch'] == max_epoch]['value'].values[0]
#     # faz o grafico
#     sns.lineplot(data=df_metric, x="epoch", y="value")
#     # adiciona o maximo no grafico
#     plt.text(max_epoch, max_value, f"max: {max_value:.3f}")
#     # salva o grafico
#     plt.savefig(f"{exp_path}/{metric}.png")
#     # limpa o grafico
#     plt.clf()
#     plt.close()
    


