import logging
from colorama import init, Fore, Style

init()

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[38;5;214m',
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA,
    }

    def format(self, record):
        time_str = self.formatTime(record, self.datefmt)
        levelname = record.levelname
        color = self.COLORS.get(levelname, '')
        reset = Style.RESET_ALL
        gray = '\033[90m'

        return f"{gray}[{time_str}]{reset} {color}[{levelname}]{reset} {record.getMessage()}"
