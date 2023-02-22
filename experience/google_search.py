from googleapiclient.discovery import build
import pprint

API_KEY = "AIzaSyCsBmUzB-KWShCbWHCWTOKSYbGjHFd8s2M"
CSE_ID = "361ef2027456b4ed6"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
