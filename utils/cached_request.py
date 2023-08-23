import os
from datetime import timedelta

import requests_cache
from requests import auth

from utils.cache import get_cache_dir

cache_file_location = os.getenv("OPENSHIFT_ARTIFACT_SCRAPPER_CACHE_DIR") or os.pathsep.join(
    [str(get_cache_dir()), "openshift-artifact-scraper"])

request = requests_cache.CachedSession(cache_file_location, expire_after=timedelta(days=1))
quay_username = os.getenv("QUAY_USER")
quay_token = os.getenv("QUAY_TOKEN")
if quay_username == "" or quay_token == "":
    print(
        "Please provide quay user (env QUAY_USER) and quay token (env QUAY_TOKEN) or set the value in a '.env' file with export command in PWD")
    exit(1)
a = auth.HTTPDigestAuth
basic = auth.HTTPBasicAuth(quay_username, quay_token)
authenticated_req = requests_cache.CachedSession(cache_file_location, auth=basic, expire_after=timedelta(days=3))
