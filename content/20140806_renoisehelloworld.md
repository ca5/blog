Title: Renoise+Luaでhelloworld
Date: 2014-08-06 02:07
Author: Ca5
Category: create
Tags: Lua, renoise
Slug: renoisehelloworld

Renoiseの拡張機能をLuaで書けるらしいので始めてみました

準備編
------

1.  まずrenoise DEMO版をDL+インストール  
    <http://www.renoise.com/>
2.  次にスターターパックの最新版をDLして解凍しておく  

    (renoiseインストールした時も同じようなのが勝手に入るんですが、こっちのほうがサンプルが多かった)  
    <https://code.google.com/p/xrnx/>
3.  起動オプションをつけてrenoiseを起動  

    スターターパックのページにも書いてありますが、"--scripting-dev"オプションを付けて起動します。  
    自分はmac版を使ってるので、Automaterで起動スクリプトを準備しました。  
    [![スクリーンショット 2014-08-06
    1.16.50](http://farm6.staticflickr.com/5566/14650385269_f064e32339_n.jpg "スクリーンショット 2014-08-06 1.16.50")](http://farm6.staticflickr.com/5566/14650385269_f064e32339_n.jpg "スクリーンショット 2014-08-06 1.16.50")  
    Windowsの場合は多分ショートカット作って起動コマンドいじればいいはず
4.  configの変更  
    "Help" -\> "Show Preferences
    Folder..."で設定ファイルが入ったディレクトリを開き、  
    config.xmlのShowScriptingDevelopmentToolsプロパティを  
    false→trueに変更
5.  Toolsを開く  
    4.でconfigを変更するとメニューに"Tools"が増える  
    Tools -\> <span style="color: #000000;">"Scripting Console &
    Editor" で、ようやくスクリプトエディタを起動することが出来ます  
   </span>

実行編
------

スクリプトエディタで"File"-\>"New"  
新規にhelloworld.luaなんて名前でファイルを保存。

[bash]  
renoise.app():show\_message("はろーわーるど")  
[/bash]

右下のexecuteをクリックすると  
[![スクリーンショット 2014-08-06
2.05.12](http://farm4.staticflickr.com/3904/14650675130_66e84b6eb9_n.jpg "スクリーンショット 2014-08-06 2.05.12")](http://farm4.staticflickr.com/3904/14650675130_66e84b6eb9_n.jpg "スクリーンショット 2014-08-06 2.05.12")

こんな風にダイアログボックスを出すことが出来ました。
