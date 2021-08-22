# animal_detection_with_Jetson
Jetsonを用いた動物検出<br>
自分用プロジェクト管理

## 環境
デスクトップPC<br>
Windows11(Windows Insider Program)<br>
CPU:Ryzen9 5900X<br>
GPU:RTX3070<br>
メモリ:32GB<br>

Docker<br>
Docker desktop for windows<br>
WSL2:ubuntu20.04<br>
※GPU利用環境の構築手順<br>
https://qiita.com/gonzou122/items/7b5e74d7c4c5f3e969af

Jetson<br>
Jetson B01(4GB)<br>
JetPack 4.5<br>


## 手順 
1:Jetsonのセットアップ <br>
2:目的の動物の画像集め:デスクトップPC(docker) <br>
3:画像のリサイズ:デスクトップPC(docker) <br>
4:アノテーション:デスクトップPC(VOTT) <br>
4:YOLOv3のセットアップ:デスクトップPC(docker) <br>
5:学習済みのデータを利用した転移学習:デスクトップPC(docker) <br>
6:学習が完了したデータの重みをJetsonで利用できる形式(TensorRT)に変換:Jetson<br>
7:JetsonのUSBカメラで目的の動物が検出できるか確認<br>
<br>
↓将来<br>
8:検出した画像をLINEで確認できるようにする<br>
<br>

### 1:Jetsonセットアップ
割愛

### 2:目的の動物の画像集め
Google画像検索などを用いて画像の収集を行う。<br>
手動では時間がかかるため、「icrawler」を用いてスクレイビングを行う。<br>
https://github.com/hellock/icrawler <br>
デスクトップPCのローカル環境ではなくDockerで実行する。<br>
※Dockerfile未作成<br>

Dockerのベースイメージ<br>
ubuntu:20.04<br>
イメージをpull後コンテナを起動して以下コマンドを実行<br>
~~~
WSL2のターミナル
docker run -it ubuntu:20.04 bash
~~~

~~~
コンテナ内
apt update -y && apt upgrade -y
apt install -y python3
apt install -y python3-pip
apt insatll -y icrawler
~~~
Ctrl+p,Ctrl+qでコンテナから抜けてコンテナをコミットしてimageを作成<br>
~~~
WSL2のターミナル
docker commit <コンテナ名orコンテナID>　<イメージ名>
~~~
画像収集用のpyファイルを作成してコンテナにマウントするホストPCのフォルダに格納する。
https://github.com/gonzou122/animal_detection_with_Jetson/blob/main/image_download.py

icrawlerが利用できるDockerイメージが作成されるので、ホストPCのフォルダをマウントしてDockerコンテナを起動する。<br>
フォルダ構成<br>
~~~
── ./適当なフォルダ
    ├────image_download.py(適当なフォルダの直下)
    ├────(image_download.py実行後の画像格納フォルダ）
~~~

~~~
WSL2のターミナル
対象のフォルダに移動
cd <コンテナをマウントするフォルダ>
docker run -it --rm -v $PWD:/opt <先ほど作成したイメージ名> bash
~~~

~~~
コンテナのターミナル
対象のフォルダに移動
cd <コンテナをマウントするフォルダ>
python3 image_download.py
~~~
ターミナルに結果が出力される。画像はコンテナをマウントしたフォルダの直下に新しく作成されたフォルダに格納されている。<br>

### 3:画像のリサイズ:デスクトップPC(docker)
作成中


