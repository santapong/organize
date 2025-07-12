from litestar import Litestar

from backend.config.middleware.CORS import cors_config
from backend.config.logs import logging_config

from backend.apis.v1 import api_v1_router

app = Litestar(route_handlers=[api_v1_router])