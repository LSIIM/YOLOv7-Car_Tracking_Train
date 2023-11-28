#!/bin/bash
#
# Script de exemplo para submeter trabalho que não use MPI
#
#SBATCH --job-name=yolov7_train # Nome do trabalho a ser executado (para melhor identificação)
#SBATCH --partition=open_cpu # Em qual fila o trabalho será executado (ver filas disponíveis com o comando sinfo)
#SBATCH --nodes 1 # Número de nós (computadores) que serão utilizados (1 para códigos openMP)
#SBATCH --cpus-per-task=4 # Número de cores que será utilizado
#SBATCH --mem 2048 # Quanto de memória em MB por nó (computador) o programa necessitará.
#SBATCH --time=30:00:00 # Tempo máximo de simulação (D-HH:MM).
#SBATCH -o cons_out.%j.out # Nome do arquivo onde a saída (stdout) será gravada %N = Máquina , %j = Número do trabalho.
#SBATCH -e cons_err.%j.err # Nome do arquivo para qual a saída de erros (stderr) será redirecionada.
#SBATCH --mail-user=dev.rodrigofs@gmail.com # Email para enviar notificações sobre alteraçãono estados do trabalho
#SBATCH --mail-type=BEGIN # Envia email quando o trabalho for iniciado
#SBATCH --mail-type=END # Envia email quando o trabalho finalizar
#SBATCH --mail-type=FAIL # Envia email caso o trabalho apresentar uma mensagem de erro.
python yolov7_train "/home/antoniosobieranski/ralph/VAID_yolo"
python yolov7_train "/home/antoniosobieranski/ralph/YOLOv7-Car_Tracking_Train/Areial1-4"

