from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .form_kit_step_marker import FormKitStepMarker

T = TypeVar('T')

class FormKitNode(AppwriteModel, Generic[T]):
    """
    One node of a form definition.

A definition is a FLAT ARRAY of these, and the storefront hands each one to `&lt;FormKitSchema&gt;` verbatim — it maps nothing, so every key FormKit understands works here whether or not it is named below (`options`, `if`, `rows`, `autocomplete`, `min`, `max`, `$cmp`, …). Three kinds of node occur:

  • an INPUT node (`$formkit`) collects a value and, if it carries a `name`, contributes exactly one key to a submission&#039;s `data`;
  • a CONTENT node (`$el`) renders markup — a paragraph of legal text, a heading — and collects nothing;
  • a STEP MARKER (`$rxStep`) is a Revenexx extension the storefront consumes and strips before FormKit sees the node; it splits the flat array into wizard steps.

Only the four keys `name`, `label`, `placeholder` and `help` are read by Revenexx code at all (the last three are what the per-form i18n overlay translates). Everything else is FormKit&#039;s business.

    Attributes
    ----------
    el : Optional[str]
        A CONTENT node instead of an input: a raw element name (&#039;p&#039;, &#039;h2&#039;, &#039;div&#039;). It collects no value and contributes no key to `data`.
    formkit : Optional[str]
        An INPUT node: the FormKit input type — &#039;text&#039;, &#039;email&#039;, &#039;textarea&#039;, &#039;number&#039;, &#039;select&#039;, &#039;checkbox&#039;, &#039;radio&#039;, &#039;date&#039;, &#039;group&#039;, &#039;list&#039;, … . The set is FormKit&#039;s, not this app&#039;s, which is why nothing here enforces it and no vocabulary is published for it; the storefront adds one input of its own, `datepicker`, and three validation rules (`zip`, `companyName`, `phoneNumber`).
    rxstep : Optional[FormKitStepMarker[T]]
        A Revenexx step marker. The storefront cuts the flat array at each marker and renders the nodes that follow it as one wizard step, then removes the marker before FormKit renders anything. A definition with no marker is a single-step form.
    children : Optional[str]
        The content of an `$el` node: a string of text, or nested nodes.
    help : Optional[str]
        The hint under the input. Translatable.
    label : Optional[str]
        What the visitor reads above the input. Translatable: the per-form i18n overlay replaces it per locale.
    name : Optional[str]
        The key this input writes into a submission&#039;s `data` — `{ &quot;$formkit&quot;: &quot;email&quot;, &quot;name&quot;: &quot;email&quot; }` here is the `&quot;email&quot;` key there, and that correspondence is the whole contract between a form and its inbox. A node with a non-empty `name` is a FIELD: only fields count against the tenant&#039;s `max_form_fields`, so a form with twenty paragraphs of legal text and three inputs is a three-field form. A `group` or `list` input nests, and its `name` keys the nested object or array.
    placeholder : Optional[str]
        Placeholder text inside the input. Translatable.
    rxkind : Optional[str]
        A Revenexx hint about where the value comes from rather than what it looks like. &#039;product&#039; means the storefront prefills this input from the page context or the query string (`?sku=…`) and renders it read-only — how a price request knows which article it is about. Stripped before FormKit renders the node.
    validation : Optional[str]
        FormKit validation, in either notation FormKit accepts: the pipe string &#039;required|email&#039;, or the array form. It is enforced in the browser by FormKit — this API stores whatever `data` it is sent, so a server-side integration must not treat it as a guarantee.
    """
    el: Optional[str] = Field(default=None, alias='$el')
    formkit: Optional[str] = Field(default=None, alias='$formkit')
    rxstep: Optional[FormKitStepMarker[T]] = Field(default=None, alias='$rxStep')
    children: Optional[str] = Field(default=None, alias='children')
    help: Optional[str] = Field(default=None, alias='help')
    label: Optional[str] = Field(default=None, alias='label')
    name: Optional[str] = Field(default=None, alias='name')
    placeholder: Optional[str] = Field(default=None, alias='placeholder')
    rxkind: Optional[str] = Field(default=None, alias='rxKind')
    validation: Optional[str] = Field(default=None, alias='validation')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormKitNode[T]':
        """Create FormKitNode instance with typed data."""
        internal_fields = {k: v for k, v in data.items() if k.startswith('$')}
        user_data = {k: v for k, v in data.items() if not k.startswith('$')}
        instance = cls.model_validate(internal_fields)
        instance._data = model_type(**user_data) if model_type is not dict else user_data
        return instance

    _data: Any = PrivateAttr(default_factory=dict)

    @property
    def data(self) -> T:
        return cast(T, self._data)

    @data.setter
    def data(self, value: T) -> None:
        object.__setattr__(self, '_data', value)

    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        if hasattr(self, '_data'):
            if isinstance(self._data, dict):
                result['data'] = self._data
            elif hasattr(self._data, 'model_dump'):
                result['data'] = self._data.model_dump(mode='json')
            else:
                result['data'] = self._data
        return result
