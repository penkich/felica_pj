#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IDを表示させるだけのテスト by penkich 2016-08-28
# nfcpy を下記を参考にインストールする（root権限で実行する必要あるが、piユーザでもできるようにしておく）。
# https://nfcpy.readthedocs.io/en/latest/
# 

import nfc
import re
 
def connected(tag):
  # タグのIDなどを出力する
  #  print tag
    a = '%s' % tag
    print re.findall("ID=([0-9A-F]*)",a)[0]
# タッチ時のハンドラを設定して待機する
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
