OVERRIDE_HTTP_HEADERS = {
    "X-Frame-Options": "ALLOWALL",
}
# Enable the embedded Superset feature
FEATURE_FLAGS = {
    “EMBEDDED_SUPERSET”: True
}

# Enable Cross-Origin Resource Sharing (CORS)
ENABLE_CORS = True
CORS_OPTIONS = {
    “supports_credentials”: True,
    “allow_headers”: “*”,
    “expose_headers”: “*”,
    “resources”: “*”,
    “origins”: []  # React URL or frontend URL
}

# Dashboard Embedding Configuration
GUEST_ROLE_NAME = “Gamma”
GUEST_TOKEN_JWT_SECRET = “PASTE_GENERATED_SECRET_HERE”  # Replace with a secure secret
GUEST_TOKEN_JWT_ALGO = “HS256”
GUEST_TOKEN_HEADER_NAME = “X-GuestToken”
GUEST_TOKEN_JWT_EXP_SECONDS = 300  # Token expiry time set to 5 minutes
