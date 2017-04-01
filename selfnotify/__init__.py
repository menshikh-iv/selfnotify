from __future__ import absolute_import
import json
import os

__version__ = '0.1'
_config_fn = 'selfnotify.json'

_ENVIRON_TOKEN_KEY = 'TELENOTIFY_TOKEN'
_ENVIRON_CHAT_ID_KEY = 'TELENOTIFY_CHAT_ID'

_user_dir = os.path.expanduser('~')
_selfnotify_dir = os.path.join(_user_dir, '.selfnotify')
if not os.path.exists(_selfnotify_dir):
    os.makedirs(_selfnotify_dir)

_config_path = os.path.join(_selfnotify_dir, _config_fn)

TOKEN = os.environ.get(_ENVIRON_TOKEN_KEY, None)
CHAT_ID = os.environ.get(_ENVIRON_CHAT_ID_KEY, None)

try:
    CHAT_ID = int(CHAT_ID)
except ValueError:
    CHAT_ID = None


if (CHAT_ID is None or TOKEN is None) and os.path.exists(_config_path):
    with open(_config_path) as infile:
        cfg = json.load(infile)

    if TOKEN is None:
        assert 'token' in cfg, 'config %s should contain %s field' % (_config_path, 'token')
        TOKEN = cfg['token']

    if CHAT_ID is None:
        assert 'chat_id' in cfg, 'config %s should contain %s field' % (_config_path, 'chat_id')
        CHAT_ID = cfg['chat_id']

if (CHAT_ID is None or TOKEN is None) and not os.path.exists(_config_path):
    cfg = {'token': None,
           'chat_id': None}

    with open(_config_path, 'w') as outfile:
        outfile.write(json.dumps(cfg))

    raise RuntimeError('Please, fill config file {} of ENV vars: {} and {}'.format(_config_path,
                                                                                   _ENVIRON_TOKEN_KEY,
                                                                                   _ENVIRON_CHAT_ID_KEY))

assert TOKEN, 'You should write bot `token` to {} or set ENV {}'.format(_config_path, _ENVIRON_TOKEN_KEY)
assert len(TOKEN) > 0, 'You should write bot `token` to {} or set ENV {}'.format(_config_path, _ENVIRON_TOKEN_KEY)
assert CHAT_ID, 'You should write `chat_id` to {} or set ENV {}'.format(_config_path, _ENVIRON_CHAT_ID_KEY)
assert isinstance(CHAT_ID, int)


from .notifier import Notifier
