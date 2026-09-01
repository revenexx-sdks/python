from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRegisterRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        The buyer&#039;s address. It becomes the login AND the unique key of the contact, so a second registration with it is a 409 — including while the first one is still waiting for approval.
    first_name : Optional[str]
        Given name. Optional: an ERP import often has only a mailbox.
    last_name : Optional[str]
        Family name. Optional for the same reason.
    locale : Optional[str]
        The language this person is written to in — BCP 47, and one of the store&#039;s configured locales. Null falls back to the store default. One of the store&#039;s own locales, or the call is a 400.
    organization_id : Optional[str]
        JOIN an existing company — the invite shape. Neither b2b_registration_enabled nor b2c_registration_enabled applies to it.
    organization_name : Optional[str]
        FOUND a new company, with this contact as its admin. This is what makes the registration a B2B one; leaving it out registers a standalone buyer.
    password : str
        The password the buyer chooses. It is hashed by the identity service at this moment and never travels again: an approval later enables the account, it does not issue a new credential.
    url : Optional[str]
        Where the welcome mail&#039;s button points — the buyer&#039;s first stop in this shop. Absent, the mail still goes out and simply carries no button. Ignored when the registration is an APPLICATION: there is no account to send anybody to yet.
    vat_id : Optional[str]
        VAT identification number (USt-IdNr. in Germany) — the closest thing a B2B buyer has to a legal identity. Validated against the EU VIES service when the tenant&#039;s `organization_vat_id_required` setting is on, and stored verbatim otherwise, including for buyers outside the EU. Required when the tenant&#039;s `organization_vat_id_required` is on, and checked BEFORE the company is created so a bad one leaves no half-founded organization behind.
    verification_url : Optional[str]
        Where the address-confirmation link points, when the tenant&#039;s `email_verification` asks for one on registration. `userId`, `secret` and `expire` are appended, and `PUT /customers/auth/verification` takes the first two. Without it the registration still succeeds and `verification_sent` is false — this app cannot invent a storefront URL, and a link pointing nowhere is worse than none.
    """
    email: str = Field(..., alias='email')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    organization_name: Optional[str] = Field(default=None, alias='organization_name')
    password: str = Field(..., alias='password')
    url: Optional[str] = Field(default=None, alias='url')
    vat_id: Optional[str] = Field(default=None, alias='vat_id')
    verification_url: Optional[str] = Field(default=None, alias='verification_url')
