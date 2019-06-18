# eel_bootstrap

`async-eel`でデスクトップアプリを作るときの小さなテンプレです。

`asyncio`を使いたいのに`gevent`と同時に使用すると制限が強かったのでフォーク。

とりあえず（オンラインなら）（最低限）VueとBootstrapが使えるようになっています。

## 使い方

Python 3.6 以上必須。3.5では動きません。

```bash
pip install -r requirements.txt
python gui.py
```

## Tips

* Javascript側のエラーは開いたウィンドウを右クリックして「検証」から見れます
* Ctrl(Cmd) + Shift + Rでキャッシュ消去 + リロードができます
* ダイアログによりEventLoopがBlockされます、解決方法は未定です（教えて
* `callback`や`expose`するFunctionは非同期である必要はありません。
