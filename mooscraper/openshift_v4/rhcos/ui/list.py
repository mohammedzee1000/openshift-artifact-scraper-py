from mooscraper.openshift_v4.rhcos.main import RHCOSArtifactsFetcher

from utils.ui.printing import RichPrinter


def list_released_versions(arch: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Released Versions")
    rp.start_status("fetching RHCOS versions")
    items = RHCOSArtifactsFetcher(arch).get_released_versions()
    rp.stop_last_status()
    rp.print_list(items)


def list_released_sub_versions(arch: str, version: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Released Sub Versions for version " + version)
    rp.start_status("fetching rhcos sub versions")
    items = RHCOSArtifactsFetcher(arch).get_released_sub_versions(version)
    rp.stop_last_status()
    rp.print_list(items)


def list_released_artifacts(arch: str, version: str, sub_version: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Artifacts Version " + version + " Sub Version " + sub_version)
    rp.start_status("fetching rhcos artifacts")
    items = RHCOSArtifactsFetcher(arch).get_released_artifacts(version, sub_version)
    rp.stop_last_status()
    rp.print_list(items)


def list_latest_artifacts(arch: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Latest Artifacts")
    rp.start_status("fetching RHCOS artifacts")
    items = RHCOSArtifactsFetcher(arch).get_latest_artifacts()
    rp.stop_last_status()
    rp.print_list(items)


def list_pre_release_versions(arch: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Pre-Release sub versions")
    rp.start_status("fetching RHCOS pre release sub versions")
    items = RHCOSArtifactsFetcher(arch).get_pre_release_sub_versions()
    rp.stop_last_status()
    rp.print_list(items)


def list_pre_release_artifacts(arch: str, sub_version: str, pretty=True):
    rp = RichPrinter(pretty)
    rp.print_title("RHCOS Pre-Release artifacts for sub version " + sub_version)
    rp.start_status("fetching RHCOS pre release artifacts")
    items = RHCOSArtifactsFetcher(arch).get_pre_release_artifacts(sub_version)
    rp.stop_last_status()
    rp.print_list(items)
