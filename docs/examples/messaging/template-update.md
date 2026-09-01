```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error
from revenexx.enums import MessageClass
from revenexx.enums import WhatsappCategory

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.template_update(
    id = '',
    body_html = '', # optional
    body_text = '', # optional
    content_sid = '', # optional
    design = [], # optional
    enabled = True, # optional
    layout_id = '', # optional
    markets = [], # optional
    message_class = MessageClass.TRANSACTIONAL, # optional
    subject = '', # optional
    test_mode = True, # optional
    title = '', # optional
    valid_from = '2026-01-01T12:00:00Z', # optional
    valid_until = '2026-01-01T12:00:00Z', # optional
    variable_defaults = [], # optional
    variables = [], # optional
    whatsapp_category = WhatsappCategory.MARKETING # optional
)

print(result.model_dump())
```
