import constants


def get_rhcos_base_url_for_arch(arch: str) -> str:
    return "/".join([constants.ocpv4_moourl, arch, constants.dependencies, constants.rhcos])


def get_rhcos_url_arch_and_version(arch: str, version: str) -> str:
    return "/".join([get_rhcos_base_url_for_arch(arch), version])


def get_rhcos_url_released_non_latest_arch_version_and_subversion(arch: str, version: str, sub_version: str) -> str:
    return "/".join([get_rhcos_url_arch_and_version(arch, version),
                     sub_version]) if version != "latest" else None


def get_rhcos_url_released_nonlatest_arch_version_subversion_artifact(arch: str, version: str, sub_version: str,
                                                                      artifact: str):
    return "/".join(
        [get_rhcos_url_released_non_latest_arch_version_and_subversion(arch, version, sub_version), artifact])


def get_rhcos_url_latest_arch(arch: str):
    return get_rhcos_url_arch_and_version(arch, "latest")


def get_rhcos_url_latest_arch_artifact(arch: str, artifact: str):
    return "/".join([get_rhcos_url_latest_arch(arch), artifact])


def get_rhcos_url_prerelease(arch: str) -> str:
    return get_rhcos_url_arch_and_version(arch, "pre-release")


def get_rhcos_url_prerelease_subversion(arch: str, sub_version: str):
    return "/".join([get_rhcos_url_prerelease(arch), sub_version])


def get_rhcos_url_prerelease_artifact(arch: str, sub_version: str, artifact: str):
    return "/".join([get_rhcos_url_prerelease_subversion(arch, sub_version), artifact])
