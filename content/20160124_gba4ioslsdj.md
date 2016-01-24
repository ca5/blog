Title: iPhoneでLSDJを動かせた!(セーブも可!)
Date: 2016-01-24 21:00
Author: Ca5
Category: create
Tags: LSDJ,iOS
Slug: gba4ios-lsdj

![LSDJ with GBA4iOS]({filename}/images/20160124/lsdj.jpg)

GBA4iOSというエミュを使ってiPhoneでLSDJを動かすんですが、  
そのままでは無理なので LSDJ用に修正したバージョンのソースをビルドして使います。  
たぶん音質の再現性も初代系のGBに近いと思います。この辺りは後述します。  

## 1.LSDJ対応版GBA4iOSのビルド方法(2016/1/24時点)
ある程度以下がわかっている向けにさっくり書きます

- git
- Objective-C
- CocoaPods
- Xcode7

### 1-1.naorunaoruさんの128kbRAM対応済みソースのDL
ここからソースを取得します  
[https://bitbucket.org/naorunaoru/gba4ios/branch/feature/128k-save](https://bitbucket.org/naorunaoru/gba4ios/branch/feature/128k-save)  

そもそもGBのカートリッジってRAMサイズいろいろあるんですね！  
LSDJは128kb無いとセーブ出来ないけど、元のGBA4iOSが32kb固定なつくりになっているので  
この改変版ソースからのビルドが必要になります。  

参考:   
[http://chipmusic.org/forums/topic/13483/does-lsdj-use-a-nonstandard-type-of-sav-file/](http://chipmusic.org/forums/topic/13483/does-lsdj-use-a-nonstandard-type-of-sav-file/)


### 1-2.pod install
いくつかライブラリ依存があるのでpod installしてから  
GBA4iOS.xcworkspaceを開きます。

### 1-3.Bundle IdentifierとTeamをなおす
Bundle Identifierを元とは違う適当な文字列にして、  
Teamを自分のアカウントにセットし直します。  

### 1-4.Enable Bitcode = Noに
Build Settingで"Enable Bitcode" = No に変更します。

### 1-5.DropboxのSDKのヘッダを参照できるようにする
pod installだけだとうまいことヘッダのパスが想定通りいかないようなので、  
下記を参考にシムリンクを貼ります。  
[http://stackoverflow.com/questions/32969971/dropbox-ios-sdk-dropboxsdk-h-file-not-found](http://stackoverflow.com/questions/32969971/dropbox-ios-sdk-dropboxsdk-h-file-not-found)

※もっと良い方法あれば教えて欲しいです

### 1-6.CrashlyticsのSDKのヘッダを参照できるようにする
1-5.に似てますが今度は参照してるソースの方を書き換えちゃいます。
```
#import <CrashlyticsFramework/Crashlytics.h>
```
となっている箇所を探して全て  
```
#import <CrashlyticsFramework/Crashlytics/Crashlytics.h>
```
と書き換えます。  

※これももっと良い方法あれば教えて欲しいです

### 1-7.ビルド
ここまでやればたぶん問題なくビルドできるはず。

### 1-8.iPhoneDeveloperを信頼
ビルド後、アプリの立ち上げでコケることがあります。  
その時は下記を参考に自分のIDをインストール先iPhoneで信頼設定します。  
[http://qiita.com/FumihikoSHIROYAMA/items/a754f77c41b585c90329]( http://qiita.com/FumihikoSHIROYAMA/items/a754f77c41b585c90329)

以上でLSDJ対応版のGBA4iOSがiPhone上で動かせるはずです！

## 2.GBA4iOSでLSDJで動かしてみて
### 良かったこと
- iPhoneでLSDJを使える！
- Dropbox連携でsavファイルをバックアップできる！

### 微妙なところ
- 今後いつまでも同じやり方でいけるかわからない

今回つかったnaorunaoruさんのソースは、pull requestはされているものの  
本家ブランチへはまだマージされていません。  
pull requestが出されてからかれこれ半年近く経っているんですが  
いつになったらマージしてもらえるんでしょう。。。  
LSDJユーザーのためにも是非対応していただきたいところです。  
[https://bitbucket.org/rileytestut/gba4ios/pull-requests/12/128k-save-support-pulled-from-gambatte/diff](https://bitbucket.org/rileytestut/gba4ios/pull-requests/12/128k-save-support-pulled-from-gambatte/diff)

### 音質について
- 全体的に再現性が高い気がする（小並感
- 特にパン振ったときにプチノイズが乗るところは初代系の音に似てる
- 逆に言うとGBA派+パン振りまくりたい派には微妙かもしれない
- 波形チャンネルの再現も問題なし

この辺り他の方の感想も聞いてみたいところです。  
少なくとも、[Gearboy](https://github.com/drhelius/Gearboy)よりは音質は良かったと思います。  
ご要望 or 気が向いたら音質比較用に何か録音したりしようかなと思います。


## 3.最後に
iOSでLSDJやれるようになったらチップチューンのハードル結構下がると思うんです。  
Xcode7から自分の端末にビルドしたアプリをインストールするのは無料で出来るようになったので、  
これを気にやってみてはいかがでしょうか？  

あと、128kbRAM対応版版のソース公式にマージしてください！頼む！
