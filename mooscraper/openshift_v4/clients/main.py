from mooscraper.mooutils import extract_a_hrefs
from mooscraper.openshift_v4.clients.url_gen import get_clients_ocp_url_for_arch, \
    get_clients_ocp_dev_preview_url_for_arch, get_clients_ocp_url_for_version_and_arch, \
    get_clients_ocp_dev_preview_url_for_version_and_arch, get_clients_ocp_url_for_version_arch_and_artifact, \
    get_clients_ocp_dev_preview_url_for_version_arch_and_artifact
from utils.cached_request import request


class ClientArtifactsFetcher:
    def __init__(self, arch: str):
        self._arch = arch

    def get_ocp_sub_versions(self, dev_preview=False) -> list[str]:
        data = request.get(
            get_clients_ocp_url_for_arch(self._arch) if not dev_preview else get_clients_ocp_dev_preview_url_for_arch(
                self._arch)
        )
        return [x for x in extract_a_hrefs(data.text) if x not in ["..", "unreleased"]] if data.ok else []

    def get_ocp_artifacts(self, version: str, dev_preview=False) -> list:
        data = request.get(
            get_clients_ocp_url_for_version_and_arch(self._arch, version) if not dev_preview
            else get_clients_ocp_dev_preview_url_for_version_and_arch(self._arch, version)
        )
        return [x for x in extract_a_hrefs(data.text) if x not in [".."]] if data.ok else []