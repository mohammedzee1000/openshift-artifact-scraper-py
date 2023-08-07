from datetime import timedelta
import requests_cache

request = requests_cache.CachedSession('opeshift_artifact_cache', expire_after=timedelta(days=1))