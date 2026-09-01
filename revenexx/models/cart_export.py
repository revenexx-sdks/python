from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_io_format import CartIoFormat

class CartExport(AppwriteModel):
    """
    

    Attributes
    ----------
    content : Optional[str]
        The export itself. For json: `{ &quot;cart&quot;: { name, status, currency, channel_id, item_count, subtotal }, &quot;items&quot;: [ … ] }` — exactly what carts.import takes back, so an export round-trips. For csv: the lines as a CSV string, header first, with jsonb columns serialized as JSON text. Deliberately untyped, because a profile&#039;s mapping renames the columns and that mapping is the caller&#039;s own.
    filename : Optional[str]
        A suggested download name, built as `cart-&lt;cart id&gt;.&lt;format&gt;`. Nothing is stored under it; it is there so a browser download has a name that says which cart it is.
    format : Optional[CartIoFormat]
        The format that ran — the profile&#039;s, or the ad-hoc one.
    """
    content: Optional[str] = Field(default=None, alias='content')
    filename: Optional[str] = Field(default=None, alias='filename')
    format: Optional[CartIoFormat] = Field(default=None, alias='format')
