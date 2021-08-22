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
https://github.com/hellock/icrawler
デスクトップPCのローカル環境ではなくDockerで実行する。<br>



