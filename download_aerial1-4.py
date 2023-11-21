from roboflow import Roboflow
rf = Roboflow(api_key="iKA9P5eUE0Kaej16Tg0e")
project = rf.workspace("mohammed-vo6ua").project("areial1")
dataset = project.version(4).download("yolov7")