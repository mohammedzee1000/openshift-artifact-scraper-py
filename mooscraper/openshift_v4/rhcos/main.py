from mooscraper.moocore import MajorVersionArtifacts, VersionedArtifacts
from mooscraper.mooutils import extract_a_hrefs
from mooscraper.openshift_v4.rhcos.types import RHCOSReleasedArtifacts, RHCOSPreReleaseArtifacts, \
    RHCOSReleasedVersionedArtifacts
from mooscraper.openshift_v4.rhcos.url_gen import get_rhcos_base_url_for_arch, get_rhcos_url_arch_and_version, \
    get_rhcos_url_released_non_latest_arch_version_and_subversion, get_rhcos_url_prerelease, \
    get_rhcos_url_prerelease_subversion
from mooscraper.openshift_v4.rhcos.url_gen import get_rhcos_url_latest_arch
from utils.cached_request import request


def get_released_artifacts(arch: str) -> RHCOSReleasedArtifacts:
    # Load info about released non-latest artifacts
    mva = MajorVersionArtifacts()
    data1 = request.get(get_rhcos_base_url_for_arch(arch))
    for major_version in [x for x in extract_a_hrefs(data1.text) if x not in ["..", "pre-release", "latest"]]:
        data2 = request.get(get_rhcos_url_arch_and_version(arch, major_version))
        mva[major_version] = VersionedArtifacts()
        for sub_version in [x for x in extract_a_hrefs(data2.text) if x not in [".."]]:
            data3 = request.get(
                get_rhcos_url_released_non_latest_arch_version_and_subversion(arch, major_version, sub_version))
            mva[major_version][sub_version] = []
            for artifact in [x for x in extract_a_hrefs(data3.text) if x not in [".."]]:
                mva[major_version][sub_version].append(artifact)
    rrva = RHCOSReleasedVersionedArtifacts(mva)
    data4 = request.get(get_rhcos_url_latest_arch(arch))
    return RHCOSReleasedArtifacts(rrva, [x for x in extract_a_hrefs(data4.text) if x not in [".."]])


def get_pre_release_artifacts(arch: str) -> RHCOSPreReleaseArtifacts:
    va = VersionedArtifacts()
    data1 = request.get(get_rhcos_url_prerelease(arch))
    for sub_version in [x for x in extract_a_hrefs(data1.text) if x not in [".."]]:
        data2 = request.get(get_rhcos_url_prerelease_subversion(arch, sub_version) + "/")
        va[sub_version] = []
        for artifact in [x for x in extract_a_hrefs(data2.text) if x not in [".."]]:
            va[sub_version].append(artifact)
    return RHCOSPreReleaseArtifacts(va)
