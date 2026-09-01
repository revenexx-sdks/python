import io
import json
import os
import platform
import sys
import requests
from .input_file import InputFile
from .exception import RevenexxException
from .encoders.value_class_encoder import ValueClassEncoder

class Client:
    def __init__(self):
        self._chunk_size = 5*1024*1024
        self._self_signed = False
        self._endpoint = 'https://api.revenexx.com'
        self._global_headers = {
            'content-type': '',
            'user-agent' : f'RevenexxPythonSDK/0.0.2 ({platform.uname().system}; {platform.uname().version}; {platform.uname().machine})',
            'x-sdk-name': 'Revenexx Python',
            'x-sdk-platform': '',
            'x-sdk-language': 'python',
            'x-sdk-version': '0.0.2',
        }

    def set_self_signed(self, status=True):
        self._self_signed = status
        return self

    def set_endpoint(self, endpoint):
        if not endpoint.startswith('http://') and not endpoint.startswith('https://'):
            raise RevenexxException('Invalid endpoint URL: ' + endpoint)

        self._endpoint = endpoint
        return self

    def add_header(self, key, value):
        self._global_headers[key.lower()] = value
        return self

    def set_tenant(self, value):
        """The tenant slug your requests are scoped to, sent as the X-Revenexx-Tenant header on every request."""

        self._global_headers['x-revenexx-tenant'] = value
        return self

    def set_market(self, value):
        """The market slug to scope requests to, sent as the X-Revenexx-Market header. Optional - omit it to see only global rows."""

        self._global_headers['x-revenexx-market'] = value
        return self

    def set_api_key_auth(self, value):
        """A gateway-managed scoped API key (rvxk_…)."""

        self._global_headers['x-revenexx-api-key'] = value
        return self

    def set_bearer_auth(self, value):
        """A Zitadel-issued JWT (Cockpit / interactive callers)."""

        self._global_headers['authorization'] = value if value.lower().startswith('bearer ') else f'Bearer {value}'
        return self

    def call(self, method, path='', headers=None, params=None, response_type='json'):
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        data = {}
        files = {}
        stringify = False

        headers = {**self._global_headers, **headers}

        if method != 'get':
            data = params
            params = {}

        if headers['content-type'].startswith('application/json'):
            data = json.dumps(data, cls=ValueClassEncoder)

        if headers['content-type'].startswith('multipart/form-data'):
            del headers['content-type']
            stringify = True
            for key in data.copy():
                if isinstance(data[key], InputFile):
                    files[key] = (data[key].filename, data[key].data)
                    del data[key]
            data = self.flatten(data, stringify=stringify)

        response = None
        try:
            response = requests.request(  # call method dynamically https://stackoverflow.com/a/4246075/2299554
                method=method,
                url=self._endpoint + path,
                params=self.flatten(params, stringify=stringify),
                data=data,
                files=files,
                headers=headers,
                verify=(not self._self_signed),
                allow_redirects=False if response_type == 'location' else True
            )

            response.raise_for_status()

            warnings = response.headers.get('x-revenexx-warning')
            if warnings:
                for warning in warnings.split(';'):
                    print(f'Warning: {warning}', file=sys.stderr)

            content_type = response.headers['Content-Type']

            if response_type == 'location':
                return response.headers.get('Location')

            if content_type.startswith('application/json'):
                return response.json()

            return response._content
        except Exception as e:
            if response != None:
                content_type = response.headers['Content-Type']
                if content_type.startswith('application/json'):
                    raise RevenexxException(response.json()['message'], response.status_code, response.json().get('type'), response.text)
                else:
                    raise RevenexxException(response.text, response.status_code, None, response.text)
            else:
                raise RevenexxException(e)

    def chunked_upload(
        self,
        path,
        headers = None,
        params = None,
        param_name = '',
        on_progress = None,
        upload_id = ''
    ):
        # The API takes one multipart body per upload. It has no chunked or
        # resumable protocol — no content-range, no upload id, no per-chunk
        # endpoint — so the whole file always goes in a single request.
        input_file = params[param_name]

        if input_file.source_type == 'path':
            size = os.stat(input_file.path).st_size
            with open(input_file.path, 'rb') as input:
                input_file.data = input.read()
        elif input_file.source_type == 'bytes':
            size = len(input_file.data)

        params[param_name] = input_file

        result = self.call(
            'post',
            path,
            headers,
            params
        )

        if on_progress is not None:
            on_progress({
                "$id": result.get("$id") if isinstance(result, dict) else None,
                "progress": 100,
                "sizeUploaded": size,
                "chunksTotal": 1,
                "chunksUploaded": 1,
            })

        return result

    def flatten(self, data, prefix='', stringify=False):
        output = {}
        i = 0

        for key in data:
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + '[' + key +']' if prefix else key
            finalKey = prefix + '[' + str(i) +']' if isinstance(data, list) else finalKey
            i += 1

            if isinstance(value, list) or isinstance(value, dict):
                output = {**output, **self.flatten(value, finalKey, stringify)}
            else:
                if stringify:
                    output[finalKey] = str(value)
                else:
                    output[finalKey] = value

        return output
