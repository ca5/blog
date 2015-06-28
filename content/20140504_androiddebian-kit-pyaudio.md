Title: Android端末と Debian kitと PyAudio
Date: 2014-05-04 22:30
Author: Ca5
Category: create
Tags: android, debian, PyAudio, python
Slug: androiddebian-kit-pyaudio

家に使ってないAndroid端末があったんで、  
Debian化してpython入れて音出せるかどうか試してみました。  
結論から言うと全然うまくいかないんですが。

対象端末:  
・Galaxy Tab(SC-01C)  
→ 中古で購入した時点ですでに JK2 FroyoのRoot化ROMが焼いてあったっぽい  
　→ バージョンは2.2 Froyo

Debianのinstall
---------------

この記事を参考に、Debian kitを使ってDebianを入れます  
[http://gihyo.jp/admin/serial/01/ubuntu-recipe/0256?page=3  
](http://gihyo.jp/admin/serial/01/ubuntu-recipe/0256?page=3)  
Debian入れると言っても完全にOS焼きなおすんじゃなくて、  
chrootな環境が出来上がるだけってもののようです。

基本的にはAndroid端末にDebian
kitと何か端末シミュレータをいれて上記の記事にそってインストールしていっただけ。  

OSが入って、debコマンドで環境起動したら、その後の作業が楽になるようにssh
serverを入れておきます

[bash]  
apt-get install openssh-server  
[/bash]

その後の作業は外部からこの端末にsshして色々いじっていく

pythonとかpyenvとか
-------------------

pyenv入れる前に以下をapt-get installしておく  
参考：[https://github.com/yyuu/pyenv/wiki/Common-build-problems  
](https://github.com/yyuu/pyenv/wiki/Common-build-problems)  
[bash]  
git  
make  
build-essential  
libssl-dev  
zlib1g-dev  
libbz2-dev  
libreadline-dev  
libsqlite3-dev  
wget  
curl  
llvm  
[/bash]

pyenvをレポジトリのREADMEに沿ってインストール  
<https://github.com/yyuu/pyenv>

pythonのインストールと環境設定  
[bash]  
pyenv install 2.7.6  
pyenv local 2.7.6  
[/bash]

PyAudioとportaudio
------------------

PyAudioはportaudioのpython wrapper版  
http://people.csail.mit.edu/hubert/pyaudio/

portaudioは各OSのaudio apiをwrapしたAPI  
http://portaudio.com/docs/v19-doxydocs/api\_overview.html

PyAudio入れる前に、aptでportaudio v19を入れておく  
[bash]  
portaudio19-dev  
libportaudio-dev  
[/bash]

PyAudioのインストール  
[bash]  
pip install --allow-external PyAudio --allow-unverified PyAudio
PyAudio  
[/bash]  
この長ったらしいオプション指定なんとかならんのか。。

動作チェック
------------

PyAudio本家のサンプルをそのままコピって動かしてみる  
http://people.csail.mit.edu/hubert/pyaudio/

[python]  
"""PyAudio Example: Play a WAVE file."""

import pyaudio  
import wave  
import sys

CHUNK = 1024

if len(sys.argv) \< 2:  
print("Plays a wave file.\\n\\nUsage: %s filename.wav" % sys.argv[0])  
sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get\_format\_from\_width(wf.getsampwidth()),  
channels=wf.getnchannels(),  
rate=wf.getframerate(),  
output=True)

data = wf.readframes(CHUNK)

while data != '':  
stream.write(data)  
data = wf.readframes(CHUNK)

stream.stop\_stream()  
stream.close()

p.terminate()  
[/python]

実行  
[bash]  
\$ python ./soundtest.py amen.wav  
Traceback (most recent call last):  
File "./soundtest.py", line 22, in \<module\>  
output=True)  
File
"/home/ca5/.pyenv/versions/2.7.6/lib/python2.7/site-packages/pyaudio.py",
line 747, in open  
stream = Stream(self, \*args, \*\*kwargs)  
File
"/home/ca5/.pyenv/versions/2.7.6/lib/python2.7/site-packages/pyaudio.py",
line 442, in \_\_init\_\_  
self.\_stream = pa.open(\*\*arguments)  
IOError: [Errno Invalid output device (no default output
device)] -9996  
[/bash]

わー　デバイスが認識されてねー

別途、portaudioのサンプルも動かしてみたんですがやっぱりダメ  
portaudioが使うaudioAPIが対応してないと思われる。

Android側のバージョンあげたらportaudioが使えるってどこかの記事で見かけたんで  
次はOS上げて再チャレンジか

参考
----

http://stackoverflow.com/questions/5921947/pyaudio-installation-error-command-gcc-failed-with-exit-status-1

ここ見るとportaudioでOpenSL使えそう？  
http://www.gizmodo.jp/2012/07/android\_osjelly\_bean.html

http://stackoverflow.com/questions/4672155/pyaudio-ioerror-no-default-input-device-available
