import sys

import quayscraper.quay
from mooscraper.openshift_v4.clients.main import ClientArtifactsFetcher
from mooscraper.openshift_v4.rhcos.main import  RHCOSArtifactsFetcher
from utils.progess import ProgressMessage
from rich.tree import Tree
from rich import print as rprint


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

    ocpArtifacts = Tree("OCP Artifacts")
    rhcosArtifacts = ocpArtifacts.add("RHCOS")
    raf = RHCOSArtifactsFetcher(arch)
    rhcosReleasedArtifacts = rhcosArtifacts.add("Released")
    for v in raf.get_released_versions():
        rvt = rhcosReleasedArtifacts.add(v)
        for sv in raf.get_released_sub_versions(v):
            rsvt = rvt.add(sv)
            for a in raf.get_released_artifacts(v, sv):
                rsvt.add(a)

    rhcosLatestArtifacts = rhcosReleasedArtifacts.add("latest")
    for a in raf.get_latest_artifacts():
        rhcosLatestArtifacts.add(a)
    rhcosPreReleaseArtifacts = rhcosArtifacts.add("Pre Release")
    for sv in raf.get_pre_release_sub_versions():
        prsvt = rhcosPreReleaseArtifacts.add(sv)
        for a in raf.get_pre_release_artifacts(sv):
            prsvt.add(a)

    caf = ClientArtifactsFetcher(arch)
    clientArtifacts = ocpArtifacts.add("Clients")
    clientOCPArtifacts = clientArtifacts.add("OCP")
    for sv in caf.get_ocp_sub_versions():
        cvt = clientOCPArtifacts.add(sv)
        for a in caf.get_ocp_artifacts(sv):
            cvt.add(a)
    rprint(ocpArtifacts)