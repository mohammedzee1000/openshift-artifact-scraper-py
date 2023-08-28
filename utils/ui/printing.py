from rich.console import Console
from rich.status import Status


class RichPrinter:
    def __init__(self, pretty: bool):
        self._pretty = pretty
        self._console = Console()
        self._status = Status("_")
        self._status_set = False

    def print_title(self, title: str):
        if not self._pretty:
            return
        l = len(title) + 4
        self._console.print("*" * l)
        self._console.print("* [bold][u]" + title + "[/u][/bold] *")
        self._console.print("*" * l)

    def start_status(self, status: str):
        if self._status_set:
            raise Exception("please stop the current status before starting a new one")
        self._status = self._console.status(status)
        self._status.start()
        self._status_set = True

    def stop_last_status(self):
        if not self._status_set:
            raise Exception("please start a status before trying to stop one")
        self._status.stop()
        self._status_set = False

    def print_list(self, items: list[str]):
        if self._pretty:
            content = "[list]\n"
            for i in items:
                content = content + "  [*] " + i + "\n"
            self._console.print(content + "[/list]")
        else:
            for i in items:
                print(i)
