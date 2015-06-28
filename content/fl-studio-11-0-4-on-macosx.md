Title: FL Studio 11.0.4 on MacOSX
Date: 2014-03-21 00:50
Author: admin
Category: music
Tags: crossover, FL, mac
Slug: fl-studio-11-0-4-on-macosx

前に[この記事書いた時に](http://blog.ca54makske.com/blog/2014/01/09/il-remote%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F/)IL-remoteのためにFLをアップデート(FL
Studio 11.0.4)してたんですが、  
このアップデートのお陰で、MacBookにインストールしている[FL Studio MacOS
X
Beta](http://www.image-line.com/documents/news.php?entry_id=1378290309)(これ書いてる時点では最新版が11.0.2)でプロジェクトファイルを開けなくなってしまいました。

~~**そもそも0.2っつーマイナーバージョンアップでプロジェクトファイルの互換性失うのってどうなんだよ？**~~  

・・・という話は置いておいて、MacBookに最新版のFLをちゃんと入れられたのでやり方を簡単に書いておきます。

必要なもの
----------

-   FL Studio 11.0.4 インストーラ
-   FLRegkey.Reg (ユーザーページで発行)
-   [CrossOver](http://www.codeweavers.com/products/)

公式で配布されているベータ版のFL Studio
MacOSXの実体はOSXネイティブなアプリではなくて  
CrossOverでラッピングしたものになってます。  
なので今回はCrossOverを使って自力でFLをインストールします

インストール手順
----------------

・・・といってもそんなに書くこともあまり無かったりしますが  
手順としてはこう

1.  CrossOverをインストール
2.  FLのインストーラを起動(CrossOverが立ち上がってインストーラを起動しようとする)
3.  FLをインストールしたボトル(CrossOverの仮想マシン?)のレジストリエディタを起動してFLRegKey.Regを登録

わかりにくいやつ
----------------

まず最初に躓いたのがインストーラで

[flickr id="13289019103" thumbnail="small\_320" overlay="true"
size="original" group="" align="none"]

途中で真っ白な画面があるんですが、何かを選択しなければならなかったようで先に進みません。  

これを回避するには**この前の画面からウィンドウのフォーカスが変わらないように[Next]を押**さなければならないです。

ちなみに、これなんの選択画面だったかというと  
[flickr id="13289386705" thumbnail="small\_320" overlay="true"
size="original" group="" align="none"]  

上のバナーにもありますがあの悪名高きhaoでした。汚いさすがhao123きたない。

次に躓いたのがレジストリの登録ですが、  

[このへん](http://d.hatena.ne.jp/Kei_9/20060921/1158803907)見て分かったんですが  

CrossOverで作った各ボトルにはちゃんとレジストリエディタが標準でインストールされるようになってます  
(各ボトルのdir/drive\_c/windows/regedit.exe)  
これを起動して、レジストリの取り込み→FLRegKey.regを選択すれば登録完了

おわりに
--------

[Image-LineさんがFLのOSXネイティブ対応諦めてるっぽい](http://support.image-line.com/knowledgebase/base.php?id=55&ans=114)おかげでMacOSX機でFL使うのはちょっと最初がめんどくさいですが、  
自分が使った感じではこのCrossOver環境で十分に使えてると思います。

あと、CrossOver環境における利点も実はあって・・・

**windows用のVSTプラグイン(.dll)をそのまま使える！**

ので、ぼくのようにwindowsでもmacでも同じ作曲環境を作りたい人にとっては  
実はありがたかったりします。
