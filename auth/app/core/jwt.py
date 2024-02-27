from jwt import JWT, jwk_from_pem
import time
import sys
import os

def generate_jwt():
    with open('github.private-key.pem', 'rb') as pem_file:
        signing_key = jwk_from_pem(pem_file.read())

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 300,
        # GitHub App's identifier
        'iss': os.getenv('GITHUB_APP_ID')
    }

    # Create JWT
    jwt_instance = JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')
    return encoded_jwt