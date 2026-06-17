from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.number_range import NumberRange;
from ..models.order_item_create_request import OrderItemCreateRequest;
from ..models.order_detail import OrderDetail;
from ..models.order import Order;
from ..enums.order_comment_visibility import OrderCommentVisibility;
from ..models.order_comment import OrderComment;
from ..models.order_cancel_position import OrderCancelPosition;
from ..enums.order_payment_status import OrderPaymentStatus;
from ..models.order_return_position import OrderReturnPosition;
from ..models.order_return import OrderReturn;
from ..models.order_shipment_position import OrderShipmentPosition;

class Orders(Service):

    def __init__(self, client) -> None:
        super(Orders, self).__init__(client)

    def orders_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def orders_number_ranges_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def orders_number_ranges_create(
        self,
        code: str,
        channel_id: Optional[str] = None,
        counter: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        padding: Optional[float] = None,
        position_step: Optional[float] = None,
        prefix: Optional[str] = None,
        step: Optional[float] = None,
        suffix: Optional[str] = None
    ) -> NumberRange:
        """
        

        Parameters
        ----------
        code : str
            Range key drawn by the app ('order', 'delivery', 'return') — unique per tenant.
        channel_id : Optional[str]
            
        counter : Optional[float]
            Current counter value (default 0) — the next number draws counter+step.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        padding : Optional[float]
            Zero-padding width of the counter (default 6).
        position_step : Optional[float]
            Position numbering increment for order items (default 10).
        prefix : Optional[str]
            Default ''.
        step : Optional[float]
            Counter increment per drawn number (default 1).
        suffix : Optional[str]
            Default ''.
        
        Returns
        -------
        NumberRange
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')


        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['code'] = self._normalize_value(code)
        if counter is not None:
            api_params['counter'] = self._normalize_value(counter)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if padding is not None:
            api_params['padding'] = self._normalize_value(padding)
        if position_step is not None:
            api_params['position_step'] = self._normalize_value(position_step)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if step is not None:
            api_params['step'] = self._normalize_value(step)
        if suffix is not None:
            api_params['suffix'] = self._normalize_value(suffix)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=NumberRange)


    def orders_number_ranges_defaults(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def orders_number_ranges_delete(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def orders_number_ranges_get(
        self,
        id: str
    ) -> NumberRange:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        NumberRange
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=NumberRange)


    def orders_number_ranges_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        code: Optional[str] = None,
        counter: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        padding: Optional[float] = None,
        position_step: Optional[float] = None,
        prefix: Optional[str] = None,
        step: Optional[float] = None,
        suffix: Optional[str] = None
    ) -> NumberRange:
        """
        

        Parameters
        ----------
        id : str
            
        channel_id : Optional[str]
            
        code : Optional[str]
            Range key drawn by the app ('order', 'delivery', 'return') — unique per tenant.
        counter : Optional[float]
            Current counter value (default 0) — the next number draws counter+step.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        padding : Optional[float]
            Zero-padding width of the counter (default 6).
        position_step : Optional[float]
            Position numbering increment for order items (default 10).
        prefix : Optional[str]
            Default ''.
        step : Optional[float]
            Counter increment per drawn number (default 1).
        suffix : Optional[str]
            Default ''.
        
        Returns
        -------
        NumberRange
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if counter is not None:
            api_params['counter'] = self._normalize_value(counter)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if padding is not None:
            api_params['padding'] = self._normalize_value(padding)
        if position_step is not None:
            api_params['position_step'] = self._normalize_value(position_step)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if step is not None:
            api_params['step'] = self._normalize_value(step)
        if suffix is not None:
            api_params['suffix'] = self._normalize_value(suffix)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=NumberRange)


    def orders_place(
        self,
        items: List[OrderItemCreateRequest],
        billing_address: Optional[Dict[str, Any]] = None,
        buyer: Optional[Dict[str, Any]] = None,
        cart_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        customer_order_number: Optional[str] = None,
        grand_total: Optional[float] = None,
        market_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        organization_id: Optional[str] = None,
        payment: Optional[Dict[str, Any]] = None,
        shipping: Optional[Dict[str, Any]] = None,
        shipping_address: Optional[Dict[str, Any]] = None,
        shipping_total: Optional[float] = None,
        user_data: Optional[Dict[str, Any]] = None
    ) -> OrderDetail:
        """
        

        Parameters
        ----------
        items : List[OrderItemCreateRequest]
            The order positions (at most 500).
        billing_address : Optional[Dict[str, Any]]
            Frozen billing address.
        buyer : Optional[Dict[str, Any]]
            Frozen buyer snapshot (name, email, …).
        cart_id : Optional[str]
            Source cart (the carts.order hand-over).
        channel_id : Optional[str]
            
        contact_id : Optional[str]
            Ordering customer contact.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        customer_order_number : Optional[str]
            The buyer's own order/PO number.
        grand_total : Optional[float]
            Override — computed as subtotal + shipping + tax when omitted.
        market_id : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        organization_id : Optional[str]
            B2B organization.
        payment : Optional[Dict[str, Any]]
            Frozen payment snapshot — a known 'payment.status' seeds payment_status (otherwise 'open').
        shipping : Optional[Dict[str, Any]]
            Frozen shipping snapshot — 'shipping.price' seeds shipping_total.
        shipping_address : Optional[Dict[str, Any]]
            Frozen shipping address.
        shipping_total : Optional[float]
            Shipping total (fallback when 'shipping.price' is absent).
        user_data : Optional[Dict[str, Any]]
            Free-form user data.
        
        Returns
        -------
        OrderDetail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/place'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')


        api_params['billing_address'] = self._normalize_value(billing_address)
        api_params['buyer'] = self._normalize_value(buyer)
        api_params['cart_id'] = self._normalize_value(cart_id)
        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['customer_order_number'] = self._normalize_value(customer_order_number)
        api_params['grand_total'] = self._normalize_value(grand_total)
        api_params['items'] = self._normalize_value(items)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['payment'] = self._normalize_value(payment)
        api_params['shipping'] = self._normalize_value(shipping)
        api_params['shipping_address'] = self._normalize_value(shipping_address)
        api_params['shipping_total'] = self._normalize_value(shipping_total)
        api_params['user_data'] = self._normalize_value(user_data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderDetail)


    def orders_get(
        self,
        id: str
    ) -> OrderDetail:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        OrderDetail
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=OrderDetail)


    def orders_update(
        self,
        id: str,
        billing_address: Optional[Dict[str, Any]] = None,
        buyer: Optional[Dict[str, Any]] = None,
        customer_order_number: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        shipping_address: Optional[Dict[str, Any]] = None,
        user_data: Optional[Dict[str, Any]] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        billing_address : Optional[Dict[str, Any]]
            
        buyer : Optional[Dict[str, Any]]
            
        customer_order_number : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        shipping_address : Optional[Dict[str, Any]]
            
        user_data : Optional[Dict[str, Any]]
            Free-form user data.
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if billing_address is not None:
            api_params['billing_address'] = self._normalize_value(billing_address)
        if buyer is not None:
            api_params['buyer'] = self._normalize_value(buyer)
        if customer_order_number is not None:
            api_params['customer_order_number'] = self._normalize_value(customer_order_number)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if shipping_address is not None:
            api_params['shipping_address'] = self._normalize_value(shipping_address)
        if user_data is not None:
            api_params['user_data'] = self._normalize_value(user_data)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_acknowledge(
        self,
        id: str,
        external_ref: Optional[str] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        external_ref : Optional[str]
            The fulfilling system's order reference (e.g. the ERP order number).
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/acknowledge'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if external_ref is not None:
            api_params['external_ref'] = self._normalize_value(external_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_cancel(
        self,
        id: str,
        cancelled_by: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        cancelled_by : Optional[str]
            Acting user/system.
        reason : Optional[str]
            
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/cancel'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if cancelled_by is not None:
            api_params['cancelled_by'] = self._normalize_value(cancelled_by)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_comments_list(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/comments'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def orders_comments_create(
        self,
        id: str,
        body: str,
        author: Optional[str] = None,
        visibility: Optional[OrderCommentVisibility] = None
    ) -> OrderComment:
        """
        

        Parameters
        ----------
        id : str
            
        body : str
            
        author : Optional[str]
            
        visibility : Optional[OrderCommentVisibility]
            Default 'internal'.
        
        Returns
        -------
        OrderComment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/comments'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if body is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if author is not None:
            api_params['author'] = self._normalize_value(author)
        api_params['body'] = self._normalize_value(body)
        if visibility is not None:
            api_params['visibility'] = self._normalize_value(visibility)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderComment)


    def orders_events_list(
        self,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/events'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def orders_hold(
        self,
        id: str,
        reason: Optional[str] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        reason : Optional[str]
            Why the order is blocked (shown on the shipping guard).
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/hold'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_items_cancel(
        self,
        id: str,
        positions: List[OrderCancelPosition],
        cancelled_by: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        positions : List[OrderCancelPosition]
            
        cancelled_by : Optional[str]
            Acting user/system.
        reason : Optional[str]
            
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/items/cancel'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if positions is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "positions"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if cancelled_by is not None:
            api_params['cancelled_by'] = self._normalize_value(cancelled_by)
        api_params['positions'] = self._normalize_value(positions)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_payment_status_update(
        self,
        id: str,
        status: OrderPaymentStatus,
        payment_id: Optional[str] = None
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        status : OrderPaymentStatus
            The new payment dimension value.
        payment_id : Optional[str]
            Reference into the payment system — merged into the order's payment snapshot.
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/payment-status'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if status is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "status"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if payment_id is not None:
            api_params['payment_id'] = self._normalize_value(payment_id)
        api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)


    def orders_return(
        self,
        id: str,
        positions: List[OrderReturnPosition],
        metadata: Optional[Dict[str, Any]] = None,
        reason: Optional[str] = None
    ) -> OrderReturn:
        """
        

        Parameters
        ----------
        id : str
            
        positions : List[OrderReturnPosition]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        reason : Optional[str]
            
        
        Returns
        -------
        OrderReturn
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/return'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if positions is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "positions"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        api_params['positions'] = self._normalize_value(positions)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderReturn)


    def orders_returns_complete(
        self,
        id: str,
        rid: str,
        resolution: Optional[str] = None
    ) -> OrderReturn:
        """
        

        Parameters
        ----------
        id : str
            
        rid : str
            
        resolution : Optional[str]
            How the return was settled (refund, replacement, …).
        
        Returns
        -------
        OrderReturn
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/complete'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "rid"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        if resolution is not None:
            api_params['resolution'] = self._normalize_value(resolution)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderReturn)


    def orders_returns_receive(
        self,
        id: str,
        rid: str,
        data: Dict[str, Any]
    ) -> OrderReturn:
        """
        

        Parameters
        ----------
        id : str
            
        rid : str
            
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        OrderReturn
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/receive'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "rid"')

        if data is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderReturn)


    def orders_returns_reject(
        self,
        id: str,
        rid: str,
        reason: Optional[str] = None,
        resolution: Optional[str] = None
    ) -> OrderReturn:
        """
        

        Parameters
        ----------
        id : str
            
        rid : str
            
        reason : Optional[str]
            Fallback for 'resolution'.
        resolution : Optional[str]
            Why the return was rejected.
        
        Returns
        -------
        OrderReturn
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/reject'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "rid"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        if resolution is not None:
            api_params['resolution'] = self._normalize_value(resolution)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderReturn)


    def orders_ship(
        self,
        id: str,
        carrier: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        number: Optional[str] = None,
        positions: Optional[List[OrderShipmentPosition]] = None,
        shipped_at: Optional[str] = None,
        tracking_code: Optional[str] = None,
        tracking_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        carrier : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        number : Optional[str]
            Delivery note number — drawn from the 'delivery' range when omitted.
        positions : Optional[List[OrderShipmentPosition]]
            Omitted = every position with open quantity, in full.
        shipped_at : Optional[str]
            Defaults to now.
        tracking_code : Optional[str]
            
        tracking_url : Optional[str]
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/ship'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if carrier is not None:
            api_params['carrier'] = self._normalize_value(carrier)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if number is not None:
            api_params['number'] = self._normalize_value(number)
        if positions is not None:
            api_params['positions'] = self._normalize_value(positions)
        if shipped_at is not None:
            api_params['shipped_at'] = self._normalize_value(shipped_at)
        if tracking_code is not None:
            api_params['tracking_code'] = self._normalize_value(tracking_code)
        if tracking_url is not None:
            api_params['tracking_url'] = self._normalize_value(tracking_url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def orders_unhold(
        self,
        id: str,
        data: Dict[str, Any]
    ) -> Order:
        """
        

        Parameters
        ----------
        id : str
            
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Order
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/orders/{id}/unhold'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        if data is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Order)

