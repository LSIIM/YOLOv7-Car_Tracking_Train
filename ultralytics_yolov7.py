import os



from ultralytics import YOLO




# Load a model
model = YOLO("yolov7.pt")  # build a new model from scratch

# Use the model
results = model.train(data=os.path.join(ROOT_DIR, "/mnt/hd/Projects_Datasets/GlobalDrones/PRF/VAID_yolo/data.yaml"), epochs=5, patience=300,batch=4 )  # train the model
