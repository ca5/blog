Title: logbarのRingでkaosspadのコントロール
Date: 2015-02-06 00:34
Author: Ca5
Category: create
Tags: max/msp, Ring
Slug: logbar-ring-kaosspad

[logbarのRing](http://logbar.jp/ring/ja/developer/)面白いんですが、  
まだSDKとかがなくて正直やれることが少ないかなといった印象です。

SDKがなくても最初から、  

1ジェスチャーにつき1httpリクエストを投げられる機能が標準で付いているので  
ある程度色んな物を操作できるんですが、  

エフェクター操作をこれでやろうと思うとどうしてもワンテンポずれた挙動になってしまう。。。

・・・というわけで、ちょっと別な操作法を考えてみました。  

<iframe width="420" height="315" src="https://www.youtube.com/embed/RIszxzo9Zco" frameborder="0" allowfullscreen></iframe>

ジェスチャー入力後、指の上下でエフェクトON/OFFを切り替えています。  

これはRing標準の音量コントロールを無理やり使ってこんな操作を実現しています。

1.  iPhoneで一定の音を出力(今回はtonetableを使いました)
2.  1.の音量をRingで変化させてmax/mspへ入力
3.  max/msp側で音量に応じたmidiメッセージをkaosspadへ送る

かなりシンプルなmax/mspのパッチでこんな操作が一応実現できます。

ただ欲を言うとやっぱりy軸だけじゃなくてx軸も取りたい・・・・  

というわけで、Ringの開発担当の方、SDKのリリース是非是非よろしくお願いしまーす
