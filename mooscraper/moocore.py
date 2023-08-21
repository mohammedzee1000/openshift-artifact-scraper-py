from typing import Dict


class VersionedArtifacts(Dict[str, list[str]]):
    pass
    # def __setitem__(self, key, value):
    #     Dict[str, str].__setitem__(key, value)


class MajorVersionArtifacts(Dict[str, VersionedArtifacts]):
    pass
    # def __setitem__(self, key, value):
    #     Dict[str, VersionedArtifacts].__setitem__(key, value)
