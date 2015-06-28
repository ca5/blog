Title: 【arduino】距離センサとKAOSSPAD連動させてみた 
Date: 2013-11-26 01:36
Author: Ca5
Category: create
Tags: arduino, max/msp, midi
Slug: arduino-kaosspad

arduino実験  
説明するより動画見たほうが早いっす  

<iframe width="420" height="315" src="//www.youtube.com/embed/p5obKtVHaRE" frameborder="0" allowfullscreen></iframe>

距離センサの値をmax/mspで受け取って、midiに変換してKAOSSPADに投げてます。

今回ネットで調べて情報が多くかつ扱いも簡単そうなシャープの2Y0A21YKって距離センサーを使ってみました。  
<http://akizukidenshi.com/catalog/g/gI-02551/>

距離が離れてくるとどうもノイズと区別できなくなってしまうようで、値がふらついてしまいます。  

[ここのブログ](http://blog.pineapple.cc/post/50115809244/gp2y0a21yk-100uf)のように電解コンデンサを挟んでやるといいらしいんですが、  

あいにく手元にそんな部品ないんでmax側でソフトウェア的に制御できないかなーといろいろ試したんですが  
今のところうまくいってないです。  
おとなしく電解コンデンサ買いに行こうかな。
