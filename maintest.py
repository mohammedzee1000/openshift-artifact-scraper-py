from mooscraper.openshift_v4 import rhcos
from quayscraper.quay import get_release_tags

if __name__ == '__main__':
    # print("Architecture = s390x")
    # for i in rhcos.get_versions("s390x"):
    #     print("\tversion: " + i)
    #     if i != "latest":
    #         print("\t\tSubversions: ")
    #         for j in rhcos.get_sub_versions("s390x", i):
    #             print("\t\t\t" + j + ":")
    #             print("\t\t\t\tArtifacts: ")
    #             for k in rhcos.get_artifact_files("s390x", i, j):
    #                 print("\t\t\t\t\t" + k)
    #     else:
    #         print("\t\tArtifacts: ")
    #         for j in rhcos.get_artifact_files("s390x", "latest", ""):
    #             print("\t\t\t" + j)
    print(get_release_tags()[0])
