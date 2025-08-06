# Need to make a Review agent.py using typhoon

import os 

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

TYPHOON_API_KEY = os.getenv("TYPHOON_API_KEY")

typhoon_model = ""



llm = init_chat_model(
    model=""
)