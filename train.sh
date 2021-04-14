#!/bin/bash
./darknet detector train ./obj.data ./yolo4urpc.cfg ./yolov4-tiny.weights -dont_show -map -clear
