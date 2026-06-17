from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class File(AppwriteModel):
    """
    File

    Attributes
    ----------
    createdat : str
        File creation date in ISO 8601 format.
    id : str
        File ID.
    permissions : List[Any]
        File permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    updatedat : str
        File update date in ISO 8601 format.
    bucketid : str
        Bucket ID.
    chunkstotal : float
        Total number of chunks available
    chunksuploaded : float
        Total number of chunks uploaded
    compression : str
        Compression algorithm used for the file. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    encryption : bool
        Whether file contents are encrypted at rest.
    mimetype : str
        File mime type.
    name : str
        File name.
    signature : str
        File MD5 signature.
    sizeoriginal : float
        File original size in bytes.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    updatedat: str = Field(..., alias='$updatedAt')
    bucketid: str = Field(..., alias='bucketId')
    chunkstotal: float = Field(..., alias='chunksTotal')
    chunksuploaded: float = Field(..., alias='chunksUploaded')
    compression: str = Field(..., alias='compression')
    encryption: bool = Field(..., alias='encryption')
    mimetype: str = Field(..., alias='mimeType')
    name: str = Field(..., alias='name')
    signature: str = Field(..., alias='signature')
    sizeoriginal: float = Field(..., alias='sizeOriginal')
