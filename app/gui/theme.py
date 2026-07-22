"""
ÆTHERIS Theme System
Professional Theme v2
"""

from app.gui.design_system import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,
    PRIMARY, PRIMARY_HOVER, SUCCESS, WARNING, ERROR,
    BACKGROUND, SURFACE, CARD,
    TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED,
    BORDER,
    RADIUS_SMALL, RADIUS_MEDIUM, RADIUS_LARGE,
    TITLE, SUBTITLE, HEADING, BODY, SMALL, FONT,
)

STYLE_SHEET = f"""
QMainWindow {{
    background-color: {BACKGROUND};
}}

QWidget {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
    font-family: "{FONT}";
    font-size: {BODY}px;
}}

QStatusBar {{
    background-color: {SURFACE};
    color: {TEXT_PRIMARY};
    border-top: 1px solid {BORDER};
}}

QLabel {{
    color: {TEXT_PRIMARY};
}}

#Header {{
    background-color: {SURFACE};
    border-bottom: 1px solid {BORDER};
}}

#AppTitle {{ font-size:22px; font-weight:bold; color:{PRIMARY}; }}
#AppSubtitle {{ font-size:{SMALL}px; color:{TEXT_MUTED}; }}
#HeaderLabel {{ font-size:{SMALL}px; color:{TEXT_MUTED}; }}
#HeaderValue {{ font-size:{BODY}px; font-weight:bold; color:{PRIMARY}; }}
#HeaderVersion {{ font-size:{SMALL}px; color:{TEXT_SECONDARY}; }}
#HeaderStatus {{ font-size:{BODY}px; font-weight:bold; color:{SUCCESS}; }}

#Sidebar {{
    background-color:{SURFACE};
    border-right:1px solid {BORDER};
}}

#SidebarLogo {{ font-size:24px; font-weight:bold; color:{PRIMARY}; }}
#SidebarTitle {{ font-size:{BODY}px; font-weight:bold; color:{TEXT_SECONDARY}; }}
#SidebarFooter {{ font-size:{SMALL}px; color:{TEXT_MUTED}; }}

QPushButton#NavButton {{
    background-color:{CARD};
    border:1px solid {BORDER};
    border-radius:{RADIUS_MEDIUM}px;
    text-align:left;
    padding:12px 16px;
}}

QPushButton#NavButton:hover {{
    border:1px solid {PRIMARY};
    background:#162033;
}}

QPushButton#NavButton[active="true"] {{
    background:{PRIMARY};
    color:black;
    font-weight:bold;
}}

#WelcomeBanner {{
    background-color:{SURFACE};
    border:1px solid {BORDER};
    border-radius:{RADIUS_LARGE}px;
}}

#BannerTitle {{ font-size:{TITLE}px; font-weight:bold; }}
#BannerSubtitle {{ font-size:{BODY}px; color:{TEXT_MUTED}; }}

#BannerInfo {{
    background-color:{CARD};
    border:1px solid {BORDER};
    border-radius:{RADIUS_SMALL}px;
    padding:6px 12px;
}}

#StatusGrid {{ background:transparent; }}

#StatusCard {{
    background-color:{CARD};
    border:1px solid {BORDER};
    border-radius:{RADIUS_MEDIUM}px;
}}

#StatusCard:hover {{ border:1px solid {PRIMARY}; }}

#CardIcon {{ font-size:18px; }}
#CardTitle {{ font-size:{BODY}px; font-weight:bold; color:{TEXT_SECONDARY}; }}
#CardValue {{ font-size:26px; font-weight:bold; color:{TEXT_PRIMARY}; }}
#CardStatus {{ font-size:{SMALL}px; color:{TEXT_MUTED}; }}

QProgressBar#CardProgress {{
    border:none;
    border-radius:4px;
    background:{SURFACE};
    height:8px;
}}

QProgressBar#CardProgress::chunk {{
    background:{PRIMARY};
    border-radius:4px;
}}

#ActivityPanel {{
    background:{CARD};
    border:1px solid {BORDER};
    border-radius:{RADIUS_MEDIUM}px;
}}

#ActivityTitle {{
    font-size:{HEADING}px;
    font-weight:bold;
    color:{PRIMARY};
}}

QTextEdit {{
    background:{SURFACE};
    border:none;
    border-radius:{RADIUS_SMALL}px;
    color:{TEXT_PRIMARY};
    padding:10px;
}}

#PageTitle {{ font-size:30px; font-weight:bold; color:{PRIMARY}; }}
#PageSubtitle {{ font-size:{BODY}px; color:{TEXT_SECONDARY}; }}

#SystemInfo {{
    background-color: {CARD};
    border: 1px solid {BORDER};
    border-radius: {RADIUS_MEDIUM}px;
}}

#SystemInfoTitle {{
    font-size: {HEADING}px;
    font-weight: bold;
    color: {PRIMARY};
}}

#InfoLabel {{
    color: {TEXT_MUTED};
    font-size: {BODY}px;
}}

#InfoValue {{
    color: {TEXT_PRIMARY};
    font-size: {BODY}px;
    font-weight: bold;
}}

#ClockTime {{
    font-size: 18px;
    font-weight: bold;
    color: {PRIMARY};
}}

#ClockDate {{
    font-size: 11px;
    color: {TEXT_MUTED};
}}

/* ==========================================
   Chat Header
========================================== */

#ChatHeader {{
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 12px;
}}

#ChatHeaderTitle {{
    font-size: 18px;
    font-weight: bold;
    color: #00D4FF;
}}

#ChatHeaderModel {{
    color: #CBD5E1;
    font-size: 12px;
}}

#ChatHeaderStatus {{
    color: #22C55E;
    font-weight: bold;
}}

/* ==========================================
   CHAT HISTORY
========================================== */

#ChatHistory {{

    background: #111827;

    border: 1px solid #334155;

    border-radius: 14px;
}}

/* ==========================================
   Chat Input
========================================== */

#ChatInput {{
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 12px;
}}

QTextEdit {{
    background-color: #0F172A;
    border: 1px solid #334155;
    border-radius: 8px;
    color: #F8FAFC;
    padding: 8px;
}}

#PrimaryButton {{
    background-color: #00D4FF;
    color: #0F172A;
    border: none;
    border-radius: 8px;
    padding: 10px 18px;
    font-weight: bold;
}}

#PrimaryButton:hover {{
    background-color: #38BDF8;
}}

/* ==========================================
   MESSAGE BUBBLES
========================================== */

#UserBubble {{

    background:#22D3EE;

    border-radius:18px;

    margin:6px;
}}

#UserBubble QLabel{{

    color:#04121C;

    background:transparent;

    font-size:14px;
}}


#AIBubble {{

    background-color:{SURFACE};

    border:1px solid {BORDER};

    border-radius:{RADIUS_MEDIUM}px;

    margin:6px;
}}

#AIBubble QLabel{{

    color:white;

    background:transparent;

    font-size:14px;
}}

QPushButton {{
    border: {BORDER};
    border-radius: 8px;
    padding: 4px 10px;
    background: rgba(255,255,255,0.08);
}}

QPushButton:hover {{
    background: rgba(255,255,255,0.15);
}}

QPushButton:pressed {{
    background: rgba(255,255,255,0.25);
}}

#BubbleCopyButton {{
    border: none;
    border-radius: 8px;
    padding: 4px 10px;
    background-color: #334155;
    color: #F8FAFC;
}}

#BubbleCopyButton:hover {{
    background-color: #475569;
}}

#BubbleCopyButton:disabled {{
    background-color: #1E293B;
    color: #94A3B8;
}}
"""