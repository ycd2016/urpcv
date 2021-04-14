#!/bin/bash
python3 ./utils.py json2sub
darknet detector test ./yolo/obj.data ./yolo/yolo4urpc.cfg ./backup/yolo4urpc_best.weights -ext_output -dont_show -out result.json < ./yolo/testa.txt
