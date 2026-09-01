```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.enums import OrderStatus
from revenexx.enums import OrderPaymentStatus
from revenexx.enums import OrderFulfillmentStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result = orders.orders_list(
    id = '', # optional
    number = 'ORD-000123', # optional
    customer_order_number = 'PO-2026-0042', # optional
    external_ref = 'ERP-4711', # optional
    acknowledged_at = '2026-01-01T12:00:00Z', # optional
    cart_id = '', # optional
    contact_id = '', # optional
    organization_id = '', # optional
    channel_id = '', # optional
    currency = 'EUR', # optional
    status = OrderStatus.PENDING, # optional
    payment_status = OrderPaymentStatus.OPEN, # optional
    fulfillment_status = OrderFulfillmentStatus.UNFULFILLED, # optional
    on_hold = True, # optional
    hold_reason = 'Credit check pending', # optional
    item_count = 3, # optional
    subtotal = 149.7, # optional
    shipping_total = 5.9, # optional
    tax_total = 29.56, # optional
    grand_total = 185.16, # optional
    placed_at = '2026-01-01T12:00:00Z', # optional
    completed_at = '2026-01-01T12:00:00Z', # optional
    cancelled_at = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)
```
