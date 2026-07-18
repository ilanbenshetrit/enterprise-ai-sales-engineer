"""
Kubeforge Hero Section
"""

import streamlit as st


HERO_NETWORK_SVG = """
<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg"
     style="width:100%; max-width:820px; height:auto; margin:10px auto 0; display:block;">
    <defs>
        <linearGradient id="heroNetGrad" x1="0" y1="0" x2="800" y2="0">
            <stop offset="0" stop-color="#c084fc"/>
            <stop offset="0.5" stop-color="#38bdf8"/>
            <stop offset="1" stop-color="#34d399"/>
        </linearGradient>
    </defs>
    <g stroke="url(#heroNetGrad)" stroke-width="1" opacity="0.35">
        <line x1="60" y1="60" x2="160" y2="30"/>
        <line x1="60" y1="60" x2="160" y2="90"/>
        <line x1="160" y1="30" x2="280" y2="60"/>
        <line x1="160" y1="90" x2="280" y2="60"/>
        <line x1="280" y1="60" x2="400" y2="20"/>
        <line x1="280" y1="60" x2="400" y2="100"/>
        <line x1="400" y1="20" x2="520" y2="60"/>
        <line x1="400" y1="100" x2="520" y2="60"/>
        <line x1="520" y1="60" x2="640" y2="30"/>
        <line x1="520" y1="60" x2="640" y2="90"/>
        <line x1="640" y1="30" x2="740" y2="60"/>
        <line x1="640" y1="90" x2="740" y2="60"/>
    </g>
    <g fill="url(#heroNetGrad)">
        <circle cx="60" cy="60" r="6"/>
        <circle cx="280" cy="60" r="6"/>
        <circle cx="520" cy="60" r="6"/>
        <circle cx="740" cy="60" r="6"/>
    </g>
    <g fill="#e2e8f0" opacity="0.55">
        <circle cx="160" cy="30" r="3.5"/>
        <circle cx="160" cy="90" r="3.5"/>
        <circle cx="400" cy="20" r="3.5"/>
        <circle cx="400" cy="100" r="3.5"/>
        <circle cx="640" cy="30" r="3.5"/>
        <circle cx="640" cy="90" r="3.5"/>
    </g>
</svg>
"""


def render_hero():

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Alex+Brush&display=swap');

        .hero {{
            text-align: center;
            padding: 80px 20px 20px;
        }}

        .hero-signature-wrap {{
            padding: 18px 20px 6px;
        }}

        .hero-signature {{
            font-family: 'Alex Brush', cursive;
            font-size: 40px;
            font-weight: 400;
            line-height: 1;
            background: linear-gradient(90deg, #c084fc, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline-block;
        }}

        .hero-title {{
            font-size: 64px;
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 25px;
        }}

        .hero-gradient {{
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .hero-description {{
            max-width: 850px;
            margin: auto;
            font-size: 22px;
            line-height: 1.6;
            color: rgba(255,255,255,0.85);
        }}

        .hero-button {{
            display: inline-block;
            margin: 40px 12px;
            padding: 15px 35px;
            border-radius: 14px;
            font-size: 18px;
            font-weight: 600;
            color: white;
            background: linear-gradient(90deg, #8b5cf6, #38bdf8, #34d399);
            transition: 0.3s;
            text-decoration: none;
        }}

        .hero-button:hover {{
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(56,189,248,0.35);
        }}

        .hero-button-outline {{
            display: inline-block;
            margin: 40px 12px;
            padding: 15px 35px;
            border-radius: 14px;
            font-size: 18px;
            font-weight: 600;
            color: white;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.2);
            transition: 0.3s;
            text-decoration: none;
        }}

        .hero-button-outline:hover {{
            transform: translateY(-6px);
            border-color: rgba(255,255,255,0.4);
        }}

        </style>
        <section class="hero">
            <div class="hero-title">
                <span class="hero-gradient">Building The Future</span>
                <br>
                <span class="hero-gradient">Of Intelligent Enterprise Automation</span>
            </div>
            <div class="hero-signature-wrap">
                <span class="hero-signature">Kubeforge</span>
            </div>
            <div class="hero-description">
                Kubeforge delivers advanced AI-driven automation capabilities
                that help organizations transform complex processes into
                secure, intelligent, and scalable digital environments.
            </div>
            <div>
                <a class="hero-button" href="/platform" target="_self">Explore Platform</a>
                <a class="hero-button-outline" href="/contact" target="_self">Contact Us</a>
            </div>

            {HERO_NETWORK_SVG}

        </section>

        """,
        unsafe_allow_html=True
    )
