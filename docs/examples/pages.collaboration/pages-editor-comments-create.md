```python
from revenexx.client import Client
from revenexx.services.pages_collaboration import PagesCollaboration
from revenexx.models import PageCommentList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_collaboration = PagesCollaboration(client)

result: PageCommentList = pages_collaboration.pages_editor_comments_create(
    page_id = '',
    body = '<p>Please shorten this headline.</p>',
    block_uuids = [], # optional
    parent_uuid = '' # optional
)

print(result.model_dump())
```
