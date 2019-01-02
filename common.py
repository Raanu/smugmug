import json
from rauth import OAuth1Service
import sys
from six.moves.urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

OAUTH_ORIGIN = 'http://ranugupta.smugmug.com'
REQUEST_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getRequestToken'
ACCESS_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getAccessToken'
AUTHORIZE_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/authorize'
KEY = 'dkqJgVr5nsffz6chgp6Kcz2pmDgnsGPW'
SECRET = 'RFZTNPcSN7vKT54z6hCTMM5vWrPvfg5wC26f7zNcK64fS4gnTgVQNnxsKqsCV28t'


API_ORIGIN = 'http://api.smugmug.com'

SERVICE = None


def get_service():
    global SERVICE

    SERVICE = OAuth1Service(
        name='Ranu',
        consumer_key=KEY,
        consumer_secret=SECRET,
        request_token_url=REQUEST_TOKEN_URL,
        access_token_url=ACCESS_TOKEN_URL,
        authorize_url=AUTHORIZE_URL,
        base_url=API_ORIGIN + '/api/v2')
    return SERVICE


def add_auth_params(auth_url, access=None, permissions=None):
    if access is None and permissions is None:
        return auth_url
    parts = urlsplit(auth_url)
    query = parse_qsl(parts.query, True)
    if access is not None:
        query.append(('Access', access))
    if permissions is not None:
        query.append(('Permissions', permissions))
    return urlunsplit((
        parts.scheme,
        parts.netloc,
        parts.path,
        urlencode(query, True),
        parts.fragment))
		
