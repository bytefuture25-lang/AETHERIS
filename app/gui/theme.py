"""
ÆTHERIS Theme System
"""

from PySide6.QtGui import QColor

# ----------------------------------------------------------
# Color Palette
# ----------------------------------------------------------

BACKGROUND = "#0F172A"
SURFACE = "#1E293B"

PRIMARY = "#00D4FF"

SUCCESS = "#22C55E"
WARNING = "#F59E0B"
ERROR = "#EF4444"

TEXT_PRIMARY = "#F8FAFC"
TEXT_SECONDARY = "#CBD5E1"

# ----------------------------------------------------------
# Window
# ----------------------------------------------------------

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WINDOW_TITLE = "ÆTHERIS"

# ----------------------------------------------------------
# Global Stylesheet
# ----------------------------------------------------------

STYLE_SHEET = f"""
QMainWindow {{
    background-color: {BACKGROUND};
}}

QWidget {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
    font-family: "Segoe UI";
    font-size: 11pt;
}}

QStatusBar {{
    background-color: {SURFACE};
    color: {TEXT_PRIMARY};
}}

QLabel {{
    color: {TEXT_PRIMARY};
}}

#Header {{
    background-color: #1E293B;
    border-bottom: 1px solid #334155;
}}

#AppTitle {{
    font-size: 22px;
    font-weight: 700;
    color: #00D4FF;
}}

#PageTitle {{
    font-size:30px;
    font-weight:700;
    color:#00D4FF;
}}

#PageSubtitle {{
    font-size:14px;
    color:#CBD5E1;
}}

#StatusCard {{
    background-color: #1E293B;
    border: 1px solid #334155;
    border-radius: 12px;
}}

#StatusCard:hover {{
    border: 1px solid #00D4FF;
}}

#CardTitle {{
    font-size: 12px;
    color: #CBD5E1;
}}

#CardValue {{
    font-size: 22px;
    font-weight: bold;
    color: #F8FAFC;
}}

#CardStatus {{
    font-size: 11px;
    color: #22C55E;
}}
"""
