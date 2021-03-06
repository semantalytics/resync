"""ResourceSync ResourceDumpManifest object

"""

from list_base_with_index import ListBaseWithIndex

class ResourceDumpManifest(ListBaseWithIndex):
    """Class representing a Resource Dump Manifest"""

    def __init__(self, resources=None, md=None, ln=None):
        if (resources is None):
            resources = list()
        super(ResourceDumpManifest, self).__init__(resources=resources, md=md, ln=ln)
        self.capability_name='resourcedump-manifest'
        self.capability_md='resourcedump-manifest'

