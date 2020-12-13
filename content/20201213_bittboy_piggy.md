Title: Little GP Tracker ON Bittboy
Date: 2020-12-13 23:30
Author: Ca5
Category: create
Tags: chiptune
Slug: lgpt_piggy_on_bittboy

ブラックフライデーセールで [NEW Bittboy](https://retromimi.com/collections/deals/products/new-bittboy)を買って  
[Little GP Tracker (通称piggy tracker)](https://www.littlegptracker.com/index.php) を入れて作曲環境を整えるまでの記録です。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">激安ポータブル作曲環境が仕上がってきた <a href="https://t.co/NXxSSnWwKa">pic.twitter.com/NXxSSnWwKa</a></p>&mdash; かご (@Ca5) <a href="https://twitter.com/Ca5/status/1335965195378647040?ref_src=twsrc%5Etfw">December 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 1. Little GP Tracker の導入

### 1-1. Dingux版バイナリ
Bittboyは Dingux というディストリビューションのLinuxが動くようなんですが、  
いきなり[公式のDLページ])(https://www.littlegptracker.com/download.php)に無くて途方に暮れます。

有志の方がプルリクでBittboyのビルドに対応した修正を出してるんですが、    
まだ現時点(2020/12/13)ではマージもされていないようです。  
修正した方がビルド版を公開してくれているので、  
このバイナリをそのまま使わせていただきます。  

下記のプルリクの下の方にある `gameblabla` さんのコメント  
[https://github.com/Mdashdotdashn/LittleGPTracker/pull/10](https://github.com/Mdashdotdashn/LittleGPTracker/pull/10)

> Here's a binary for the Bittboy/PocketGo :  
> [lgbt_binary_bittboy.zip](https://github.com/Mdashdotdashn/LittleGPTracker/files/3428804/lgbt_binary_bittboy.zip)


### 1-2. サンプルフォルダ
また、バイナリだけだとサンプルも何もなくてちょっと困るので、  
[公式のDLページ](https://www.littlegptracker.com/download.php) から windows版でもOSX版でもいいのでDLしておいて  
その中にこのバイナリを置いて使います。

### 1-3. キーマッピング
Bittboyは他のDinguxが乗る筐体と違ってボタンが少なく、  
いろんな操作が犠牲になってしまっていてそのままでは実は  
メニュー移動すらできずアプリの終了もままならない状態です。

僕が勝手に頑張って作った下記のmapping.xmlをバイナリと同じ階層に置きます

**mapping.xml**
```
<MAPPINGS>
<MAP src="key:0:up" dst="/event/up" />
<MAP src="key:0:down" dst="/event/down" />
<MAP src="key:0:left" dst="/event/left" />
<MAP src="key:0:right" dst="/event/right" />
<MAP src="key:0:left ctrl" dst="/event/a" />
<MAP src="key:0:space" dst="/event/b" />
<MAP src="key:0:right alt" dst="/event/rshoulder" />
<MAP src="key:0:left alt" dst="/event/rshoulder" />
<MAP src="key:0:escape" dst="/event/rshoulder" />
<MAP src="key:0:left shift" dst="/event/lshoulder" />
<MAP src="key:0:return" dst="/event/start" />
</MAPPINGS>
```

これを使うと、

* LボタンがBittboyのTボタン右
* RボタンがBittboyのTボタン左
* 十字キー, start, A, B は刻印通り

に基本なるんですが、  
メニュー移動(R+十字キー)だけはselectボタンになります。

本当は全部Rボタンの操作をselectボタンに寄せればLSDjと操作が一緒になるんですが、  
Bittboyはselect+A(orB) がシステムの音量調整に割り当てられているのでうまくいきません。

いっそpiggyにならって全部T左ボタンに寄せようとも思ったんですが、それだと何故かメニュー移動ができなくなったりして結局これに落ち着いてます。


### 1-4. 最終的なパス構成
Bittboy用のSDカードのmainボリュームの中で、  
こういうパス構成で置ければOKです

```
lgpt/
├── mapping.xml
├── lgpt.elf
├── lgpt10k
├── lgptNew
└── samplelib
```


# 2. PWMノイズ対策
起動中ちょっとイヤホンジャックでノイズを拾っちゃうんですが、   
特に画面のバックライトを落とすと顕著に現れます。

下記の記事を見ると、bittboyの別なバージョン(pocket go)では バックライトのPWMが1000Hz設定されているようで、これを17000くらいにすると聞こえにくくなるとのことでした
https://byteporter.com/pocket-go-pwm-script-install/

NEW bittboyで試すとこれも同じくうまくいったので合わせて行うといいと思います。  
ただしノイズが無くなるというよりは、高周波になって聞こえにくくなるだけってことですね。

# その他
付属のsamplelibで [Osc] のサンプル(例えばsinus.wav) とかを  
`loop mode: osc` で 高めの音出すとすぐ音程狂う気がするんですが。。  
これってlgpt全体の問題なんですかね?