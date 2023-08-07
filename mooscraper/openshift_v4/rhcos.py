from cached_request import request
from bs4 import BeautifulSoup

import constants

__extract_a_hrefs = lambda content: [x["href"].strip("/") for x in
                                     BeautifulSoup(content, features="html5lib").findAll("a")]


def __build_rhcos_base_url(arch: str) -> str:
    return constants.ocpv4_rhcos_moourl.format(arch=arch)


def get_versions(arch: str) -> list[str]:
    data = request.get(__build_rhcos_base_url(arch) + "/")
    return [x for x in __extract_a_hrefs(data.text) if x not in ["..", "pre-release"]]


def __build_rhcos_version_url(arch: str, version: str) -> str:
    return constants.ocpv4_rhcos_version_moourl.format(arch=arch, version=version)


def get_sub_versions(arch: str, version: str) -> list[str]:
    if version == "latest":
        return []
    data = request.get(__build_rhcos_version_url(arch, version))
    return [x for x in __extract_a_hrefs(data.text) if x not in [".."]]


def __build_rhcos_artifact_url(arch: str, version: str, sub_version: str) -> str:
    return constants.ocpv4_rhcos_sub_version_moourl.format(arch=arch, version=version, sub_version=sub_version) if version != "latest" else __build_rhcos_version_url(arch=arch, version=version)


def get_artifact_files(arch: str, version: str, sub_version: str) -> list[str]:
    data = request.get(__build_rhcos_artifact_url(arch, version, sub_version))
    return [x for x in __extract_a_hrefs(data.text) if x not in [".."]]
