from litestar import Controller, get, patch, put, post, delete

# TODO: Wait for DTO
class ConversationController(Controller):
    """
    Using asking Agentic Model or Let Model Talk to eachother
    
    """
    path = "/Conversation"
    
    @get()
    async def get_conversation(self):
        return {}
    
    @post()
    async def talk_to_team(self):
        return {}