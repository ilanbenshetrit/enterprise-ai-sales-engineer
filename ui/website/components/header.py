"""
SixStage Corporate Header — Datadog-Style Navigation

Mirrors datadoghq.com's exact top-level taxonomy: Product, Customers,
Pricing, Solutions, About, Blog, Docs, Login, then a Get Started button.
Product/Solutions/About open a hover panel (mega or simple dropdown);
Customers/Pricing/Blog/Docs/Login are plain links, matching Datadog's
own mix of dropdown vs. direct nav items.
"""

import streamlit as st

from components.logo import kf_logo_lockup


_MEGA_MENU = [
    {
        "label": "Product",
        "href": "/security",
        "links": [
            ("Overview", "/security"),
            ("Continuous Scanning", "/security-scanning"),
            ("Posture & Risk Analysis", "/security-posture"),
            ("AI Copilot Triage", "/security-copilot"),
            ("Alerting & Remediation", "/security-alerting"),
            ("AI & Identity Security", "/security-ai"),
            ("CI/CD & Cloud Integration", "/security-integrations"),
            ("How It Works — Hybrid Model", "/how-it-works"),
            ("Live Security Console", "/security-console"),
        ],
        "highlight_label": "Our Flagship Platform",
        "highlight_text": (
            "Continuous, AI-assisted security for CI/CD pipelines, "
            "Kubernetes, containers, and cloud."
        ),
        "highlight_href": "/security-console",
        "highlight_cta": "Open the Live Console",
    },
    {
        "label": "Solutions",
        "href": "/solutions",
        "links": [
            ("Solutions Overview", "/solutions"),
            ("Technology", "/technology"),
            ("AI Sales Engineer", "/platform"),
            ("Live Platform Demo", "/demo"),
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
        "label": "About",
        "href": "/company",
        "links": [
            ("About SixStage", "/company"),
            ("Contact Us", "/contact"),
        ],
    },
]

_SIMPLE_LINKS = [
    ("Customers", "/customers"),
    ("Pricing", "/pricing"),
    ("Blog", "/blog"),
    ("Docs", "/docs"),
    ("Login", "/security-console"),
]


def _render_mega_items() -> str:

    items_html = ""
    for cat in _MEGA_MENU:

        links_html = "".join(
            f'<a class="kf-mega-link" href="{href}" target="_self">{label}</a>'
            for label, href in cat["links"]
        )

        has_highlight = "highlight_label" in cat

        if has_highlight:
            panel_inner = f"""
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
            """
            panel_style = "grid-template-columns: 1.15fr 1fr; width: 560px;"
        else:
            panel_inner = f"""
                <div class="kf-mega-links">
                    {links_html}
                </div>
            """
            panel_style = "grid-template-columns: 1fr; width: 220px;"

        items_html += f"""
        <div class="kf-menu-item-wrap">
            <a class="kf-item" href="{cat['href']}" target="_self">
                {cat['label']}
                <span class="kf-item-chevron">&#9662;</span>
            </a>
            <div class="kf-mega-panel" style="{panel_style}">
                {panel_inner}
            </div>
        </div>
        """

    return items_html


def _render_simple_links() -> str:

    return "".join(
        f'<a class="kf-item kf-item-simple" href="{href}" target="_self">{label}</a>'
        for label, href in _SIMPLE_LINKS
    )


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
        .kf-logo-dark {{
            font-weight: 800;
            letter-spacing: -1px;
            background: linear-gradient(90deg, #9333ea, #0284c7, #059669);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 1px 1px rgba(15,23,42,0.12);
        }}
        .kf-announcement {{
            width: calc(100% + 10rem);
            margin: -3rem -5rem 0 -5rem;
            background: linear-gradient(90deg, #f3e8ff, #dbeafe, #d1fae5);
            text-align: center;
            padding: 9px 5rem;
            font-size: 13px;
            font-weight: 600;
            color: #1A2E5C;
            position: relative;
            z-index: 101;
        }}
        .kf-announcement a {{
            color: #7C3AED;
            font-weight: 800;
            text-decoration: none;
            margin-left: 6px;
        }}
        .kf-announcement a:hover {{
            text-decoration: underline;
        }}
        .kf-header {{
            width: calc(100% + 10rem);
            margin: 0 -5rem 0 -5rem;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 34px;
            padding: 22px 5rem;
            background: #FFFCF5;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .kf-header-logo {{
            flex-shrink: 0;
        }}
        .kf-menu {{
            display: flex;
            gap: 30px;
            align-items: center;
        }}
        .kf-menu-item-wrap {{
            position: relative;
        }}
        .kf-item {{
            color: #0A1628;
            font-size: 15px;
            font-weight: 600;
            text-decoration: none !important;
            border-bottom: none !important;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 2px;
            transition: color 0.2s ease;
        }}
        .kf-item-chevron {{
            font-size: 10px;
            opacity: 0.6;
            color: #7C3AED;
            transition: transform 0.2s ease;
        }}
        .kf-menu-item-wrap:hover .kf-item,
        .kf-item-simple:hover {{
            color: #7C3AED;
        }}
        .kf-menu-item-wrap:hover .kf-item-chevron {{
            transform: rotate(180deg);
            opacity: 1;
        }}

        /* Mega panel — solid white card so it stays readable no matter
           what scrolls behind it (the page below the sticky header is
           dark), and reads as floating above the page like Datadog's */

        .kf-mega-panel {{
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%) translateY(8px);
            display: grid;
            gap: 24px;
            padding: 26px 24px;
            margin-top: 14px;
            background: #FFFFFF;
            border-radius: 16px;
            box-shadow: 0 24px 60px rgba(15,23,42,0.22), 0 4px 16px rgba(15,23,42,0.1);
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s;
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
            gap: 4px;
        }}
        .kf-mega-link {{
            color: #0A1628;
            text-decoration: none !important;
            font-size: 14px;
            font-weight: 600;
            padding: 8px 4px;
            transition: color 0.2s ease, transform 0.2s ease;
            display: inline-block;
        }}
        .kf-mega-link:hover {{
            color: #7C3AED;
            transform: translateX(4px);
        }}
        .kf-mega-highlight {{
            padding: 8px 4px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            border-left: 2px solid rgba(124,58,237,0.3);
            padding-left: 20px;
        }}
        .kf-mega-highlight-label {{
            color: #7C3AED;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .kf-mega-highlight-text {{
            color: rgba(15,23,42,0.7);
            font-size: 13px;
            line-height: 1.6;
            margin-bottom: 16px;
        }}
        .kf-mega-highlight-cta {{
            color: #0A1628;
            font-size: 13px;
            font-weight: 800;
            text-decoration: none !important;
            transition: color 0.2s ease, transform 0.2s ease;
            display: inline-block;
        }}
        .kf-mega-highlight-cta:hover {{
            color: #7C3AED;
            transform: translateX(4px);
        }}
        .kf-header-cta {{
            flex-shrink: 0;
            display: inline-block;
            padding: 10px 24px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 700;
            color: white;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            text-decoration: none !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .kf-header-cta:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 24px rgba(124,58,237,0.25);
        }}
        </style>
        <div class="kf-announcement">
            Stage 12 is live — self-serve tenants with a real API key, today.
            <a href="/get-started" target="_self">Create your workspace &rarr;</a>
        </div>
        <div class="kf-header">
            <div class="kf-header-logo">{kf_logo_lockup(size=84, wordmark_size="52px", wordmark_class="kf-logo-dark", on_light=True)}</div>
            <div class="kf-menu">
                {_render_mega_items()}
                {_render_simple_links()}
            </div>
            <a class="kf-header-cta" href="/get-started" target="_self">Get Started</a>
        </div>
        """,
        unsafe_allow_html=True
    )
