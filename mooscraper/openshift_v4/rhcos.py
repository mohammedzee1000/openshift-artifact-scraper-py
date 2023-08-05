import requests
from bs4 import BeautifulSoup

import constants

__extract_a_hrefs = lambda content: [x["href"].strip("/") for x in
                                     BeautifulSoup(content, features="html5lib").findAll("a")]


def __build_rhcos_base_url(arch: str) -> str:
    return "/".join([constants.ocpv4_moourl, arch, constants.dependencies, constants.rhcos])


def get_versions(arch: str) -> list[str]:
    data = requests.get(__build_rhcos_base_url(arch) + "/")
    return [x for x in __extract_a_hrefs(data.text) if x not in ["..", "pre-release"]]


def __build_rhcos_version_url(arch: str, version: str) -> str:
    return "/".join([__build_rhcos_base_url(arch), version])


def get_sub_versions(arch: str, version: str) -> list[str]:
    versions = []
    data = requests.get(__build_rhcos_version_url(arch, version))
    return [x for x in __extract_a_hrefs(data.text) if x not in [".."]]

# def _build_rhcos_version_url(base_url: str, version: str)
