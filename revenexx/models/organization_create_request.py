from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.organization_status import OrganizationStatus

class OrganizationCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    branche : Optional[str]
        Industry / line of business, in the merchant&#039;s own words. Free text: no NACE code, no WZ number, no list to pick from — whatever somebody typed on the company. Segment rules read it, and both `?branche=` and an `eq` condition match it EXACTLY and case-sensitively, so &#039;Maschinenbau&#039; and &#039;maschinenbau&#039; are two different industries. Indexed, so it stays cheap to filter on.
    credit_limit : Optional[float]
        Ceiling on open receivables in the market&#039;s currency, and one of the inputs that decide whether an order is accepted at all. Null means NO limit — not a limit of zero. A create without it inherits the tenant&#039;s `default_credit_limit`.
    customer_number : Optional[str]
        The number this company carries in the merchant&#039;s own ERP — the key an ERP integration joins on, and what a service desk asks for on the phone. Free text with NO enforced format (a letter prefix and a running number is the common shape, but plain digits are just as valid), unique per tenant while it is set, and one of the fields duplicate detection can be pointed at. The real values come out of the merchant&#039;s ERP; nothing published here can name one that exists. A second company with the same number is a 409.
    delivery_block : Optional[bool]
        True stops SHIPMENTS to this company while leaving login and ordering alone — the &quot;they may order, we are just not sending anything until this is settled&quot; state. Separate from `status` on purpose: blocking the login to stop a delivery locks out the people who could settle it. Default false.
    lifecycle_stage : Optional[str]
        Where the company stands in the SALES PIPELINE, and a deliberately separate axis from `status`: a prospect that may log in and a customer that may not are both ordinary states, and one column cannot say that. One of the tenant&#039;s own stages (GET /customers/lifecycle-stages) — a fresh install starts with lead, prospect, customer, churned, and the merchant may add their own. Nothing moves it automatically; a stage changes when a person or an integration says so. A create without it gets the stage flagged as default; a value the tenant does not keep is a 400.
    name : str
        Legal or trading name of the COMPANY — never a person. Mirrored to the platform team, so a rename here is a rename in storefront auth too.
    payment_terms : Optional[str]
        When this company has to pay — one of the tenant&#039;s own terms (GET /customers/payment-terms, seeded with prepayment, direct_debit, net_7/14/30/60/90). Null means nothing was agreed and the order flow falls back to the market&#039;s `default_payment_terms`. This is a commercial term, not a payment method: HOW they pay is the payments app&#039;s business. A create without it inherits the market&#039;s `default_payment_terms`; a value the tenant does not keep is a 400.
    price_list : Optional[str]
        Code of the price list this company buys on — plain text pointing into the prices app. ADR-0055 forbids the cross-app foreign key, so nothing here checks it: a code that names no list simply prices nothing. `standard` is the list the prices app seeds on install.
    settings : Optional[Dict[str, Any]]
        Free-form per-organization settings, keyed by whatever the merchant&#039;s own integrations agree on — this app never branches on a key in here. Segment rules can address a TOP-LEVEL key as `setting:&lt;key&gt;`, which is the whole reason the blob survives: a flag an ERP writes here selects a segment without a schema change. Commercial terms are typed columns now (payment_terms, credit_limit); writing them back in here leaves the checkout reading the column and finding nothing. Replaced wholesale on an update — send the whole object, not a patch of it.
    status : Optional[OrganizationStatus]
        ACCESS, not pipeline: &#039;blocked&#039; stops this company&#039;s people from logging in and is where a rejected registration parks the company it founded. &#039;active&#039; is the default. For how far along a company is, read `lifecycle_stage` — reading this one for that is how a won deal gets locked out. Default &#039;active&#039;.
    vat_id : Optional[str]
        VAT identification number (USt-IdNr. in Germany) — the closest thing a B2B buyer has to a legal identity. Validated against the EU VIES service when the tenant&#039;s `organization_vat_id_required` setting is on, and stored verbatim otherwise, including for buyers outside the EU.
    """
    branche: Optional[str] = Field(default=None, alias='branche')
    credit_limit: Optional[float] = Field(default=None, alias='credit_limit')
    customer_number: Optional[str] = Field(default=None, alias='customer_number')
    delivery_block: Optional[bool] = Field(default=None, alias='delivery_block')
    lifecycle_stage: Optional[str] = Field(default=None, alias='lifecycle_stage')
    name: str = Field(..., alias='name')
    payment_terms: Optional[str] = Field(default=None, alias='payment_terms')
    price_list: Optional[str] = Field(default=None, alias='price_list')
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
    status: Optional[OrganizationStatus] = Field(default=None, alias='status')
    vat_id: Optional[str] = Field(default=None, alias='vat_id')
