from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .metric import Metric

class UsageFunction(AppwriteModel):
    """
    UsageFunction

    Attributes
    ----------
    builds : List[Metric]
        Aggregated number of function builds per period.
    buildsfailed : List[Metric]
        Aggregated number of failed builds per period.
    buildsfailedtotal : float
        Total aggregated number of failed function builds.
    buildsmbseconds : List[Metric]
        Aggregated number of function builds mbSeconds per period.
    buildsmbsecondstotal : float
        Total aggregated sum of function builds mbSeconds.
    buildsstorage : List[Metric]
        Aggregated sum of function builds storage per period.
    buildsstoragetotal : float
        total aggregated sum of function builds storage.
    buildssuccess : List[Metric]
        Aggregated number of successful builds per period.
    buildssuccesstotal : float
        Total aggregated number of successful function builds.
    buildstime : List[Metric]
        Aggregated sum of function builds compute time per period.
    buildstimeaverage : float
        Average builds compute time.
    buildstimetotal : float
        Total aggregated sum of function builds compute time.
    buildstotal : float
        Total aggregated number of function builds.
    deployments : List[Metric]
        Aggregated number of function deployments per period.
    deploymentsstorage : List[Metric]
        Aggregated number of  function deployments storage per period.
    deploymentsstoragetotal : float
        Total aggregated sum of function deployments storage.
    deploymentstotal : float
        Total aggregated number of function deployments.
    executions : List[Metric]
        Aggregated number of function executions per period.
    executionsmbseconds : List[Metric]
        Aggregated number of function mbSeconds per period.
    executionsmbsecondstotal : float
        Total aggregated sum of function executions mbSeconds.
    executionstime : List[Metric]
        Aggregated number of function executions compute time per period.
    executionstimetotal : float
        Total aggregated sum of function  executions compute time.
    executionstotal : float
        Total  aggregated number of function executions.
    range : str
        The time range of the usage stats.
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
    buildstimeaverage: float = Field(..., alias='buildsTimeAverage')
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
    range: str = Field(..., alias='range')
