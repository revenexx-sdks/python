```python
from revenexx.client import Client
from revenexx.services.forms import Forms
from revenexx.models import Error
from revenexx.enums import FormSubmissionStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

forms = Forms(client)

result: Error = forms.forms_submissions_list(
    id = '', # optional
    form_id = '', # optional
    form_slug = 'contact', # optional
    source = '/contact', # optional
    status = FormSubmissionStatus.NEW, # optional
    created_at = '2026-01-31T09:15:00Z', # optional
    updated_at = '2026-01-31T09:15:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
