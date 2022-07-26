# yolov5_strongsort_osnet
このレポジトリは、Docker container上で物体追跡アルゴリズム[Yolov5_StrongSORT_OSNet](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet)を実行するための、環境構築と実行を行うファイルを保存するものです。

## 環境構築
Dockerがインストールされている環境で、以下のコマンドを実行してください。
```
$ git clone https://github.com/Tyanakai/yolov5_strongsort_osnet_with_docker.git
$ cd yolov5_strongsort_osnet
$ docker-compose up -d
```
## 実行
上記コマンドによって`traffic_object_tracer`というDocker containerが作成されたのを確認し、
```
$ python container_exec.py
```
により、Yolov5_StrongSORT_OSNetがcontainer内で実行されます。<br>
container内のデータはローカルフォルダと同期しています。

`python_src/input`以下に置いた動画に対し、物体追跡アルゴリズムを実行し、その結果作成されるファイルに基づいて、何台の車両が動画中映り込んだかをカウントします。
