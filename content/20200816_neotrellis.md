Title: NeoTrellisで遊ぶ
Date: 2020-08-16 19:00
Author: Ca5
Category: release
Tags: chiptune,chipbreak
Slug: neotrellis

my new gear... が増えたので  
備忘録的に久々にブログにまとめました

[https://www.adafruit.com/product/3938](https://www.adafruit.com/product/3938)  
最近教えてもらった NeoTrellis が結構いけてそうだったので衝動買いしてしまいました。  
あまり正体はよくわかってないんですが、最初からボタンやらイヤホンジャックが付いてるTeensy互換ボード、ってところでしょうか?  
以下使ってみたメモ

## マニュアル
まずここがこのキットのマニュアル全てっぽいです  
最初ここ見てなくて色々つまずいた  
[https://learn.adafruit.com/adafruit-neotrellis-m4/overview](https://learn.adafruit.com/adafruit-neotrellis-m4/overview)  


## 組み立て
全部ここに書いてます。  
[https://learn.adafruit.com/adafruit-neotrellis-m4/assembly](https://learn.adafruit.com/adafruit-neotrellis-m4/assembly)  
・・・が、ネジは裏から入れるのがおすすめです。  
上から入れると、裏に貼るゴムの高さが足りなくて滑り止めになってくれませんでした。  
自分が頼んだときの部品の問題かもしれないですが。

## ブートローダーの更新
ここのとおりに進めます  
[https://learn.adafruit.com/adafruit-neotrellis-m4/update-the-uf2-bootloader](https://learn.adafruit.com/adafruit-neotrellis-m4/update-the-uf2-bootloader)

ブートローダー自体はここからDL  
[https://circuitpython.org/board/trellis_m4_express/](https://circuitpython.org/board/trellis_m4_express/) 

## ボードマネージャ
[https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/using-with-arduino-ide](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/using-with-arduino-ide)  

- Arduino SAMD Boards
- Adafruit SAMD Boards

の2つを入れる必要があるようです。  
下の方だけでいいのかと思ってた。

## サンプルプログラム(SamplePlayer)のインストール
サンプルプログラムののSamplePlayer... ってややこしいですね。  

本家サイト  
[https://www.adafruit.com/product/3938](https://www.adafruit.com/product/3938)   

本家サイトにはリンクが一つだけあって、  
リンク先はgithubでフォークされたレポジトリが一つ。  
[https://github.com/adafruit/Audio](https://github.com/adafruit/Audio)  

README.mdの一番最後に
```
To install, use the Arduino Library Manager
and search for 'Audio - Adafruit Fork' and install the library
```

と書いてあるんで、  
Arduinoを開いて
`ライブラリマネージャー -> 検索フォームに'Audio - Adafruit Fork'と入れてインストール`

  
・・・という流れでインストールすればOK  
別なプロジェクトでTeensy触っててよかった。  
そっちの話は別な記事で書きます。

ここまで行ったら、  
`スケッチ例 -> Audio - Adafruit Fork -> SamplePlayer`  
でサンプルプログラムを呼び出して書き込み ...

... ではライブラリが足りなくて、  
追加で下記のライブラリを入れました。

- Adafruit Keypad
- Adafruit DMA neopixel library

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">やっとライブラリのサンプルプログラムが動いた <a href="https://t.co/4FswpBSM6C">pic.twitter.com/4FswpBSM6C</a></p>&mdash; かご (@Ca5) <a href="https://twitter.com/Ca5/status/1295006836744048641?ref_src=twsrc%5Etfw">August 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

で一応音がちゃんと出るんですが、  
ボタンが光らないんですよね。。。  
これは NeopixelっていうLEDリボンを外付けしたときに光らせるものだったのかな。。互換性があるのかと思ったが。。  

もうちょっと色々いじってみます。