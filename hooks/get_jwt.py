#!/usr/bin/env python3
import jwt
import time
import sys
import base64

# Get the content (base64 encoded) of PEM
if len(sys.argv) > 1:
    pem_content_b64 = sys.argv[1]
else:
    raise Exception("Missing PEM content")

# Get the App ID
if len(sys.argv) > 2:
    app_id = sys.argv[2]
else:
    raise Exception("Missing App ID")

# Open PEM
content = base64.b64decode(pem_content_b64)
signing_key = jwt.jwk_from_pem(content)

payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minutes maximum)
    'exp': int(time.time()) + 600,
    # GitHub App's identifier
    'iss': app_id
}

# Create JWT
jwt_instance = jwt.JWT()
encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

# JWT=$(python3 get_jwt.py $PEM_CONTENT_B64 $APP_ID)
print(encoded_jwt)
