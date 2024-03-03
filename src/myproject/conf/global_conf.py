TITLE = "My Project"
DESCRIPION = "My Project with sample protobuf API"

# Pymongo Databases Settings
# PYMONGO_DATABASES = {
# Pymongo Databases Settings
# PYMONGO_DATABASES = {
#     "default": {
#         "db_prefix": "dev2",
#         "username": "aurorastack",
#         "password": "password1234",
#         "host": "mongodb://localhost:27017",
#     },
#     "identity": {
#         "db": "identity",
#     },
# }

DATABASES = {
    "default": {
        "username": "aurorastack",
        "password": "password1234",
        "host": "mongodb://localhost:27017",
    }
}

# Cache Settings
CACHES = {
    "default": {},
    "local": {
        "backend": "aurorastack.core.cache.local_cache.LocalCache",
        "max_size": 128,
        "ttl": 300,
    },
}

# Handler Settings
HANDLERS = {
    # "authentication": [{
    #     "backend": "aurorastack.core.handler.authentication_handler:AuroraStackAuthenticationHandler"
    # }],
    # "authorization": [{
    #     "backend": "aurorastack.core.handler.authorization_handler:AuroraStackAuthorizationHandler"
    # }],
    # "mutation": [{
    #     "backend": "aurorastack.core.handler.mutation_handler:AuroraStackMutationHandler"
    # }],
    # "event": []
}

# Log Settings
LOG = {"filters": {"masking": {"rules": {}}}}

# Connector Settings
CONNECTORS = {
    "AuroraConnector": {
        "backend": "aurorastack.core.connector.space_connector:AuroraConnector",
        "endpoints": {
            "identity": "grpc://localhost:50051",
        },
    },
}

# Endpoint Settings
ENDPOINTS = [
    # {
    #     "service": "identity",
    #     "name": "Identity Service",
    #     "endpoint": "grpc://<endpoint>>:<port>"
    # },
]

# System Token Settings
TOKEN = ""
