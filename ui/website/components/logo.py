"""
SixStage Logo Mark

A dot-sphere globe (particles arranged into a lit sphere, colored
across the site's purple -> blue -> green gradient) paired with the
"sixstage" wordmark and tagline, matching the brand's horizontal
lockup. The sphere is deliberately lit up: brighter dots, larger
core particles, and a soft glow so the icon reads as a light source
rather than a flat graphic.
"""

_SPHERE_DOTS = """
<circle cx="64.4" cy="22.3" r="1.28" fill="#6ea6fa" opacity="0.74"/>
<circle cx="76.9" cy="22.8" r="1.47" fill="#5aaff9" opacity="0.79"/>
<circle cx="91.6" cy="24.0" r="1.55" fill="#46b7f8" opacity="0.81"/>
<circle cx="105.5" cy="22.4" r="1.56" fill="#38bef3" opacity="0.81"/>
<circle cx="117.8" cy="22.3" r="1.51" fill="#37c1e5" opacity="0.79"/>
<circle cx="130.8" cy="23.5" r="1.36" fill="#37c5d7" opacity="0.76"/>
<circle cx="143.8" cy="22.7" r="1.01" fill="#36c8c8" opacity="0.67"/>
<circle cx="44.1" cy="37.1" r="1.29" fill="#8d99fa" opacity="0.74"/>
<circle cx="56.5" cy="37.2" r="1.58" fill="#79a2fa" opacity="0.81"/>
<circle cx="71.6" cy="35.7" r="1.74" fill="#64aaf9" opacity="0.85"/>
<circle cx="85.0" cy="37.5" r="1.82" fill="#50b3f9" opacity="0.88"/>
<circle cx="97.3" cy="36.1" r="1.86" fill="#3bbcf8" opacity="0.89"/>
<circle cx="112.4" cy="36.6" r="1.84" fill="#38c0ec" opacity="0.88"/>
<circle cx="123.7" cy="36.0" r="1.77" fill="#37c3de" opacity="0.86"/>
<circle cx="139.2" cy="37.3" r="1.64" fill="#36c6d0" opacity="0.83"/>
<circle cx="152.5" cy="37.6" r="1.41" fill="#36cac1" opacity="0.77"/>
<circle cx="37.1" cy="51.7" r="1.46" fill="#9795fb" opacity="0.78"/>
<circle cx="50.2" cy="50.6" r="1.72" fill="#839efa" opacity="0.85"/>
<circle cx="64.9" cy="50.8" r="1.89" fill="#6ea6fa" opacity="0.89"/>
<circle cx="78.4" cy="50.7" r="1.99" fill="#5aaff9" opacity="0.92"/>
<circle cx="91.5" cy="49.3" r="2.04" fill="#46b7f8" opacity="0.93"/>
<circle cx="103.8" cy="50.0" r="2.04" fill="#38bef3" opacity="0.93"/>
<circle cx="116.9" cy="49.8" r="2.01" fill="#37c1e5" opacity="0.92"/>
<circle cx="130.5" cy="49.9" r="1.93" fill="#37c5d7" opacity="0.90"/>
<circle cx="145.4" cy="50.1" r="1.79" fill="#36c8c8" opacity="0.87"/>
<circle cx="158.2" cy="49.7" r="1.56" fill="#35cbba" opacity="0.81"/>
<circle cx="171.4" cy="51.6" r="1.12" fill="#35cfac" opacity="0.70"/>
<circle cx="30.6" cy="64.3" r="1.51" fill="#a191fb" opacity="0.80"/>
<circle cx="42.9" cy="64.6" r="1.79" fill="#8d99fa" opacity="0.87"/>
<circle cx="56.4" cy="63.7" r="1.96" fill="#79a2fa" opacity="0.91"/>
<circle cx="72.0" cy="64.4" r="2.08" fill="#64aaf9" opacity="0.94"/>
<circle cx="84.4" cy="64.5" r="2.14" fill="#50b3f9" opacity="0.96"/>
<circle cx="98.6" cy="64.7" r="2.17" fill="#3bbcf8" opacity="0.97"/>
<circle cx="110.5" cy="62.8" r="2.16" fill="#38c0ec" opacity="0.96"/>
<circle cx="124.3" cy="63.4" r="2.11" fill="#37c3de" opacity="0.95"/>
<circle cx="137.5" cy="65.2" r="2.01" fill="#36c6d0" opacity="0.92"/>
<circle cx="152.7" cy="63.5" r="1.86" fill="#36cac1" opacity="0.89"/>
<circle cx="165.7" cy="63.7" r="1.62" fill="#35cdb3" opacity="0.82"/>
<circle cx="179.8" cy="63.9" r="1.17" fill="#34d0a5" opacity="0.71"/>
<circle cx="22.9" cy="76.8" r="1.47" fill="#ac8dfb" opacity="0.79"/>
<circle cx="37.2" cy="76.9" r="1.79" fill="#9795fb" opacity="0.87"/>
<circle cx="50.7" cy="78.5" r="1.99" fill="#839efa" opacity="0.92"/>
<circle cx="63.7" cy="76.8" r="2.12" fill="#6ea6fa" opacity="0.95"/>
<circle cx="78.8" cy="77.5" r="2.20" fill="#5aaff9" opacity="0.97"/>
<circle cx="89.9" cy="76.3" r="2.24" fill="#46b7f8" opacity="0.99"/>
<circle cx="103.5" cy="77.8" r="2.25" fill="#38bef3" opacity="0.99"/>
<circle cx="118.8" cy="77.3" r="2.22" fill="#37c1e5" opacity="0.98"/>
<circle cx="130.4" cy="77.2" r="2.15" fill="#37c5d7" opacity="0.96"/>
<circle cx="146.3" cy="77.6" r="2.04" fill="#36c8c8" opacity="0.93"/>
<circle cx="159.7" cy="78.4" r="1.86" fill="#35cbba" opacity="0.89"/>
<circle cx="170.7" cy="78.1" r="1.60" fill="#35cfac" opacity="0.82"/>
<circle cx="186.0" cy="77.6" r="1.04" fill="#34d29e" opacity="0.67"/>
<circle cx="16.1" cy="91.4" r="1.32" fill="#b688fc" opacity="0.75"/>
<circle cx="29.2" cy="90.8" r="1.72" fill="#a191fb" opacity="0.85"/>
<circle cx="43.6" cy="92.2" r="1.95" fill="#8d99fa" opacity="0.91"/>
<circle cx="58.2" cy="90.4" r="2.11" fill="#79a2fa" opacity="0.95"/>
<circle cx="70.8" cy="90.2" r="2.21" fill="#64aaf9" opacity="0.98"/>
<circle cx="85.3" cy="92.0" r="2.27" fill="#50b3f9" opacity="0.99"/>
<circle cx="97.2" cy="91.4" r="2.29" fill="#3bbcf8" opacity="1.00"/>
<circle cx="111.5" cy="90.1" r="2.28" fill="#38c0ec" opacity="0.99"/>
<circle cx="125.4" cy="91.1" r="2.23" fill="#37c3de" opacity="0.98"/>
<circle cx="139.0" cy="91.1" r="2.14" fill="#36c6d0" opacity="0.96"/>
<circle cx="150.5" cy="90.5" r="2.01" fill="#36cac1" opacity="0.92"/>
<circle cx="164.0" cy="92.1" r="1.81" fill="#35cdb3" opacity="0.87"/>
<circle cx="179.7" cy="91.9" r="1.48" fill="#34d0a5" opacity="0.79"/>
<circle cx="23.0" cy="103.4" r="1.56" fill="#ac8dfb" opacity="0.81"/>
<circle cx="38.0" cy="105.7" r="1.85" fill="#9795fb" opacity="0.88"/>
<circle cx="49.4" cy="104.5" r="2.04" fill="#839efa" opacity="0.93"/>
<circle cx="62.9" cy="105.2" r="2.17" fill="#6ea6fa" opacity="0.97"/>
<circle cx="78.2" cy="103.5" r="2.25" fill="#5aaff9" opacity="0.99"/>
<circle cx="90.9" cy="104.6" r="2.29" fill="#46b7f8" opacity="1.00"/>
<circle cx="103.9" cy="105.5" r="2.30" fill="#38bef3" opacity="1.00"/>
<circle cx="117.8" cy="103.8" r="2.27" fill="#37c1e5" opacity="0.99"/>
<circle cx="131.6" cy="105.1" r="2.20" fill="#37c5d7" opacity="0.97"/>
<circle cx="144.2" cy="104.0" r="2.09" fill="#36c8c8" opacity="0.95"/>
<circle cx="159.8" cy="104.9" r="1.93" fill="#35cbba" opacity="0.90"/>
<circle cx="171.8" cy="104.5" r="1.68" fill="#35cfac" opacity="0.84"/>
<circle cx="184.5" cy="103.8" r="1.23" fill="#34d29e" opacity="0.72"/>
<circle cx="16.3" cy="118.2" r="1.25" fill="#b688fc" opacity="0.73"/>
<circle cx="29.5" cy="117.3" r="1.68" fill="#a191fb" opacity="0.84"/>
<circle cx="42.6" cy="118.3" r="1.92" fill="#8d99fa" opacity="0.90"/>
<circle cx="56.5" cy="119.1" r="2.08" fill="#79a2fa" opacity="0.94"/>
<circle cx="71.7" cy="116.9" r="2.18" fill="#64aaf9" opacity="0.97"/>
<circle cx="83.6" cy="118.4" r="2.24" fill="#50b3f9" opacity="0.99"/>
<circle cx="97.0" cy="117.0" r="2.27" fill="#3bbcf8" opacity="0.99"/>
<circle cx="112.4" cy="118.2" r="2.26" fill="#38c0ec" opacity="0.99"/>
<circle cx="124.7" cy="118.7" r="2.21" fill="#37c3de" opacity="0.98"/>
<circle cx="139.0" cy="117.2" r="2.12" fill="#36c6d0" opacity="0.95"/>
<circle cx="150.7" cy="117.8" r="1.98" fill="#36cac1" opacity="0.92"/>
<circle cx="165.1" cy="117.9" r="1.77" fill="#35cdb3" opacity="0.86"/>
<circle cx="179.3" cy="118.5" r="1.43" fill="#34d0a5" opacity="0.78"/>
<circle cx="24.8" cy="130.5" r="1.36" fill="#ac8dfb" opacity="0.76"/>
<circle cx="36.7" cy="131.1" r="1.71" fill="#9795fb" opacity="0.85"/>
<circle cx="51.4" cy="130.8" r="1.93" fill="#839efa" opacity="0.90"/>
<circle cx="63.2" cy="131.4" r="2.06" fill="#6ea6fa" opacity="0.94"/>
<circle cx="77.3" cy="130.9" r="2.15" fill="#5aaff9" opacity="0.96"/>
<circle cx="90.3" cy="132.6" r="2.19" fill="#46b7f8" opacity="0.97"/>
<circle cx="104.4" cy="132.4" r="2.20" fill="#38bef3" opacity="0.97"/>
<circle cx="118.1" cy="130.3" r="2.17" fill="#37c1e5" opacity="0.97"/>
<circle cx="132.8" cy="132.4" r="2.10" fill="#37c5d7" opacity="0.95"/>
<circle cx="146.2" cy="132.6" r="1.98" fill="#36c8c8" opacity="0.92"/>
<circle cx="159.4" cy="130.6" r="1.80" fill="#35cbba" opacity="0.87"/>
<circle cx="172.0" cy="130.8" r="1.51" fill="#35cfac" opacity="0.79"/>
<circle cx="30.0" cy="143.9" r="1.35" fill="#a191fb" opacity="0.75"/>
<circle cx="43.4" cy="146.3" r="1.68" fill="#8d99fa" opacity="0.84"/>
<circle cx="56.6" cy="145.7" r="1.87" fill="#79a2fa" opacity="0.89"/>
<circle cx="70.6" cy="144.8" r="1.99" fill="#64aaf9" opacity="0.92"/>
<circle cx="85.4" cy="146.3" r="2.06" fill="#50b3f9" opacity="0.94"/>
<circle cx="97.9" cy="145.6" r="2.09" fill="#3bbcf8" opacity="0.95"/>
<circle cx="110.4" cy="144.5" r="2.08" fill="#38c0ec" opacity="0.94"/>
<circle cx="126.0" cy="145.2" r="2.02" fill="#37c3de" opacity="0.93"/>
<circle cx="138.4" cy="145.6" r="1.92" fill="#36c6d0" opacity="0.90"/>
<circle cx="150.6" cy="145.2" r="1.75" fill="#36cac1" opacity="0.86"/>
<circle cx="165.3" cy="145.9" r="1.48" fill="#35cdb3" opacity="0.79"/>
<circle cx="36.1" cy="159.7" r="1.21" fill="#9795fb" opacity="0.72"/>
<circle cx="49.4" cy="157.7" r="1.56" fill="#839efa" opacity="0.81"/>
<circle cx="64.2" cy="159.0" r="1.75" fill="#6ea6fa" opacity="0.86"/>
<circle cx="76.8" cy="157.5" r="1.86" fill="#5aaff9" opacity="0.89"/>
<circle cx="92.0" cy="157.8" r="1.92" fill="#46b7f8" opacity="0.90"/>
<circle cx="104.7" cy="158.8" r="1.93" fill="#38bef3" opacity="0.90"/>
<circle cx="117.8" cy="158.7" r="1.89" fill="#37c1e5" opacity="0.89"/>
<circle cx="131.6" cy="159.6" r="1.80" fill="#37c5d7" opacity="0.87"/>
<circle cx="144.2" cy="159.1" r="1.64" fill="#36c8c8" opacity="0.83"/>
<circle cx="157.8" cy="158.2" r="1.36" fill="#35cbba" opacity="0.76"/>
<circle cx="57.7" cy="171.5" r="1.32" fill="#79a2fa" opacity="0.75"/>
<circle cx="70.3" cy="172.7" r="1.53" fill="#64aaf9" opacity="0.80"/>
<circle cx="83.1" cy="171.9" r="1.64" fill="#50b3f9" opacity="0.83"/>
<circle cx="99.0" cy="173.3" r="1.68" fill="#3bbcf8" opacity="0.84"/>
<circle cx="110.1" cy="171.3" r="1.66" fill="#38c0ec" opacity="0.83"/>
<circle cx="124.1" cy="173.1" r="1.58" fill="#37c3de" opacity="0.81"/>
<circle cx="139.2" cy="173.0" r="1.41" fill="#36c6d0" opacity="0.77"/>
<circle cx="151.4" cy="171.1" r="1.02" fill="#36cac1" opacity="0.67"/>
<circle cx="78.4" cy="186.0" r="1.04" fill="#5aaff9" opacity="0.67"/>
<circle cx="91.3" cy="186.8" r="1.21" fill="#46b7f8" opacity="0.72"/>
<circle cx="104.9" cy="184.2" r="1.23" fill="#38bef3" opacity="0.72"/>
<circle cx="118.8" cy="185.0" r="1.12" fill="#37c1e5" opacity="0.70"/>
"""


