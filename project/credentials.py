class Credentials:
    def __init__(self, clientId, clientSecret, accessToken, refreshToken):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.accessToken = accessToken
        self.refreshToken = refreshToken
        self.expires = 0