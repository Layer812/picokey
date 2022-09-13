# picokey
Raspberry PICOの一種である[Itsy Bitsy RP2040](https://www.switch-science.com/catalog/7900/)を用いたUSB HIDデバイスです。<br>
GPIOよりキー入力を読み取り、定義したキーマップに従いUSB経由でPC/Raspberry Pi等にキーコードを送ります。<br>
現状、GPIOの接続先として[TRS-80 Model 100](https://www.massmadesoul.com/features/trs80)のみ対応しています。<br>

## 作り方
### 使うもの
 - [Itsy Bitsy RP2040](https://www.switch-science.com/catalog/7900/) 1個
 - ジャンパ線(オス-メス)適宜
 - USBケーブル(Micro - Type A)

### ハードウェア接続
1.TRS-80の裏蓋をあけ、メインユニットを取り外します。<br>
 [このあたりの動画](https://www.youtube.com/watch?v=hbLWk7ir9sI)を参考に、メインユニットを外します。<br>
キーボード基盤の左側にあるキーボードケーブル(黒10本、白10本)を次の工程で使います。<br>
2.キーボードケーブルとItsy Bitsyを接続します。<br>
以下のように合計17本のケーブルをItsy Bitsyに接続します。<br>
![キーボード接続図](https://user-images.githubusercontent.com/111331376/189836293-7701fa93-ca99-415a-8890-32104d5d2494.png)
ジャンパ線は細いのでコネクタに刺さりますが、Itsy Bitsyのピンヘッダをそのままさす場合は、<br>
SWITCH SCIENCEさんの[丸ピンヘッダ](https://www.switch-science.com/catalog/93/)なら行ける気がします。<br>

### ソフトウェア設定
1,Circuit python書き込み<br>
 Itsy Bitsyに[Circuit python 7.3x](https://circuitpython.org/board/adafruit_itsybitsy_rp2040/)のuf2を書き込みます。<br>
 (このあたり)[https://mag.switch-science.com/2017/08/30/circuitpython/]を参考に書き込みます。<br>
2.HIDライブラリの格納<br>
 Itsy Bitsyのlibフォルダ以下に[adafruitのHID](https://docs.circuitpython.org/projects/hid/en/latest/)ライブラリを格納します。<br>
3.code.pyを格納します。<br>
 Thonnyをつかうと便利です。<br>

### つなぎ方
 Itsy BitsyとPC/Raspberry PIをUSBケーブルで繋ぎます。<br>
 Itsy Bitsyは起動するとLEDが点滅します。<br>

## 制限
 - キーコード全てには対応していませんが、Keymapを修正すれば好きなキーをアサインできます。<br>
 - unix使う時に困るキーは以下のように対応しました。<br>
![キーの置き換え](https://user-images.githubusercontent.com/111331376/189951347-d1f18aec-eae9-4343-bec5-dcef67f46222.png)

## Thanks to
 - [Final build of the Pine A64 TRS-80 Model 100](https://fadsihave.wordpress.com/) TRS改造元祖、キーマップ参考になりました。
 - [SWITCH SCIENCE](https://www.switch-science.com/) 楽しい部品が安く早く手に届くので、大好き。
 - [RaspberryPiクックブック](https://www.denshi.club/parts/) 説明分かりやすくて助かりました。

## ライセンス
 [Apache License v2.0](http://www.apache.org/licenses/LICENSE-2.0)に基づいてご利用ください。ご連絡は[layer8](https://twitter.com/layer812)までお願いします。