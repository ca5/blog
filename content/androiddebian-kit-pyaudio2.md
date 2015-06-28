Title: Android端末と Debian kitと PyAudio(2)
Date: 2014-05-11 22:00
Author: admin
Category: music
Tags: android, debian, linux, PyAudio, ubuntu
Slug: androiddebian-kit-pyaudio2

[前回](http://blog.ca54makske.com/blog/2014/05/04/androiddebian-kit-pyaudio/)の続き

ドコかの記事で、AndroidのOSをバージョンアップさせるとオーディオのドライバが変わるって記事を見かけたのと、  

linux-on-androidプロジェクトでは[オーディオ鳴ってるdemo](https://www.youtube.com/watch?v=3_AiWoTjO78)があったりするんでこれらを導入してみる

1.AndroidOSアップデート
-----------------------

初代GalaxyTabは公式では2.3.3までしかアップデート出来ないので、  
CyanogenModというROMを焼いちゃいます。

手順まとめるのめんどくさいから参考にしたサイトだけメモ

### 1-1. 2.3.3のカスタムROMにする

Cyanogenmod入れる前にまずは2.3.3のカスタムROMを焼く

参考:  

[http://paso-kon-seikatsu.cocolog-nifty.com/blog/2011/07/galaxy-tabgin-1.html  
](http://paso-kon-seikatsu.cocolog-nifty.com/blog/2011/07/galaxy-tabgin-1.html)

romがリンク切れでなかなか見つからなかったけどここにあった  

[http://www.ersinkoc.com/galaxy-tab-icin-android-2-3-3-gingerbread-kurmak-ve-root-yapmak/  
](http://www.ersinkoc.com/galaxy-tab-icin-android-2-3-3-gingerbread-kurmak-ve-root-yapmak/)

### 1-2. CyanogenModいれる

CyanogenModを導入。CM10まで上げていくとバージョンが4.1まで上がる

参考:  
[http://cielsomer.blog.fc2.com/blog-entry-79.html  
](http://cielsomer.blog.fc2.com/blog-entry-79.html)[](</a>http://cielsomer.blog.fc2.com/blog-entry-175.html)http://cielsomer.blog.fc2.com/blog-entry-175.html  
</a>

これで古いGalaxyTabが最新のOSで遊べるようになった！  
・・・けど本題はここから

2. Debian kit + PyAudio
-----------------------

前回の記事と同じくDebian kitとPyAudioを入れてみた  
・・・が結局音はならない。  
やっぱりPortAudioがちゃんとデバイス認識してくれてない

### 3. Complete Linux Installer

そこで今度試すのが、Complete Linux Installer  
<http://linuxonandroid.org/>

これもDebian kit同様インストールは簡単。  

<https://play.google.com/store/apps/details?id=com.zpwebsites.linuxonandroid>  

ここからアプリをインストールし、中の説明通りにOSをインストールしていく。

インストールしたのは Ubuntu13.04のcoreパッケージ  
(smallやlargeだと常駐するプロセス多すぎて重かった)

ここへPyAudioを導入  
・・・しかし結局音はならず。。。

これ以上がんばるくらいなら素直にAndroidのアプリ作ったほうが早そうなんであきらめます
