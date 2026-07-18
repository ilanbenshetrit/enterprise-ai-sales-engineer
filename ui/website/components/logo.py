"""
Kubeforge Logo Mark

A single geometric monogram (hexagon outline + "K") paired with the
wordmark. Kept deliberately plain/geometric rather than illustrative,
so it reads as a serious enterprise brand mark rather than a
decorative icon.
"""


def kf_logo_svg(size: int = 40) -> str:
    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 40 40"
         xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;">
        <defs>
            <linearGradient id="kfLogoGrad" x1="0" y1="0" x2="40" y2="40">
                <stop offset="0" stop-color="#c084fc"/>
                <stop offset="0.5" stop-color="#38bdf8"/>
                <stop offset="1" stop-color="#34d399"/>
            </linearGradient>
        </defs>
        <polygon points="34.7,28.5 20,37 5.3,28.5 5.3,11.5 20,3 34.7,11.5"
                 fill="none" stroke="url(#kfLogoGrad)" stroke-width="2.2"
                 stroke-linejoin="round"/>
        <text x="20" y="27" text-anchor="middle" font-family="Arial, sans-serif"
              font-size="17" font-weight="800" fill="url(#kfLogoGrad)">K</text>
    </svg>
    """


def kf_logo_lockup(size: int = 40, wordmark_class: str = "kf-logo",
                    wordmark_size: str = "30px") -> str:
    """Icon + wordmark, wrapped in a link back to the home page."""

    return f"""
    <a href="/" target="_self" style="text-decoration:none;">
        <div style="display:flex; align-items:center; gap:10px; cursor:pointer;">
            {kf_logo_svg(size)}
            <span class="{wordmark_class}" style="font-size:{wordmark_size};">KUBEFORGE</span>
        </div>
    </a>
    """
