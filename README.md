# selfnotify
Send notification from python to you through your telegram bot

# Installation
Clone branch & install package
```
git clone -b basic-implementation git@github.com:menshikh-iv/selfnotify.git
pip install --user selfnotify/
```

If you import selfnotify, you'll get an error
```
python -c "import selfnotify"

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "selfnotify/__init__.py", line 21, in <module>
    assert cfg['token'], 'You should write bot `token` to {}'.format(_config_path)
AssertionError: You should write bot `token` to ~/.selfnotify/selfnotify.json
```
Because you need `token` and `chat_id`.

1. Go to [@BotFather](https://telegram.me/botfather), create bot and write `token` to `~/.selfnotify/selfnotify.json`

![BotFather dialog](https://cdn-images-1.medium.com/max/800/1*xbpFyoKNP1jNBLlBguTS_g.png)

2. Go to [@get_id_bot](https://telegram.me/get_id_bot), get your  `chat_id` and write it to `~/.selfnotify/selfnotify.json`

Now, you can use library

```
from selfnotify import Notifier
from time import sleep

with Notifier() as nf: # send 'Start' to telegram
    print("Run process")
    sleep(5)
    nf.notify("some important message about progress") # send this message too
    sleep(3)
    print("Complete! Yay!") # send 'End' to telegram
```
