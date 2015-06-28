Title: WebMusicハッカソンに参加してきました #webmusicjp
Date: 2014-09-19 00:11
Author: Ca5
Category: create
Tags: music, webaudio, webmidi
Slug: webmusichackathon

先日、[@fujikky](https://twitter.com/fujikky)と一緒にチームhimakanとして参加したWebMusicハッカソン
\#3で優勝しました！

関連記事:  
<http://miscfeeling.blogspot.jp/2014/09/web-music-3.html?m=1>  
↑当時の発表の様子などが紹介されています

 

作ったもの
----------

<http://himakan.github.io/facetracking-effector/>

起動してカメラの入力を許可すると、頭の位置をトラッキングして音が変化していきます。  
(Chromeでしか動作確認してません)

MIDI機器がつながっている場合、プルダウンでデバイスを選択して連携させることができます。  
(MIDI CCのマッピングはKAOSSPAD3上での挙動を想定しています)

 

WebAudio/Midiの良かったところいろいろ
-------------------------------------

以下、このイベントを機にWebAudioAPIに触れてみて、  
思ったことを色々書いておこうと思います。

 

### 1.簡単にAudioのin/out処理を書くことができる

なんといっても手軽にAudioの入出力処理をかけるのは素晴らしいと思います。  
ファイルの形式とかビットレートとか何も考えずに

-   audio in/out
-   フィルタエフェクト
-   フーリエ変換

が簡単に行えます。

AudioContextを受け渡すことで簡単に連携できるところも使い勝手が良かったです。

### 2.midi in/out

ブラウザからmidi機器を操作できるのは実際動かしてみるとほんとに画期的です！

ただし、現状動くブラウザがかなり限られているようです。

### 3.JavaScriptならではの良さ

HTML + JavaScriptで作品を作ることができるので

-   作品の公開が簡単
-   開発環境 実質0円！
-   公開されているたくさんのライブラリと連携できる

・・・などなどというメリットがあります。

例えば今回頭の位置をトラッキングするのにこれを使いましたが  
<https://github.com/auduno/headtrackr/>

JavaScriptって結構いろんなことができるんですね。。。  
これがあるならあんなにお金のかかるmax/mspとかもいらないような。。。。

 

最後に
------

WebAudio/Midi はまだまだ沢山可能性を秘めているなーと感じました。

そのうち、DAWやPCDJ系のソフトは全部クラウド上に置かれるようになって  
ブラウザが動くデバイスさえあれば  

どこでも作曲やライブなどのパフォーマンスができるような時代になるんだろうなと思います。
