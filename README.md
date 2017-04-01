# selfnotify
Send notification from python to you through your telegram bot

# Installation
Clone branch & install package
```
git clone -b basic-implementation git@github.com:menshikh-iv/selfnotify.git
pip install selfnotify/
```

If you import lib `python -c "import selfnotify"`, you'll get an error

```python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/ivan/selfnotify/selfnotify/__init__.py", line 48, in <module>
    _ENVIRON_CHAT_ID_KEY))
RuntimeError: Please, fill config file /home/ivan/.selfnotify/selfnotify.json of ENV vars: TELENOTIFY_TOKEN and TELENOTIFY_CHAT_ID
```
Because you need `token` and `chat_id`.

1. Go to [@BotFather](https://telegram.me/botfather), create bot and write `token` to `~/.selfnotify/selfnotify.json` (or use env variable `TELENOTIFY_TOKEN`)
![BotFather dialog](https://cdn-images-1.medium.com/max/800/1*xbpFyoKNP1jNBLlBguTS_g.png)
2. Go to [@get_id_bot](https://telegram.me/get_id_bot), get your  `chat_id` and write it to `~/.selfnotify/selfnotify.json` (or use env variable `TELENOTIFY_CHAT_ID`)

Now, you can use library

```python
from selfnotify import Notifier
from time import sleep

with Notifier() as nf: # send 'Start' to telegram
    print("Run process")
    sleep(5)
    nf.notify("some important message about progress") # send this message too
    sleep(3)
    print("Complete! Yay!") # send 'End' to telegram
```
