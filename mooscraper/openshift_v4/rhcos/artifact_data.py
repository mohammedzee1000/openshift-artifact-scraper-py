import copy

import mooscraper.moocore as moocore


class RHCOSReleasedVersionedArtifacts:
    def __init__(self, versioned_artifacts: moocore.MajorVersionArtifacts):
        self._major_versioned_artifacts = versioned_artifacts

    def get_artifacts_from_version_and_subversion(self, version: str, subversion: str) -> list[str]:
        v1 = self._major_versioned_artifacts.get(version) if self._major_versioned_artifacts else None
        return v1.get(subversion) if v1 else None

    def get_subversions_from_version(self, version: str) -> list[str]:
        v1 = self._major_versioned_artifacts.get(version) if self._major_versioned_artifacts else None
        return list(v1.keys()) if v1 else []

    def get_versions(self) -> list[str]:
        return list(self._major_versioned_artifacts.keys()) if self._major_versioned_artifacts else []


class RHCOSReleasedArtifacts:
    def __init__(self, versioned_artifacts: RHCOSReleasedVersionedArtifacts, latest_artifacts: list[str]):
        self._versioned_artifacts = versioned_artifacts
        self._latest_artifacts = latest_artifacts

    def get_versioned_artifacts(self) -> RHCOSReleasedVersionedArtifacts:
        return copy.deepcopy(self._versioned_artifacts)

    def get_latest_artifacts(self) -> list[str]:
        return [x for x in self._latest_artifacts]


class RHCOSPreReleaseArtifacts:
    def __init__(self, sub_versioned_artifacts: moocore.VersionedArtifacts):
        self._sub_versioned_artifacts = sub_versioned_artifacts

    def get_sub_versions(self) -> list[str]:
        return list(self._sub_versioned_artifacts.keys()) if self._sub_versioned_artifacts else []

    def get_artifacts_from_sub_version(self, sub_version: str) -> list[str]:
        return self._sub_versioned_artifacts.get(sub_version)