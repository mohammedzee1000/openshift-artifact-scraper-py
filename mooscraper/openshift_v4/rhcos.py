import copy

import constants
from cached_request import request
from mooscraper.mooutils import extract_a_hrefs


# This is all the core data classes for rhcos
class RHCOSArtifact:
    def __init__(self, artifact: str):
        self._artifact = artifact

    def get_artifact(self) -> str:
        return self._artifact


class RHCOSSubVersion:
    def __init__(self, sub_version: str, artifacts: list[RHCOSArtifact]):
        self._sub_version = sub_version
        self._artifacts = artifacts

    def get_subversion(self) -> str:
        return self._sub_version

    def get_artifacts(self) -> list[RHCOSArtifact]:
        return [x for x in self._artifacts]


class RHCOSReleasedVersion:
    def __init__(self, version: str, sub_versions: list[RHCOSSubVersion]):
        self._version = version
        self._sub_versions = sub_versions

    def get_version(self) -> str:
        return self._version

    def get_sub_versions(self) -> list[RHCOSSubVersion]:
        return [x for x in self._sub_versions]


class RHCOSReleasedLatestArtifacts:
    def __init__(self, artifacts: list[RHCOSArtifact]):
        self._artifacts = artifacts

    def get_artifacts(self) -> list[RHCOSArtifact]:
        return [x for x in self._artifacts]


# This us the core data class that will be returned to the user

class RHCOSArtifactInfo:
    def __init__(self, rhcos_released_versions: list[RHCOSReleasedVersion],
                 rhcos_released_latest_artifacts: RHCOSReleasedLatestArtifacts):
        self._rhcos_released_versions = rhcos_released_versions
        self._rhcos_latest_released_artifacts = rhcos_released_latest_artifacts

    def get_rhcos_released_versions(self) -> list[RHCOSReleasedVersion]:
        return [x for x in self._rhcos_released_versions]

    def get_rhcos_latest_artifacts(self) -> RHCOSReleasedLatestArtifacts:
        return copy.deepcopy(self._rhcos_latest_released_artifacts)


def get_rhcos_artifact_info(arch: str) -> RHCOSArtifactInfo:
    versions = []
    sub_versions = []
    artifacts = []
    data1 = request.get(get_rhcos_base_url_for_arch(arch))
    for major_version in [x for x in extract_a_hrefs(data1.text) if x not in ["..", "pre-release", "latest"]]:
        data2 = request.get(get_rhcos_url_for_arch_and_version(arch, major_version))
        sub_versions = []
        for sub_version in [x for x in extract_a_hrefs(data2.text) if x not in [".."]]:
            data3 = request.get(
                get_rhcos_artifact_url_for_arch_version_and_subversion(arch, major_version, sub_version))
            artifacts = []
            for artifact in [x for x in extract_a_hrefs(data3.text) if x not in [".."]]:
                a = RHCOSArtifact(artifact)
                artifacts.append(a)
            sv = RHCOSSubVersion(sub_version, artifacts)
            sub_versions.append(sv)
        v = RHCOSReleasedVersion(major_version, sub_versions)
        versions.append(v)
    data4 = request.get(get_rhcos_url_for_arch_and_version(arch, "latest"))
    artifacts = []
    for artifact in [x for x in extract_a_hrefs(data4.text) if x not in [".."]]:
        a = RHCOSArtifact(artifact)
        artifacts.append(a)
    rrrla = RHCOSReleasedLatestArtifacts(artifacts)
    return RHCOSArtifactInfo(versions, rrrla)


def get_rhcos_base_url_for_arch(arch: str) -> str:
    return "/".join([constants.ocpv4_moourl, arch, constants.dependencies, constants.rhcos])


def get_rhcos_url_for_arch_and_version(arch: str, version: str) -> str:
    return "/".join([get_rhcos_base_url_for_arch(arch), version])


def get_rhcos_artifact_url_for_arch_version_and_subversion(arch: str, version: str, sub_version: str) -> str:
    return "/".join([get_rhcos_url_for_arch_and_version(arch, version),
                     sub_version]) if version != "latest" else get_rhcos_url_for_arch_and_version(arch, version)
