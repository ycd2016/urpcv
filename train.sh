#!/bin/bash
python3 ./utils.py xml2yolo
darknet detector train ./yolo/obj.data ./yolo/yolo4urpc.cfg ./yolo/yolov4-tiny.weights -dont_show -map -clear
