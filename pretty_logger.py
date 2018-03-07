#!/usr/bin/env python2.7

from datetime import datetime


class PrettyLogger(object):
    """ -
        use PrettyLogger(log_level="warn", msg="sup yo H|colorcode|highlight me")
        use PrettyLogger(log_level="warn", msg="sup yo H|highlight me")
    """

    header = 'your header'

    _log_level_map = {
        "error"   : ["red", "\x1b[31m"],
        "warn"    : ["yellow", "\x1b[33m"],
        "info"    : ["green", "\x1b[32m"],
        "verbose" : ["blue", "\x1b[34;1m"],
        "other"   : ["cyan", "\x1b[36m"],
        "invalid" : ["red", "\x1b[36m"],
        "creset"  : ["creset", "\x1b[0m"],
        "debug"   : ["magenta", "\x1b[35m"],
    }

    _color_map = {
        "red": "\x1b[31m",
        "yellow": "\x1b[33m",
        "green": "\x1b[32m",
        "blue": "\x1b[34m",
        "cyan": "\x1b[36m",
        "magenta": "\x1b[35m",
        "hred": "\x1b[31;1m",
        "hyellow": "\x1b[33;1m",
        "hblue": "\x1b[34;1m",
        "hgreen": "\x1b[32;1m",
        "hcyan": "\x1b[36;1m",
        "hmagenta": "\x1b[35;1m",
        "creset": "\x1b[0m",
    }

    def highlight(self, msg):
        if msg.startswith("H|"):
            reset_color = self._color_map["creset"]
            msg = msg.split("H|")[1]
            msg = msg.split(" ")
            msgcopy = msg
            for index, item in enumerate(msgcopy):
                print index, item
                if "|" in item:
                    color_code = item.split("|")[0].lower()
                    if color_code not in self._color_map:
                        highlight_color = self._color_map["hmagenta"]
                    else:
                        highlight_color = self._color_map[color_code]
                    word = item.split("|")[-1:][0]
                    word = '{}{}{}'.format(highlight_color, word, reset_color)
                    msg[index] = "{}".format(word)
            msg = " ".join(msg)
        return msg

    def fix_header(self):
        return "[\033[92m{} - {}\x1b[0m]".format(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), self.header)

    def __init__(self, **kwargs):
        log_level = kwargs["log_level"]
        if log_level not in self._log_level_map:
            log_level = "invalid"
        msg = kwargs["msg"]
        self.log_level_color = self._log_level_map[log_level][1]
        self.log_level_color_reset = self._log_level_map["creset"][1]
        self.log_level = ":{}{:>7s}{}:".format(self.log_level_color, log_level, self.log_level_color_reset)
        header = self.fix_header()
        msg = self.highlight(msg)
        print("{} {} {}").format(header, self.log_level, msg)
