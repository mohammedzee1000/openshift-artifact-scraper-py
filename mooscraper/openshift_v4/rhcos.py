from cached_request import request
from bs4 import BeautifulSoup

import constants

__extract_a_hrefs = lambda content: [x["href"].strip("/") for x in
                                     BeautifulSoup(content, features="html5lib").findAll("a")]


def get_rhcos_base_url_for_arch(arch: str) -> str:
    return "/".join([constants.ocpv4_moourl, arch, constants.dependencies, constants.rhcos])


def get_major_versions(arch: str) -> list[str]:
    data = request.get(get_rhcos_base_url_for_arch(arch) + "/")
    return [x for x in __extract_a_hrefs(data.text) if x not in ["..", "pre-release"]]


def get_rhcos_url_for_arch_and_version(arch: str, version: str) -> str:
    return "/".join([get_rhcos_base_url_for_arch(arch), version])


def get_sub_versions(arch: str, version: str) -> list[str]:
    if version == "latest":
        return []
    data = request.get(get_rhcos_url_for_arch_and_version(arch, version))
    return [x for x in __extract_a_hrefs(data.text) if x not in [".."]]


def get_rhcos_artifact_url_for_arch_version_and_subversion(arch: str, version: str, sub_version: str) -> str:
    return "/".join([get_rhcos_url_for_arch_and_version(arch, version), sub_version]) if version != "latest" else get_rhcos_url_for_arch_and_version(arch, version)


def get_artifact_files(arch: str, version: str, sub_version: str) -> list[str]:
    data = request.get(get_rhcos_artifact_url_for_arch_version_and_subversion(arch, version, sub_version))
    return [x for x in __extract_a_hrefs(data.text) if x not in [".."]]
