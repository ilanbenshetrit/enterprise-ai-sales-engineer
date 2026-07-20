"""
SixStage Website Footer — Rich Multi-Column Directory (Datadog-style)
"""

import streamlit as st

from components.logo import kf_logo_lockup


_COLUMNS = [
    {
        "title": "Product",
        "links": [
            ("Overview", "/security"),
            ("Continuous Scanning", "/security-scanning"),
            ("Posture & Risk Analysis", "/security-posture"),
            ("AI Copilot Triage", "/security-copilot"),
            ("Alerting & Remediation", "/security-alerting"),
            ("AI & Identity Security", "/security-ai"),
            ("Live Security Console", "/security-console"),
        ],
    },
    {
        "title": "Resources",
        "links": [
            ("Pricing", "/pricing"),
            ("Docs", "/docs"),
            ("How It Works", "/how-it-works"),
            ("Get Started", "/get-started"),
            ("Customers", "/customers"),
        ],
    },
    {
        "title": "Solutions",
        "links": [
            ("Solutions Overview", "/solutions"),
            ("Technology", "/technology"),
            ("AI Sales Engineer", "/platform"),
            ("Live Platform Demo", "/demo"),
        ],
    },
    {
        "title": "Company",
        "links": [
            ("About SixStage", "/company"),
            ("Blog", "/blog"),
            ("Contact Us", "/contact"),
        ],
    },
]


def render_footer():

    columns_html = "".join(
        f"""
        <div class="kf-footer-col">
            <div class="kf-footer-col-title">{col['title']}</div>
            {''.join(f'<a href="{href}" target="_self" class="kf-footer-link">{label}</a>' for label, href in col['links'])}
        </div>
        """
        for col in _COLUMNS
    )

    st.markdown(
        f"""
        <style>
        .kf-footer {{
            border-top: 1px solid rgba(255,255,255,0.08);
            margin-top: 100px;
            padding: 60px 0 30px;
        }}
        .kf-footer-grid {{
            display: grid;
            grid-template-columns: 1.2fr repeat(4, 1fr);
            gap: 32px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .kf-footer-brand-desc {{
            color: rgba(255,255,255,0.55);
            font-size: 14px;
            line-height: 1.7;
            margin-top: 16px;
            max-width: 260px;
        }}
        .kf-footer-col-title {{
            color: white;
            font-size: 13px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            margin-bottom: 18px;
        }}
        .kf-footer-link {{
            display: block;
            color: rgba(255,255,255,0.6);
            font-size: 14px;
            text-decoration: none;
            margin-bottom: 12px;
            transition: color 0.2s ease;
        }}
        .kf-footer-link:hover {{
            color: #38bdf8;
        }}
        .kf-footer-bottom {{
            max-width: 1200px;
            margin: 50px auto 0;
            padding-top: 24px;
            border-top: 1px solid rgba(255,255,255,0.06);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .kf-footer-copyright {{
            color: rgba(255,255,255,0.45);
            font-size: 13px;
        }}
        </style>
        <div class="kf-footer">
            <div class="kf-footer-grid">
                <div>
                    {kf_logo_lockup(size=32, wordmark_size="22px", show_tagline=False)}
                    <div class="kf-footer-brand-desc">
                        AI-assisted security for CI/CD pipelines, Kubernetes,
                        containers, and cloud &mdash; and the AI engineering
                        platform behind it.
                    </div>
                </div>
                {columns_html}
            </div>
            <div class="kf-footer-bottom">
                <div class="kf-footer-copyright">&copy; 2026 SixStage. All rights reserved.</div>
                <div class="kf-footer-copyright">hello@sixstage.ai</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
