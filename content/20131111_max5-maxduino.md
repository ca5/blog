Title: max5  + maxuino + Arduino UNO + OSC の組み合わせに気をつけろ
Date: 2013-11-11 01:18
Author: Ca5
Category: create
Tags: arduino, max/msp, osc
Slug: max5-maxduino

arduinoに手を出し始めました  
正直まだブレッドボードの正しい使い方すら怪しいです

[flickr id="10780096903" thumbnail="small\_320" overlay="true"
size="large" group="" align="none"]

とりあえず今までmax/mspで作ってきたライブセットと連動させることを当面の目標にしているので、  

[maxuino](http://www.maxuino.org)を使ってとりあえずLEDをPWDモードで明るさ変更して光らせるってとこまでやってみました。

maxuino使ってみて気づいたんですが、  
max5で使ってると最新版のb016で
maxuino-gui経由のOSC入力がうまくいかないです。  
中身見てみたら OSC-route
オブジェクトがひとつもなくてどうなってるんだ？と思ったら  
max6以降は標準のrouteオブジェクトでOSC対応してるんですね。。。

かといって、バージョン014を使おうとすると  
今度はArduino UNO用のピンセットにあったモードが無いようで  
これでもまたうまくいかず。

max5 + maxuino + Android UNOな環境では  
自力でOSC-route使ってメッセージを分けるか、  
OSC使うの諦めるしかないようですね。

まあ、maxuinoが全く使えないというわけではないので  
そんなにクリティカルな話でもなさそうです。

参考:  
<http://www.maxuino.org/getting-started>  
<http://yoppa.org/ssaw12/3759.html>
