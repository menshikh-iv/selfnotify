from __future__ import absolute_import
import urllib
import datetime
import traceback as tb
from . import CHAT_ID, TOKEN


class Notifier(object):
    _url_pattern = "https://api.telegram.org/bot{token}/sendMessage?{params}"

    def __init__(self, chat_id=CHAT_ID, token=TOKEN):
        self._chat_id = chat_id
        self._token = token

    def _notify(self, message):
        params = {"chat_id": self._chat_id,
                  "text": message}
        return urllib.urlopen(Notifier._url_pattern.format(token=self._token,
                                                           params=urllib.urlencode(params)))

    @staticmethod
    def _now():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __enter__(self):
        self._notify("[{}] Start".format(Notifier._now()))

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            exc_lines = tb.format_exception(exc_type, exc_value, exc_traceback)
            mess = "[{}] Something goes wrong\n".format(Notifier._now())
            mess += "\n{}\n".format("\n".join(exc_lines))
            self._notify(mess)
        else:
            self._notify("[{}] End".format(Notifier._now()))
