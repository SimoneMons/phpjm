from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext



class SHPConnection:
    # SharePoint connection
    sharepoint_base_url = 'https://acseittsa.sharepoint.com/teams/ITSEITT/'
    sharepoint_user = 'smontefiori@seittsa.es'
    sharepoint_password = 'David@202407'



    def __init__(self):
        print('Inside init SharePoint connection')

    def shp_conn(self):
        auth = AuthenticationContext(self.sharepoint_base_url)
        auth.acquire_token_for_user(self.sharepoint_user, self.sharepoint_password)
        ctx = ClientContext(self.sharepoint_base_url, auth)

        return ctx
