from mooscraper.openshift_v4 import rhcos
from quayscraper.quay import get_release_tags

def printMsg(msg: str):
    print("#"*10 + " " + msg + " " + "#"*10)

if __name__ == '__main__':
    print("#"*40)
    printMsg("Architecture = s390x")
    rhcosArtifacts = rhcos.get_rhcos_artifact_info("s390x")
    printMsg("Released versioned artifacts")
    rhcosVersionedArtifacts = rhcosArtifacts.get_rhcos_released_versions()
    for i in rhcosArtifacts.get_rhcos_released_versions():
        printMsg("Version: " + i.get_version())
        for j in i.get_sub_versions():
            print("\t- " + j.get_subversion())
            for k in j.get_artifacts():
                print("\t  - " + k.get_artifact())
    print("#"*40)
    rhcosLatestArtifacts = rhcosArtifacts.get_rhcos_latest_artifacts()
    printMsg("Released Latest Artifacts")
    for i in rhcosLatestArtifacts.get_artifacts():
        print("\t- " + i.get_artifact())
    tags = get_release_tags()
    print("Openshift release tags:")
    print(", ".join(tags))
    print("#"*20)
