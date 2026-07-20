"""
Homepage Promo Carousel — Datadog-style rotator below the hero

Reuses the same pure-CSS crossfade pattern as the hero spotlight, as a
distinct strip of real, current updates (not fabricated news).
"""

import streamlit as st


_PROMOS = [
    {
        "label": "Now Live",
        "title": "Stage 12: Multi-Tenant SaaS Foundation",
        "desc": "Self-serve registration with a real, isolated workspace and a live API key.",
        "href": "/get-started",
        "cta": "Create Your Workspace",
    },
    {
        "label": "New Scanners",
        "title": "AI & Identity Security",
        "desc": "Coverage for prompt injection, exposed machine credentials, and MCP server risk.",
        "href": "/security-ai",
        "cta": "See What's Covered",
    },
    {
        "label": "Not a Demo",
        "title": "The Real Product, Running Live",
        "desc": "The Live Console embeds our actual backend — the same one your team would run.",
        "href": "/security-console",
        "cta": "Open the Live Console",
    },
    {
        "label": "For Developers",
        "title": "API Docs",
        "desc": "Register once, pass your key, and every request is scoped to your tenant only.",
        "href": "/docs",
        "cta": "Read the Docs",
    },
]


def render_promo_carousel():

    n = len(_PROMOS)
    slides_html = ""
    for i, p in enumerate(_PROMOS):
        delay = i * (20 / n)
        slides_html += f"""
        <a class="kf-promo-slide" href="{p['href']}" target="_self" style="animation-delay:{delay}s;">
            <div class="kf-promo-label">{p['label']}</div>
            <div class="kf-promo-title">{p['title']}</div>
            <div class="kf-promo-desc">{p['desc']}</div>
            <div class="kf-promo-cta">{p['cta']} &rarr;</div>
        </a>
        """

    st.markdown(
        f"""
        <style>
        .kf-promo-strip {{
            position: relative;
            max-width: 1050px;
            min-height: 150px;
            margin: 0 auto 90px;
            border-radius: 20px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
        }}
        .kf-promo-slide {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 30px 60px;
            text-decoration: none;
            color: inherit;
            opacity: 0;
            animation: kfPromoFade 20s infinite;
        }}
        @keyframes kfPromoFade {{
            0% {{ opacity: 0; }}
            2% {{ opacity: 1; }}
            23% {{ opacity: 1; }}
            26% {{ opacity: 0; }}
            100% {{ opacity: 0; }}
        }}
        .kf-promo-label {{
            color: #34d399;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .kf-promo-title {{
            font-size: 22px;
            font-weight: 800;
            color: white;
            margin-bottom: 8px;
        }}
        .kf-promo-desc {{
            font-size: 14px;
            color: rgba(255,255,255,0.7);
            max-width: 560px;
            margin-bottom: 12px;
        }}
        .kf-promo-cta {{
            font-size: 13px;
            font-weight: 700;
            color: #38bdf8;
            transition: 0.2s;
        }}
        .kf-promo-slide:hover .kf-promo-cta {{
            color: #c084fc;
            transform: translateX(2px);
        }}
        </style>
        <div class="kf-promo-strip">
            {slides_html}
        </div>
        """,
        unsafe_allow_html=True
    )
