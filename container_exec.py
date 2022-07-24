from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import os
import math

import docker
import pandas as pd

INPUT = os.path.join("yolo_strong_sort", "input")
FILE = "xroad2.mp4"
source = os.path.join(INPUT, FILE)
workdir = os.path.join("/usr", "src", "app")
sort_weight = "osnet_x1_0_msmt17.pt"
DURATION = 60  # 60 秒ごとに分割する


def split_movie():
    cli = docker.DockerClient(base_url="unix://var/run/docker.sock")
    file_name = os.path.splitext(FILE)[0]
    container_name = f"traffic_object_tracer"
    split_container = cli.containers.get(container_name)

    os.makedirs("yolo_strong_sort/splited", exist_ok=True)

    print(f"container id   :{split_container.id}")
    print(f"container name :{split_container.name}")

    command = f"python split.py {source} {DURATION}"
    
    # cont_work_dir = os.path.join("/usr", "src", "app", "python-src", "Yolov5_StrongSORT_OSNet")
    res = split_container.exec_run(cmd=command, detach=False, tty=True)
    print(res.output.decode("utf-8"))


def run_track():
    cli = docker.DockerClient(base_url="unix://var/run/docker.sock")
    file_name = os.path.splitext(FILE)[0]
    container_name = f"traffic_object_tracer"
    tracer_container = cli.containers.get(container_name)

    print(f"container id   :{tracer_container.id}")
    print(f"container name :{tracer_container.name}")

    command = f"python yolo_strong_sort/track.py --yolo-weights yolo_strong_sort/yolov5/weights/yolov5x6.pt" + \
              f" --source {source} --strong-sort-weights {sort_weight}" + \
              f" --config-strongsort yolo_strong_sort/strong_sort/configs/strong_sort.yaml" + \
              f" --save-vid --save-txt"
    
    res = tracer_container.exec_run(cmd=command, detach=False, tty=True)
    print(res.output.decode("utf-8"))


def count_object():
    source_filename = os.path.splitext(os.path.basename(source))[0]
    df = pd.read_csv(
        f"python_src/yolo_strong_sort/runs/track/exp/tracks/{source_filename}.txt", 
        sep=" ", 
        index_col=None,
        names=["frame", "id", "bbox_left", "bbox_top","bbox_w", "bbox_h", "label", "a", "b", "c", "d"]
        )
    print(df.groupby("label").id.nunique())


if __name__ == "__main__":

    split_movie()    # split movie

    run_track()    # detect traffic tracking
    
    count_object()    # count traffic object number

