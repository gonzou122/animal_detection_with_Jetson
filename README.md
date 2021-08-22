# animal_detection_with_Jetson
Jetsonを用いた動物検出

#　手順 <br>
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


