from __future__ import absolute_import
import json
import os

__version__ = '0.1'
_config_fn = 'selfnotify.json'

_user_dir = os.path.expanduser('~')
_selfnotify_dir = os.path.join(_user_dir, '.selfnotify')
if not os.path.exists(_selfnotify_dir):
    os.makedirs(_selfnotify_dir)

_config_path = os.path.join(_selfnotify_dir, _config_fn)

if os.path.exists(_config_path):
    with open(_config_path) as infile:
        cfg = json.load(infile)

    assert 'token' in cfg
    assert 'chat_id' in cfg
    assert cfg['token'], 'You should write bot `token` to {}'.format(_config_path)
    assert len(cfg['token']) > 0, 'You should write bot `token` to {}'.format(_config_path)
    assert cfg['chat_id'], 'You should write `chat_id` to {}'.format(_config_path)
    assert isinstance(cfg['chat_id'], int)

    TOKEN = cfg['token']
    CHAT_ID = cfg['chat_id']

if not os.path.exists(_config_path):
    cfg = {'token': None,
           'chat_id': None}

    with open(_config_path, 'w') as outfile:
        outfile.write(json.dumps(cfg))

    raise RuntimeError('Please, fill config file {}'.format(_config_path))

from .notifier import Notifier
