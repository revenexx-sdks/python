from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .headers import Headers
from ..enums.execution_status import ExecutionStatus
from ..enums.execution_trigger import ExecutionTrigger

class Execution(AppwriteModel):
    """
    Execution

    Attributes
    ----------
    createdat : str
        Execution creation date in ISO 8601 format.
    id : str
        Execution ID.
    permissions : List[Any]
        Execution roles.
    updatedat : str
        Execution update date in ISO 8601 format.
    deploymentid : str
        Function&#039;s deployment ID used to create the execution.
    duration : float
        Resource(function/site) execution duration in seconds.
    errors : str
        Function errors. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    functionid : str
        Function ID.
    logs : str
        Function logs. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    requestheaders : List[Headers]
        HTTP request headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    requestmethod : str
        HTTP request method type.
    requestpath : str
        HTTP request path and query.
    responsebody : str
        HTTP response body. This will return empty unless execution is created as synchronous.
    responseheaders : List[Headers]
        HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    responsestatuscode : float
        HTTP response status code.
    scheduledat : Optional[str]
        The scheduled time for execution. If left empty, execution will be queued immediately.
    status : ExecutionStatus
        The status of the function execution. Possible values can be: `waiting`, `processing`, `completed`, `failed`, or `scheduled`.
    trigger : ExecutionTrigger
        The trigger that caused the function to execute. Possible values can be: `http`, `schedule`, or `event`.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    updatedat: str = Field(..., alias='$updatedAt')
    deploymentid: str = Field(..., alias='deploymentId')
    duration: float = Field(..., alias='duration')
    errors: str = Field(..., alias='errors')
    functionid: str = Field(..., alias='functionId')
    logs: str = Field(..., alias='logs')
    requestheaders: List[Headers] = Field(..., alias='requestHeaders')
    requestmethod: str = Field(..., alias='requestMethod')
    requestpath: str = Field(..., alias='requestPath')
    responsebody: str = Field(..., alias='responseBody')
    responseheaders: List[Headers] = Field(..., alias='responseHeaders')
    responsestatuscode: float = Field(..., alias='responseStatusCode')
    scheduledat: Optional[str] = Field(default=None, alias='scheduledAt')
    status: ExecutionStatus = Field(..., alias='status')
    trigger: ExecutionTrigger = Field(..., alias='trigger')
