#!/bin/bash
darknet detector train ./yolo/obj.data ./yolo/yolo4urpc.cfg ./yolo/yolov4-tiny.weights -dont_show -map -clear
