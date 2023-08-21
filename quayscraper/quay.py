import json

from utils.cached_request import authenticated_req


def __get_ocp_release_dev_tags_url() -> str:
    return "https://quay.io/api/v1/repository/openshift-release-dev/ocp-release"


def get_ocp_release_image_repo_url(tag: str):
    return "quay.io/openshift-release-dev/ocp-release:{tag}".format(tag=tag)


def get_release_tags() -> list[str]:
    data = authenticated_req.get(__get_ocp_release_dev_tags_url())
    data_dict = json.loads(data.text)
    return list(data_dict["tags"].keys())
