from mooscraper.mooutils import extract_a_hrefs
from mooscraper.openshift_v4.rhcos.url_gen import get_rhcos_base_url_for_arch, get_rhcos_url_arch_and_version, \
    get_rhcos_url_released_non_latest_arch_version_and_subversion, get_rhcos_url_latest_arch, get_rhcos_url_prerelease, \
    get_rhcos_url_prerelease_subversion
from utils.cached_request import request


class RHCOSArtifactsFetcher:
    def __init__(self, arch: str):
        self._arch = arch

    def get_released_versions(self) -> list[str]:
        data = request.get(get_rhcos_base_url_for_arch(self._arch))
        return [x for x in extract_a_hrefs(data.text) if x not in ["..", "pre-release", "latest"]] if data.ok else []

    def get_released_sub_versions(self, version: str) -> list[str]:
        data = request.get(get_rhcos_url_arch_and_version(self._arch, version))
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []

    def get_released_artifacts(self, version: str, sub_version: str):
        data = request.get(
            get_rhcos_url_released_non_latest_arch_version_and_subversion(self._arch, version, sub_version))
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []

    def get_latest_artifacts(self) -> list[str]:
        data = request.get(get_rhcos_url_latest_arch(self._arch))
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []

    def get_pre_release_sub_versions(self):
        data = request.get(get_rhcos_url_prerelease(self._arch))
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []

    def get_pre_release_artifacts(self, sub_version: str):
        data = request.get(get_rhcos_url_prerelease_subversion(self._arch, sub_version) + "/")
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []
