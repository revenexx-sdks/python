```python
from revenexx.client import Client
from revenexx.services.forms import Forms
from revenexx.models import Error
from revenexx.enums import FormSubmissionStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

forms = Forms(client)

result: Error = forms.forms_submissions_create(
    data = {
        "company": "Example GmbH",
        "email": "buyer@example.com",
        "message": "Please quote 200 units of ACME-4711-BLK, delivered to Hamburg."
    },
    form_id = '',
    form_slug = 'contact', # optional
    metadata = {}, # optional
    source = '/contact', # optional
    status = FormSubmissionStatus.NEW # optional
)

print(result.model_dump())
```
