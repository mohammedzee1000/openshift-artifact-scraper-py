import functools

from packaging import version


@functools.total_ordering
class ComparableVersion:
    def __init__(self, _version: str):
        self._version = _version

    @property
    def version(self):
        return self._version

    def __is_parsable_version(self) -> bool:
        if any(text in self.version for text in ["ec", "fc", "latest"]):
            return False
        return True

    def __lt__(self, other):
        if self.__is_parsable_version() and other.__is_parsable_version():
            return version.parse(self.version) < version.parse(other.version)
        if self._version == "latest" and other.version == "latest":
            return False
        if self._version == "latest":
            return False
        if other.version == "latest":
            return True
        p1 = self.version.split("-")
        p2 = other.version.split("-")
        if version.parse(p1[0]) < version.parse(p2[0]):
            return True
        if version.parse(p1[0]) > version.parse(p2[0]):
            return False
        pp1 = p1[1].split(".")
        pp2 = p2[1].split(".")
        return pp1[1] < pp2[1]

    def __eq__(self, other):
        if self.__is_parsable_version() and other.__is_parsable_version():
            return version.parse(self.version) == version.parse(other.version)
        p1 = self.version.split("-")
        p2 = other.version.split("-")
        if version.parse(p1[0]) == version.parse(p2[0]):
            pp1 = p1[1].split(".")
            pp2 = p2[1].split(".")
            return pp1[1] == pp2[1]
