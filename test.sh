#!/bin/bash
./darknet detector test ./obj.data ./yolo4urpc.cfg ./backup/yolo4urpc_best.weights -ext_output -dont_show -out result.json < ./testa.txt
