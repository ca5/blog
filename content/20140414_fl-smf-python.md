Title: FLとSMFとpython (準備編)
Date: 2014-04-14 01:11
Author: admin
Category: 未分類
Tags: FL, midi, python
Slug: fl-smf-python

FLで作った曲のBPMに合わせてごにょごにょする処理を自前で作りたくて色々試そうとしてます。

とりあえず思いついた方法が

-   FLで曲のwavとmidiを書き出す
-   wavとmidiをpythonのスクリプトで読み込んでごにょごにょ

というわけでまず準備編

1. FLでmidiを吐き出す
---------------------

FLでこんなプロジェクトを用意

<a href="http://firestorage.jp/download/12b13e190a604e9dcd90ff34cb7d4287f95418e5">bpmtest.zip

</a>

[flickr id="13820505455" thumbnail="small\_320" overlay="true"
size="original" group="" align="none"]

2小節分のドラムループを4回ループ。3小節目からBPM変更のパターンが入って、5-6小節目中でBPMを140→54.013へ一気に下げる。

これのmidiを吐き出すには、まず

TOOLS \> Macros \> prepare for export

でmidiファイル出力に必要な適合化処理を実行する必要があります。

(これやらないと空のmidiファイルしか出来ない

で、こんなmidiファイルが出来る

[bpmtest.mid](http://firestorage.jp/download/3fbc6a9cda4e58488abcfa6f0659aa980742f540)

2. midiファイルをpythonのスクリプトで解析する
---------------------------------------------

midiの解析にpython-midiを使う

<a href="https://github.com/vishnubob/python-midi">https://github.com/vishnubob/python-midi

</a>

pipのindexに入ってるみたいですが、

自分の環境だとうまくインストールできなかったのでgitのREADME通りの手順でソースからインストール。

すると mididump.py
というサンプルスクリプトも一緒にインストールされるので試してみる。

[bash]  
\$ mididump.py ./bpmtest.mid | less  
midi.Pattern(format=1, resolution=96, tracks=\\  
[midi.Track(\\  
[midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),  
midi.EndOfTrackEvent(tick=0, data=[])]),  
midi.Track(\\  
[midi.SetTempoEvent(tick=0, data=[16, 243, 60]),  
midi.SetTempoEvent(tick=0, data=[6, 138, 27]),  
midi.SetTempoEvent(tick=768, data=[6, 138, 27]),  
midi.SetTempoEvent(tick=768, data=[6, 254, 136]),  
midi.SetTempoEvent(tick=24, data=[7, 111, 252]),  
midi.SetTempoEvent(tick=24, data=[7, 211, 193]),  
midi.SetTempoEvent(tick=24, data=[8, 14, 176]),  
midi.SetTempoEvent(tick=24, data=[8, 109, 233]),  
midi.SetTempoEvent(tick=24, data=[8, 190, 72]),  
midi.SetTempoEvent(tick=24, data=[9, 73, 112]),  
midi.SetTempoEvent(tick=24, data=[9, 215, 214]),  
midi.SetTempoEvent(tick=24, data=[10, 103, 106]),  
midi.SetTempoEvent(tick=24, data=[10, 226, 237]),  
midi.SetTempoEvent(tick=24, data=[11, 126, 229]),  
midi.SetTempoEvent(tick=24, data=[12, 22, 109]),  
midi.SetTempoEvent(tick=24, data=[12, 241, 204]),  
midi.SetTempoEvent(tick=24, data=[13, 208, 171]),  
midi.SetTempoEvent(tick=24, data=[14, 207, 174]),  
midi.SetTempoEvent(tick=24, data=[16, 30, 101]),  
midi.SetTempoEvent(tick=24, data=[16, 243, 60]),  
midi.EndOfTrackEvent(tick=0, data=[])]),  
midi.Track(\\  
[midi.TrackNameEvent(tick=0, text='Sampler (MIDI)', data=[83, 97, 109,
112, 108, 101, 114, 32, 40, 77, 73, 68, 73, 41]),  
midi.ControlChangeEvent(tick=0, channel=0, data=[10, 64]),  
midi.ControlChangeEvent(tick=0, channel=0, data=[7, 100]),  
midi.PitchWheelEvent(tick=0, channel=0, data=[0, 64]),  
:  
:  
[/bash]

これだけだとあんまり良くわからないので

こんなサイトを参考に<http://www2s.biglobe.ne.jp/~yyagi/material/smfspec.html>

以下引用

> SMFの実際
>
> テンポ120で、四分音符でドレ、全音符でミを鳴らすSMF。
>
> ランニングステータスが多用されていることに注意。
> また、ランニングステータスの効果を高めるために、 ノートオフとして 9n
> kk 00 (ベロシティゼロでノートオン) を使用している。
>
> 000000 4D 54 68 64 00 00 00 06 00 01 00 02 00 30 4D 54 /
> MThd.........0MT
>
> 000010 72 6B 00 00 00 0B 00 FF 51 03 07 A1 20 00 FF 2F /
> rk......Q....../
>
> 000020 00 4D 54 72 6B 00 00 00 18 00 90 3C 7F 30 3C 00 /
> .MTrk.....・0.0\>..@..0@.../
>
> 000040 00 / .
>
> ヘッダ
>
> 4D 54 68 64 "MThd"
>
> 00 00 00 06 ブロック長(6)
>
> 00 01 フォーマット(1)
>
> 00 02 トラック数(2)
>
> 00 30 四分音符の分解能(0x30=48)
>
> トラック1のデータ (Conductor Track)
>
> 4D 54 72 6B "MTrk"
>
> 00 00 00 0B ブロック長(0x0B=11)
>
> 00 FF 51 03 07 A1 20 テンポ(120)
>
> 00 FF 2F 00 トラックエンド
>
> トラック2のデータ (演奏トラックその1)
>
> 4D 54 72 6B "MTrk"
>
> 00 00 00 18 ブロック長(0x18=24)
>
> 00 90 3C 7F ベロシティ127でノート3Cをノートオン
>
> 30 3C 00 48tick後、ノート3Cをノートオフ
>
> 00 3E 7F 直後に、ベロシティ127でノート3Eをノートオン
>
> 30 3E 00 48tick後、ノート3Eをノートオフ
>
> 00 40 7F 直後に、ベロシティ127でノート40をノートオン
>
> 81 40 40 00 192tick後、ノート40をノートオフ
>
> 00 FF 2F 00 トラックエンド

> FF 51 03 tttttt : テンポ設定 (単位は μsec / MIDI 四分音符)
>
> このイベントでテンポ変更を指示する。
>
> tttttt (3byte) には、四分音符の長さをマイクロ秒 (μsec)
> で表したものを格納する。
>
> 例えば、BPM=120 (1分あたり四分音符が120個)の場合、 四分音符の長さは 60
> x 106 / 120 = 500,000 (μsec)。
> これを16進にすると0x07A120。従って、メタイベントは
>
> FF 51 03 07 A1 20
>
> となる。

/引用終わり

・・・ということなのでSetTempoEventの部分をみてみると  
[bash][midi.SetTempoEvent(tick=0, data=[16, 243, 60]),  
midi.SetTempoEvent(tick=0, data=[6, 138, 27]),  
midi.SetTempoEvent(tick=768, data=[6, 138, 27]),  
midi.SetTempoEvent(tick=768, data=[6, 254, 136]),  
midi.SetTempoEvent(tick=24, data=[7, 111, 252]),  
midi.SetTempoEvent(tick=24, data=[7, 211, 193]),  
midi.SetTempoEvent(tick=24, data=[8, 14, 176]),  
midi.SetTempoEvent(tick=24, data=[8, 109, 233]),  
midi.SetTempoEvent(tick=24, data=[8, 190, 72]),  
midi.SetTempoEvent(tick=24, data=[9, 73, 112]),  
midi.SetTempoEvent(tick=24, data=[9, 215, 214]),  
midi.SetTempoEvent(tick=24, data=[10, 103, 106]),  
midi.SetTempoEvent(tick=24, data=[10, 226, 237]),  
midi.SetTempoEvent(tick=24, data=[11, 126, 229]),  
midi.SetTempoEvent(tick=24, data=[12, 22, 109]),  
midi.SetTempoEvent(tick=24, data=[12, 241, 204]),  
midi.SetTempoEvent(tick=24, data=[13, 208, 171]),  
midi.SetTempoEvent(tick=24, data=[14, 207, 174]),  
midi.SetTempoEvent(tick=24, data=[16, 30, 101]),  
midi.SetTempoEvent(tick=24, data=[16, 243, 60]),  
midi.EndOfTrackEvent(tick=0, data=[])]),[/bash]

BPMはdataの部分の数値を3byteの数値と見れば良い  
data=[6, 138, 27]の場合は  
[bash]  
27 + 256\^1 \* 138 + 256\^2 \* 6 = 428571(μsec)→4分音符の長さ  
BPM = 60000000 / 428571 = 140.00014000014 ≒ 140  
[/bash]  
となる

1.
BPMを54.012に設定(プロジェクト最後のBPMをとりあえず最初につけてしまっている？)  
2. BPMを140に設定 (1.からtick=0差なのですぐにこのBPMが適用される)  
3. 2小節後(tick=96\*4\*2=768)にBPMを140に設定  
4. 2小節後にBPMを130.896に設定  
5. 以下16分音符ごとの間隔でBPMを54.012へ下げていく

となっているのがわかりますね。  
あとはこれを元にごにょごにょやるだけ。  
気が向いたら続きを書きます。
