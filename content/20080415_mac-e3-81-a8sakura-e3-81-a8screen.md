Title: macとsakuraとscreen
Date: 2008-04-15 23:50
Author: Ca5
Category: create
Slug: macとsakuraとscreen

ようやくmacのターミナルからsakuraにログインしてscreen上で日本語打てるようになりましたメモ

<!--more-->  
•ターミナルの設定  
ターミナルの宣言方法：xterm-color (ls で多色表示にするため)  
文字エンコーディング：EUC  
※起動時にLANG環境変数を設定　は　**はずす**

•bashrcの設定

    alias screen='~/bin/screen-4.0.3/screen' #単にscreenのインストール先を指定
    export CLICOLOR=1 
    export TERM=xterm-color #この2行でカラー表示
    export LANG=ja_JP.eucJP


    •screenrcの設定（いろいろ追加してどれがどういう意味かうろ覚え）
    helltitle "$ |bash"
    hardstatus alwayslastline "%y/%m/%d(%D) [%02c]: %-w%{=b bw}%n %t%{-}%+w"
    bind s
    bind ^U encoding utf8
    bind ^E encoding EUC
    bind ^S encoding SJIS
    escape ^Zz    # Ctrl + z
    defencoding EUC
    encoding EUC
    termcap  facit|vt100|xterm LP:G0
    terminfo facit|vt100|xterm LP:G0

    あとは、普通にログインすれば日本語が打てる、と。
    screen起動してもおk
