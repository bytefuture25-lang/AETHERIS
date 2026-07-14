from app.gui.pages.dashboard_page import DashboardPage
from app.gui.pages.ai_chat_page import AIChatPage
from app.gui.pages.voice_page import VoicePage

NAV_ITEMS = [
    {
        "id": "dashboard",
        "title": "🏠 Dashboard",
        "page": DashboardPage,
    },
    {
        "id": "ai_chat",
        "title": "🤖 AI Chat",
        "page": AIChatPage,
    },
    {
        "id": "voice",
        "title": "🎤 Voice",
        "page": VoicePage,
    },
]