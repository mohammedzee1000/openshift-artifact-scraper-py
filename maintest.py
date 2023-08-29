import sys

from mooscraper.openshift_v4.rhcos.ui.list import list_released_sub_versions, list_released_artifacts, \
    list_released_versions, list_latest_artifacts, list_pre_release_versions, list_pre_release_artifacts
from utils.ui.download import download


def print_title(title: str):
    char_count = len(title) + 4
    print("#" * char_count)
    print("# " + title + " #")
    print("#" * char_count)


def print_msg(msg: str):
    print("#" * 10 + " " + msg + " " + "#" * 10)


if __name__ == '__main__':
    arch = "s390x"
    pretty = True
    if len(sys.argv) > 1:
        arch = sys.argv[1]
        if len(sys.argv) > 2:
            t = sys.argv[2]
            if t.lower() in ["false", "0"]:
                pretty = False
    down = False
    list_released_versions(arch, pretty)
    list_released_sub_versions(arch, "4.13", pretty)
    list_released_artifacts(arch, "4.13", "4.13.5", pretty)
    list_latest_artifacts(arch, pretty)
    list_pre_release_versions(arch, pretty)
    list_pre_release_artifacts(arch, "latest-4.14", pretty)
    download(["https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/rhcos-qemu.s390x.qcow2.gz"], "./") if down else None
