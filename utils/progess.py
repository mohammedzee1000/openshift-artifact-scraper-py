import itertools
import sys
import threading
import time


class ProgressMessage:
    def __init__(self, what: str, print_done=False):
        self._done = False
        self._what = what
        self._print_done = print_done
        self._thread = threading.Thread(target=self._animate)

    def _animate(self):
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self._done:
                break
            sys.stdout.write('\rloading ' + self._what + ' ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     \n') if self._print_done else None

    def start(self):
        self._thread.start()

    def done(self):
        self._done = True
