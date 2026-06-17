from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Bucket(AppwriteModel):
    """
    Bucket

    Attributes
    ----------
    createdat : str
        Bucket creation time in ISO 8601 format.
    id : str
        Bucket ID.
    permissions : List[Any]
        Bucket permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    updatedat : str
        Bucket update date in ISO 8601 format.
    allowedfileextensions : List[Any]
        Allowed file extensions.
    antivirus : bool
        Virus scanning is enabled.
    compression : str
        Compression algorithm chosen for compression. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    enabled : bool
        Bucket enabled.
    encryption : bool
        Bucket is encrypted.
    filesecurity : bool
        Whether file-level security is enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    maximumfilesize : float
        Maximum file size supported.
    name : str
        Bucket name.
    totalsize : float
        Total size of this bucket in bytes.
    transformations : bool
        Image transformations are enabled.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    updatedat: str = Field(..., alias='$updatedAt')
    allowedfileextensions: List[Any] = Field(..., alias='allowedFileExtensions')
    antivirus: bool = Field(..., alias='antivirus')
    compression: str = Field(..., alias='compression')
    enabled: bool = Field(..., alias='enabled')
    encryption: bool = Field(..., alias='encryption')
    filesecurity: bool = Field(..., alias='fileSecurity')
    maximumfilesize: float = Field(..., alias='maximumFileSize')
    name: str = Field(..., alias='name')
    totalsize: float = Field(..., alias='totalSize')
    transformations: bool = Field(..., alias='transformations')
