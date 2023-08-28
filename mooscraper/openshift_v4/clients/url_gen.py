import constants


def get_clients_base_url_for_arch(arch: str) -> str:
    return "/".join([constants.ocpv4_moourl, arch, constants.clients])


def get_clients_ocp_url_for_arch(arch: str) -> str:
    return "/".join([get_clients_base_url_for_arch(arch), constants.ocp])


def get_clients_ocp_dev_preview_url_for_arch(arch: str) -> str:
    return "/".join([get_clients_base_url_for_arch(arch), constants.ocp_dev_preview])


def get_clients_ocp_url_for_version_and_arch(arch: str, version: str) -> str:
    return "/".join([get_clients_ocp_url_for_arch(arch), version])


def get_clients_ocp_dev_preview_url_for_version_and_arch(arch: str, version: str) -> str:
    return "/".join([get_clients_ocp_dev_preview_url_for_arch(arch), version])


def get_clients_ocp_url_for_version_arch_and_artifact(arch: str, version: str, artifact: str) -> str:
    return "/".join([get_clients_ocp_url_for_version_and_arch(arch, version), artifact])


def get_clients_ocp_dev_preview_url_for_version_arch_and_artifact(arch: str, version: str, artifact: str) -> str:
    return "/".join([get_clients_ocp_dev_preview_url_for_version_and_arch(arch, version), artifact])
