```python
from revenexx.client import Client
from revenexx.services.orders import Orders
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orders = Orders(client)

result: Error = orders.orders_update(
    id = '',
    billing_address = {
        "city": "Berlin",
        "company": "Beispiel Industrietechnik GmbH",
        "country": "DE",
        "name": "Anna Berger",
        "street": "Musterstra\u00dfe 12",
        "zip": "10115"
    }, # optional
    buyer = {
        "company": "Beispiel Industrietechnik GmbH",
        "customer_number": "K-10042",
        "email": "anna.berger@example.com",
        "name": "Anna Berger"
    }, # optional
    customer_order_number = 'PO-2026-0042', # optional
    metadata = {
        "erp_batch": "2026-W32"
    }, # optional
    shipping_address = {
        "city": "Berlin",
        "company": "Beispiel Industrietechnik GmbH",
        "country": "DE",
        "name": "Anna Berger",
        "street": "Musterstra\u00dfe 12",
        "zip": "10115"
    }, # optional
    user_data = {
        "campaign": "spring-catalogue",
        "source": "webshop"
    } # optional
)

print(result.model_dump())
```
