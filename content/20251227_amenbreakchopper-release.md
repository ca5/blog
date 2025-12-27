Title: AmenBreakChopperをリリースしました
Date: 2025-12-27 10:00
Author: Ca5
Category: release
Tags: amenbreak, breakcore, vst, juce
Slug: amenbreakchopper-release

### AmenBreakChopper

今年からライブで使うようになった、自作のオーディオプラグイン「AmenBreakChopper」をリリースしました。  
入力されたオーディオをBPMに同期したディレイでビートチョップするためのエフェクトです。  
去年まで使っていたMax for Liveのパッチを元に、iPhoneやスタンドアロンアプリでも使えるようにJUCEで再実装したものとなります。

デモ動画:
<iframe width="560" height="315" src="https://www.youtube.com/embed/VpYfyNo0POY?si=ozkrlGao4mJvfBr2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[AppStore (何気に初デビューです)](https://apps.apple.com/jp/app/amenbreakchopper/id6751303065)

[ドキュメント](https://ca5.github.io/AmenBreakChopper_doc/)

プラグイン上は現状は設定とモニタリング用のシンプルなUIしかなく、  
実際に使うにはドキュメント記載のとおりにMIDIノートの送受信, CCの送信をする外部MIDIコントローラが必要です。  
CCはプラグイン側で変更可能ですが、MIDIノートは固定です。  

iOSのAUv3/Standalone版に加え、  
MacOS/Windowsで使う想定のVST3版がありますが、  
VST3版はどう公開しようかまだ考えられてないです。

おすすめの公開方法とかあったら教えて下さい。