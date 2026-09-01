from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .metric import Metric

class UsageFunctions(AppwriteModel):
    """
    UsageFunctions

    Attributes
    ----------
    builds : List[Metric]
        Aggregated number of functions build per period.
    buildsfailed : List[Metric]
        Aggregated number of failed function builds per period.
    buildsfailedtotal : float
        Total aggregated number of failed function builds.
    buildsmbseconds : List[Metric]
        Aggregated sum of functions build mbSeconds per period.
    buildsmbsecondstotal : float
        Total aggregated sum of functions build mbSeconds.
    buildsstorage : List[Metric]
        Aggregated sum of functions build storage per period.
    buildsstoragetotal : float
        total aggregated sum of functions build storage.
    buildssuccess : List[Metric]
        Aggregated number of successful function builds per period.
    buildssuccesstotal : float
        Total aggregated number of successful function builds.
    buildstime : List[Metric]
        Aggregated sum of  functions build compute time per period.
    buildstimetotal : float
        Total aggregated sum of functions build compute time.
    buildstotal : float
        Total aggregated number of functions build.
    deployments : List[Metric]
        Aggregated number of functions deployment per period.
    deploymentsstorage : List[Metric]
        Aggregated number of  functions deployment storage per period.
    deploymentsstoragetotal : float
        Total aggregated sum of functions deployment storage.
    deploymentstotal : float
        Total aggregated number of functions deployments.
    executions : List[Metric]
        Aggregated number of  functions execution per period.
    executionsmbseconds : List[Metric]
        Aggregated number of functions mbSeconds per period.
    executionsmbsecondstotal : float
        Total aggregated sum of functions execution mbSeconds.
    executionstime : List[Metric]
        Aggregated number of functions execution compute time per period.
    executionstimetotal : float
        Total aggregated sum of functions  execution compute time.
    executionstotal : float
        Total  aggregated number of functions execution.
    functions : List[Metric]
        Aggregated number of functions per period.
    functionstotal : float
        Total aggregated number of functions.
    range : str
        Time range of the usage stats.
    """
    builds: List[Metric] = Field(..., alias='builds')
    buildsfailed: List[Metric] = Field(..., alias='buildsFailed')
    buildsfailedtotal: float = Field(..., alias='buildsFailedTotal')
    buildsmbseconds: List[Metric] = Field(..., alias='buildsMbSeconds')
    buildsmbsecondstotal: float = Field(..., alias='buildsMbSecondsTotal')
    buildsstorage: List[Metric] = Field(..., alias='buildsStorage')
    buildsstoragetotal: float = Field(..., alias='buildsStorageTotal')
    buildssuccess: List[Metric] = Field(..., alias='buildsSuccess')
    buildssuccesstotal: float = Field(..., alias='buildsSuccessTotal')
    buildstime: List[Metric] = Field(..., alias='buildsTime')
    buildstimetotal: float = Field(..., alias='buildsTimeTotal')
    buildstotal: float = Field(..., alias='buildsTotal')
    deployments: List[Metric] = Field(..., alias='deployments')
    deploymentsstorage: List[Metric] = Field(..., alias='deploymentsStorage')
    deploymentsstoragetotal: float = Field(..., alias='deploymentsStorageTotal')
    deploymentstotal: float = Field(..., alias='deploymentsTotal')
    executions: List[Metric] = Field(..., alias='executions')
    executionsmbseconds: List[Metric] = Field(..., alias='executionsMbSeconds')
    executionsmbsecondstotal: float = Field(..., alias='executionsMbSecondsTotal')
    executionstime: List[Metric] = Field(..., alias='executionsTime')
    executionstimetotal: float = Field(..., alias='executionsTimeTotal')
    executionstotal: float = Field(..., alias='executionsTotal')
    functions: List[Metric] = Field(..., alias='functions')
    functionstotal: float = Field(..., alias='functionsTotal')
    range: str = Field(..., alias='range')
