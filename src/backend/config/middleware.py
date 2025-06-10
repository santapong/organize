from litestar.config.cors import CORSConfig

from src.backend.config.settings import SettingsAPI

origin = [
    SettingsAPI().origins
]

cors_config = CORSConfig(
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)