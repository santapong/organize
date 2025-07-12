from litestar.config.response_cache import ResponseCacheConfig
from litestar.stores.valkey import ValkeyStore

# Need to learn more.

valkey_store = ValkeyStore.with_client(port=6379, db=0)
cache_config = ResponseCacheConfig(store="valkey_backed_store")