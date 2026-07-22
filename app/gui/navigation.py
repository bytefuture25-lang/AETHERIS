from app.gui.pages.dashboard_page import DashboardPage
from app.gui.pages.ai_chat_page import AIChatPage
from app.gui.pages.voice_page import VoicePage
from app.gui.pages.performance_page import PerformancePage

NAV_ITEMS = [

    {
        "id": "dashboard",
        "title": "Dashboard",
        "icon": "dashboard",
        "page": DashboardPage,
    },

    {
        "id": "ai_chat",
        "title": "AI Chat",
        "icon": "ai",
        "page": AIChatPage,
    },

    {
        "id": "voice",
        "title": "Voice",
        "icon": "microphone",
        "page": VoicePage,
    },

    {
        "id": "performance",
        "title": "Performance",
        "icon": "cpu",
        "page": PerformancePage,
    }

]
