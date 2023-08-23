import sys

import quayscraper.quay
from mooscraper.openshift_v4.rhcos.main import get_released_artifacts, get_pre_release_artifacts
from utils.progess import ProgressMessage


def print_title(title: str):
    char_count = len(title) + 4
    print("#" * char_count)
    print("# " + title + " #")
    print("#" * char_count)


def print_msg(msg: str):
    print("#" * 10 + " " + msg + " " + "#" * 10)


if __name__ == '__main__':
    arch = "s390x"
    show_loading = True
    if len(sys.argv) > 1:
        arch = sys.argv[1]
        if len(sys.argv) > 2:
            t = sys.argv[2]
            if t.lower() in ["false", "0"]:
                show_loading = False
    # Getting data
    l1 = ProgressMessage("RHCOS Released Artifacts")
    l1.start() if show_loading else None
    ra = get_released_artifacts(arch)
    l1.done() if show_loading else None
    l2 = ProgressMessage("RHCOS Pre Release Artifacts") if show_loading else None
    l2.start() if show_loading else None
    pra = get_pre_release_artifacts(arch)
    l2.done() if show_loading else None
    l3 = ProgressMessage("quay tags for openshift release images") if show_loading else None
    l3.start() if show_loading else None
    tags = quayscraper.quay.get_release_tags()
    l3.done() if show_loading else None
    # Printing
    print("#" * 40)
    print_title("Released and Versioned RHCOS Artifacts")
    va = ra.get_versioned_artifacts()
    for v in va.get_versions():
        print("Version: " + v)
        for sv in va.get_subversions_from_version(v):
            print("  subversion: " + sv)
            print("    artifacts: ")
            for a in va.get_artifacts_from_version_and_subversion(v, sv):
                print("    - " + a)
    print("#" * 40)
    print_title("Latest Released RHCOS Artifacts")
    la = ra.get_latest_artifacts()
    for i in la:
        print("  - " + i)
    print("#" * 40)
    print_title("Pre Release and Sub versioned RHCOS Artifacts")
    for v in pra.get_sub_versions():
        if not v:
            break
        print("Version: " + v)
        print("  artifacts:")
        for a in pra.get_artifacts_from_sub_version(v):
            print("    - " + a)
    print("#" * 40)
    print_title("Quay Image Tags")
    for i in tags:
        print("  - " + i)
