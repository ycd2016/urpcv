#!/bin/bash
darknet detector calc_anchors ./yolo/obj.data -num_of_clusters 6 -width 608 -height 608
