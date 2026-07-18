"""
Kubeforge Hero Section
"""

import streamlit as st


HERO_NETWORK_SVG = """
<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg"
     class="kf-spotlight-net" preserveAspectRatio="xMidYMid slice">
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
        <circle class="kf-pulse-dot" style="animation-delay:0s" cx="60" cy="60" r="6"/>
        <circle class="kf-pulse-dot" style="animation-delay:0.6s" cx="280" cy="60" r="6"/>
        <circle class="kf-pulse-dot" style="animation-delay:1.2s" cx="520" cy="60" r="6"/>
        <circle class="kf-pulse-dot" style="animation-delay:1.8s" cx="740" cy="60" r="6"/>
    </g>
    <g fill="#e2e8f0" opacity="0.55">
        <circle class="kf-pulse-dot" style="animation-delay:0.3s" cx="160" cy="30" r="3.5"/>
        <circle class="kf-pulse-dot" style="animation-delay:0.9s" cx="160" cy="90" r="3.5"/>
        <circle class="kf-pulse-dot" style="animation-delay:1.5s" cx="400" cy="20" r="3.5"/>
        <circle class="kf-pulse-dot" style="animation-delay:2.1s" cx="400" cy="100" r="3.5"/>
        <circle class="kf-pulse-dot" style="animation-delay:0.15s" cx="640" cy="30" r="3.5"/>
        <circle class="kf-pulse-dot" style="animation-delay:1.05s" cx="640" cy="90" r="3.5"/>
    </g>
</svg>
"""


_SPOTLIGHT_SLIDES = [
    {
        "eyebrow": "Security Platform",
        "title": "AI-Assisted Security for Cloud-Native Infrastructure",
        "desc": (
            "Continuous scanning, posture management, and an AI copilot "
            "for CI/CD, Kubernetes, and cloud."
        ),
        "href": "/security",
        "cta": "Explore the Security Platform",
    },
    {
        "eyebrow": "AI Sales Engineer",
        "title": "One AI Engine, Six Stages of Technical Sales",
        "desc": (
            "From opportunity intelligence to a delivered solution "
            "package, running the full workflow end to end."
        ),
        "href": "/platform",
        "cta": "See How It Works",
    },
    {
        "eyebrow": "Live Platform",
        "title": "See the Actual Product, Not a Mockup",
        "desc": (
            "Every capability above is a real, working dashboard you "
            "can open right now."
        ),
        "href": "/demo",
        "cta": "Open the Live Platform",
    },
    {
        "eyebrow": "Our Story",
        "title": "Built by Engineers Who Got Tired of Manual Work",
        "desc": (
            "Kubeforge exists to turn complex technical processes into "
            "automated, intelligent systems."
        ),
        "href": "/company",
        "cta": "Learn Our Story",
    },
]


def _render_spotlight_slides() -> str:

    n = len(_SPOTLIGHT_SLIDES)

    slides_html = ""
    for i, s in enumerate(_SPOTLIGHT_SLIDES):
        delay = i * (20 / n)
        slides_html += f"""
        <a class="kf-spotlight-slide" href="{s['href']}" target="_self"
           style="animation-delay:{delay}s;">
            <div class="kf-spotlight-eyebrow">{s['eyebrow']}</div>
            <div class="kf-spotlight-title">{s['title']}</div>
            <div class="kf-spotlight-desc">{s['desc']}</div>
            <div class="kf-spotlight-cta">{s['cta']} &rarr;</div>
        </a>
        """
    return slides_html


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

        /* Rotating spotlight carousel — pure CSS, no JS/video */

        .kf-spotlight {{
            position: relative;
            max-width: 780px;
            min-height: 220px;
            margin: 50px auto 10px;
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.03);
            overflow: hidden;
        }}

        .kf-spotlight-bg {{
            position: absolute;
            inset: -60%;
            background: linear-gradient(120deg, #c084fc, #38bdf8, #34d399, #8b5cf6);
            background-size: 300% 300%;
            opacity: 0.16;
            filter: blur(50px);
            animation: kfGradientDrift 14s ease infinite;
        }}

        @keyframes kfGradientDrift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        .kf-spotlight-net {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            opacity: 0.4;
        }}

        .kf-pulse-dot {{
            animation: kfPulseDot 3s ease-in-out infinite;
            transform-origin: center;
        }}

        @keyframes kfPulseDot {{
            0%, 100% {{ opacity: 0.5; transform: scale(0.85); }}
            50% {{ opacity: 1; transform: scale(1.25); }}
        }}

        .kf-spotlight-slide {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px 56px;
            text-decoration: none;
            color: inherit;
            opacity: 0;
            animation: kfSpotlightFade 20s infinite;
        }}

        @keyframes kfSpotlightFade {{
            0% {{ opacity: 0; }}
            2% {{ opacity: 1; }}
            23% {{ opacity: 1; }}
            26% {{ opacity: 0; }}
            100% {{ opacity: 0; }}
        }}

        .kf-spotlight-eyebrow {{
            color: #38bdf8;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            margin-bottom: 14px;
        }}

        .kf-spotlight-title {{
            font-size: 26px;
            font-weight: 800;
            color: white;
            line-height: 1.3;
            margin-bottom: 12px;
        }}

        .kf-spotlight-desc {{
            font-size: 15px;
            line-height: 1.65;
            color: rgba(255,255,255,0.75);
            max-width: 560px;
            margin: 0 auto 16px;
        }}

        .kf-spotlight-cta {{
            font-size: 13px;
            font-weight: 700;
            color: #38bdf8;
            transition: 0.25s;
        }}

        .kf-spotlight-slide:hover .kf-spotlight-cta {{
            transform: translateX(4px);
            color: white;
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

            <div class="kf-spotlight">
                <div class="kf-spotlight-bg"></div>
                {HERO_NETWORK_SVG}
                {_render_spotlight_slides()}
            </div>

        </section>

        """,
        unsafe_allow_html=True
    )
