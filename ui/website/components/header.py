"""
SixStage Corporate Header — Full Mega-Menu Navigation

Structured like a large enterprise site's nav (categories that reveal
a wide panel of sub-links plus a highlight/CTA panel on hover),
scaled to SixStage's actual page count rather than padded out with
filler links.
"""

import streamlit as st

from components.logo import kf_logo_lockup


_MEGA_MENU = [
    {
        "label": "Security Platform",
        "href": "/security",
        "links": [
            ("Overview", "/security"),
            ("Continuous Scanning", "/security-scanning"),
            ("Posture & Risk Analysis", "/security-posture"),
            ("AI Copilot Triage", "/security-copilot"),
            ("Alerting & Remediation", "/security-alerting"),
            ("CI/CD & Cloud Integration", "/security-integrations"),
        ],
        "highlight_label": "Our Flagship Platform",
        "highlight_text": (
            "Continuous, AI-assisted security for CI/CD pipelines, "
            "Kubernetes, containers, and cloud."
        ),
        "highlight_href": "/security",
        "highlight_cta": "Explore the Security Platform",
    },
    {
        "label": "AI Sales Engineer",
        "href": "/platform",
        "links": [
            ("Overview", "/platform"),
            ("Live Platform Demo", "/demo"),
        ],
        "highlight_label": "One AI Engine",
        "highlight_text": (
            "Six stages of enterprise technical sales, from opportunity "
            "intelligence to a delivered solution package."
        ),
        "highlight_href": "/platform",
        "highlight_cta": "See How It Works",
    },
    {
        "label": "Solutions",
        "href": "/solutions",
        "links": [
            ("Solutions Overview", "/solutions"),
            ("Technology", "/technology"),
        ],
        "highlight_label": "Built On",
        "highlight_text": (
            "An enterprise knowledge layer and retrieval-grounded "
            "reasoning engine behind every capability we ship."
        ),
        "highlight_href": "/technology",
        "highlight_cta": "See the Technology",
    },
    {
        "label": "Company",
        "href": "/company",
        "links": [
            ("About SixStage", "/company"),
            ("Contact Us", "/contact"),
        ],
        "highlight_label": "Our Story",
        "highlight_text": (
            "Built by engineers who got tired of manual work — how "
            "SixStage started and where it's headed."
        ),
        "highlight_href": "/company",
        "highlight_cta": "Learn Our Story",
    },
]


def _render_mega_items() -> str:

    items_html = ""
    for cat in _MEGA_MENU:

        links_html = "".join(
            f'<a class="kf-mega-link" href="{href}" target="_self">{label}</a>'
            for label, href in cat["links"]
        )

        items_html += f"""
        <div class="kf-menu-item-wrap">
            <a class="kf-item" href="{cat['href']}" target="_self">
                {cat['label']}
                <span class="kf-item-chevron">&#9662;</span>
            </a>
            <div class="kf-mega-panel">
                <div class="kf-mega-links">
                    {links_html}
                </div>
                <div class="kf-mega-highlight">
                    <div class="kf-mega-highlight-label">{cat['highlight_label']}</div>
                    <div class="kf-mega-highlight-text">{cat['highlight_text']}</div>
                    <a class="kf-mega-highlight-cta" href="{cat['highlight_href']}" target="_self">
                    {cat['highlight_cta']} &rarr;
                    </a>
                </div>
            </div>
        </div>
        """

    return items_html


def render_header():

    st.markdown(
        f"""
        <style>
        .kf-logo {{
            font-weight: 800;
            letter-spacing: -1px;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .kf-header {{
            width: 100%;
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: center;
            padding: 20px 0px;
            margin-bottom: 60px;
            position: relative;
            z-index: 100;
        }}
        .kf-header-logo {{
            grid-column: 1;
            justify-self: start;
        }}
        .kf-menu {{
            grid-column: 2;
            justify-self: center;
            display: flex;
            gap: 38px;
            align-items: center;
        }}
        .kf-header-spacer {{
            grid-column: 3;
        }}
        .kf-menu-item-wrap {{
            position: relative;
        }}
        .kf-item {{
            color: rgba(255,255,255,0.85);
            font-size: 15px;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 2px;
            text-shadow:
                1px 1px 0 rgba(192,132,252,0.35),
                2px 2px 0 rgba(56,189,248,0.25),
                3px 3px 6px rgba(0,0,0,0.25);
            transition: transform 0.25s ease, color 0.25s ease, text-shadow 0.25s ease;
        }}
        .kf-item-chevron {{
            font-size: 10px;
            opacity: 0.6;
            transition: transform 0.25s ease;
        }}
        .kf-menu-item-wrap:hover .kf-item {{
            color: white;
            transform: scale(1.1) translateY(-2px);
            text-shadow:
                1px 1px 0 rgba(192,132,252,0.6),
                2px 2px 0 rgba(56,189,248,0.5),
                3px 3px 0 rgba(52,211,153,0.4),
                4px 6px 10px rgba(0,0,0,0.35);
        }}
        .kf-menu-item-wrap:hover .kf-item-chevron {{
            transform: rotate(180deg);
            opacity: 1;
        }}

        /* Mega panel */

        .kf-mega-panel {{
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(8px);
            width: 560px;
            display: grid;
            grid-template-columns: 1.15fr 1fr;
            gap: 24px;
            background: rgba(15,23,42,0.98);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 18px;
            padding: 26px;
            margin-top: 14px;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s;
            box-shadow: 0 30px 60px rgba(0,0,0,0.5);
            z-index: 200;
        }}
        .kf-menu-item-wrap:hover .kf-mega-panel {{
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
            transform: translateX(-50%) translateY(0);
        }}
        .kf-mega-links {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}
        .kf-mega-link {{
            color: rgba(255,255,255,0.82);
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            padding: 10px 12px;
            border-radius: 10px;
            transition: 0.2s;
        }}
        .kf-mega-link:hover {{
            background: rgba(255,255,255,0.06);
            color: #38bdf8;
            padding-left: 16px;
        }}
        .kf-mega-highlight {{
            background: linear-gradient(
                135deg,
                rgba(192,132,252,0.14),
                rgba(56,189,248,0.14),
                rgba(52,211,153,0.14)
            );
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}
        .kf-mega-highlight-label {{
            color: #38bdf8;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .kf-mega-highlight-text {{
            color: rgba(255,255,255,0.85);
            font-size: 13px;
            line-height: 1.6;
            margin-bottom: 16px;
        }}
        .kf-mega-highlight-cta {{
            color: white;
            font-size: 13px;
            font-weight: 700;
            text-decoration: none;
        }}
        .kf-mega-highlight-cta:hover {{
            color: #38bdf8;
        }}
        </style>
        <div class="kf-header">
            <div class="kf-header-logo">{kf_logo_lockup()}</div>
            <div class="kf-menu">
                {_render_mega_items()}
            </div>
            <div class="kf-header-spacer"></div>
        </div>
        """,
        unsafe_allow_html=True
    )
