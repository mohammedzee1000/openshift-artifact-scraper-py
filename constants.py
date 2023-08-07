moo_url = "https://mirror.openshift.com/pub"
ocpv4_moourl = moo_url + "/openshift-v4"
ocpv4_architectures = ["amd64", "x86_64", "arm64", "s390x", "ppc64le"]
ocpv4_rhcos_moourl = ocpv4_moourl + "/{arch}/dependencies/rhcos"
ocpv4_rhcos_version_moourl = ocpv4_rhcos_moourl + "/{version}"
ocpv4_rhcos_sub_version_moourl = ocpv4_rhcos_version_moourl + "/{sub_version}"
