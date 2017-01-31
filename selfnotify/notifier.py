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

    def notify(self, message, with_ts=True):
        text = message

        if with_ts:
            text = "[{}] - {}".format(Notifier._now(), message)

        params = {"chat_id": self._chat_id,
                  "text": text}
        return urllib.urlopen(Notifier._url_pattern.format(token=self._token,
                                                           params=urllib.urlencode(params)))

    @staticmethod
    def _now():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __enter__(self):
        self.notify("Start")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            exc_lines = tb.format_exception(exc_type, exc_value, exc_traceback)
            mess = "Something goes wrong\n"
            mess += "\n{}\n".format("\n".join(exc_lines))
            self.notify(mess)
        else:
            self.notify("End".format(Notifier._now()))
