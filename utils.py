import os
import sys
import json
import imagesize
import pandas as pd
from tqdm import tqdm
import xml.etree.ElementTree as et


def xml2yolo():
    namemap = {"holothurian": 0, "echinus": 1, "scallop": 2, "starfish": 3}
    for xml in tqdm(os.listdir("train/box")):
        rt = et.parse(f"train/box/{xml}").getroot()
        w = int(rt.find("size").find("width").text)
        h = int(rt.find("size").find("height").text)
        with open(f'train/image/{xml.split(".")[0]}.txt', "w") as f:
            for obj in rt.findall("object"):
                name = obj.find("name").text
                xmin = int(obj.find("bndbox").find("xmin").text)
                ymin = int(obj.find("bndbox").find("ymin").text)
                xmax = int(obj.find("bndbox").find("xmax").text)
                ymax = int(obj.find("bndbox").find("ymax").text)
                if name != "waterweeds":
                    f.write(
                        f"{namemap[name]} {(xmin+xmax)/w/2.} {(ymin+ymax)/h/2.} {(xmax-xmin)/w} {(ymax-ymin)/h}"
                        + "\n"
                    )


def json2sub():
    with open("result.json", "r") as f:
        res = json.load(f)
    lst = []
    for img in tqdm(res):
        x, y = imagesize.get(img["filename"])
        for obj in img["objects"]:
            if obj["class_id"] != 2 and obj["confidence"] < 0.25:
                continue
            crd = obj["relative_coordinates"]
            lst.append(
                [
                    obj["name"],
                    img["frame_id"],
                    obj["confidence"],
                    max(0, crd["center_x"] - crd["width"] / 2) * x,
                    max(0, crd["center_y"] - crd["height"] / 2) * y,
                    min(1, crd["center_x"] + crd["width"] / 2) * x,
                    min(1, crd["center_y"] + crd["height"] / 2) * y,
                ]
            )
    sub = pd.DataFrame(
        lst, columns=["name", "image_id", "confidence", "xmin", "ymin", "xmax", "ymax"]
    )
    sub["image_id"] = sub["image_id"].astype(str).str.zfill(6)
    sub.to_csv("sub.csv", index=False)


if __name__ == "__main__":
    if sys.argv[1] == "xml2yolo":
        xml2yolo()
    if sys.argv[1] == "json2sub":
        json2sub()
