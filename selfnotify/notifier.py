# -*- coding: utf-8 -*-
from __future__ import absolute_import
import urllib
import urllib.parse
import urllib.request
import datetime
import traceback as tb
from . import CHAT_ID, TOKEN

try:
    from urllib import urlencode
    from urllib import urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import urlopen
    


class Notifier(object):
    _url_pattern = u"https://api.telegram.org/bot{token}/sendMessage?{params}"

    def __init__(self, job_name=u'✉️', chat_id=CHAT_ID, token=TOKEN):
        self.job_name = job_name
        self._chat_id = chat_id
        self._token = token

    def notify(self, message, with_timestamp=True):
        text = message

        if len(self.job_name) > 0:
            text = u'{}: {}'.format(self.job_name, message)

        if with_timestamp:
            text = u"[{}] - {}".format(Notifier._now(), text)

        params = {"chat_id": self._chat_id,
                  "text": text.encode('utf8'),
                  "parse_mode": 'Markdown'}

        message = urlencode(params)
        return urlopen(Notifier._url_pattern.format(token=self._token,
                                            params=message))

    @staticmethod
    def _now():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __enter__(self):
        self.notify(u"Start")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            exc_lines = tb.format_exception(exc_type, exc_value, exc_traceback)
            mess = u"Something goes wrong\n"
            mess += "\n{}\n".format("\n".join(exc_lines))
            self.notify(mess)
        else:
            self.notify("End".format(Notifier._now())) #??
