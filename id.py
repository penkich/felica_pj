#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IDを表示させるだけのテスト

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
