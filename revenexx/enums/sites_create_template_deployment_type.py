from enum import Enum

class SitesCreateTemplateDeploymentType(Enum):
    BRANCH = "branch"
    COMMIT = "commit"
    TAG = "tag"