def kf_logo_svg(size: int = 56) -> str:
    """The SixStage dot-sphere globe mark, lit up with a soft glow."""

    glow = (
        "drop-shadow(0 0 8px rgba(56,189,248,0.65)) "
        "drop-shadow(0 0 16px rgba(192,132,252,0.45)) "
        "drop-shadow(0 0 24px rgba(52,211,153,0.3))"
    )

    return f"""
    <svg width="{size}" height="{size}" viewBox="0 0 200 200"
         xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0; filter:{glow};">
        <defs>
            <radialGradient id="kfGlowCore" cx="52%" cy="48%" r="55%">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.55"/>
                <stop offset="35%" stop-color="#7dd3fc" stop-opacity="0.22"/>
                <stop offset="100%" stop-color="#7dd3fc" stop-opacity="0"/>
            </radialGradient>
        </defs>
        <circle cx="100" cy="96" r="88" fill="url(#kfGlowCore)"/>
        {_SPHERE_DOTS}
    </svg>
    """


def kf_logo_lockup(size: int = 56, wordmark_class: str = "kf-logo",
                    wordmark_size: str = "34px", show_tagline: bool = True) -> str:
    """Icon + wordmark (+ optional tagline), wrapped in a link home."""

    tagline_html = ""
    if show_tagline:
        tagline_html = (
            '<span class="kf-tagline">AUTOMATE &middot; SECURE &middot; RESILIENT</span>'
        )

    return f"""
    <a href="/" target="_self" style="text-decoration:none;">
        <div style="display:flex; align-items:center; gap:14px; cursor:pointer;">
            {kf_logo_svg(size)}
            <div style="display:flex; flex-direction:column; gap:2px;">
                <span class="{wordmark_class}" style="font-size:{wordmark_size};">sixstage</span>
                {tagline_html}
            </div>
        </div>
    </a>
    """
