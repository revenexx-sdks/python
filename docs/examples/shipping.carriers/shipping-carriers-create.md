```python
from revenexx.client import Client
from revenexx.services.shipping_carriers import ShippingCarriers
from revenexx.models import Error
from revenexx.enums import ShippingCarrierStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

shipping_carriers = ShippingCarriers(client)

result: Error = shipping_carriers.shipping_carriers_create(
    code = 'acme-parcel',
    name = 'Acme Parcel',
    countries = ["DE","AT","CH"], # optional
    cutoff_time = '16:00', # optional
    eta_days_max = 1, # optional
    eta_days_min = 1, # optional
    handling_days = 1, # optional
    labels = {
        "de": "Acme Paketdienst",
        "en": "Acme Parcel"
    }, # optional
    metadata = {
        "contract": "ACME-2026",
        "customer_number": "4711"
    }, # optional
    position = 1, # optional
    service_level = 'express', # optional
    status = ShippingCarrierStatus.ACTIVE, # optional
    tracking_url_template = 'https://track.example.com/parcels/{tracking_code}' # optional
)

print(result.model_dump())
```
