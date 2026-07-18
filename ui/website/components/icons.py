"""
Kubeforge Icon Set

Small, single-color line icons (feather-icon style) used across
service and capability cards. Kept minimal and geometric to match
the rest of the visual language.
"""

_WRAP = (
    '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" '
    'stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round" '
    'stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg">{body}</svg>'
)


def _icon(body: str) -> str:
    return _WRAP.format(body=body)


ICON_AUTOMATION = _icon(
    '<path d="M21 12a9 9 0 1 1-3-6.7"/><polyline points="21 3 21 9 15 9"/>'
)

ICON_AGENTS = _icon(
    '<circle cx="6" cy="6" r="2.2"/><circle cx="18" cy="6" r="2.2"/>'
    '<circle cx="12" cy="18" r="2.2"/>'
    '<line x1="7.8" y1="7.2" x2="10.6" y2="16"/>'
    '<line x1="16.2" y1="7.2" x2="13.4" y2="16"/>'
    '<line x1="8.2" y1="6" x2="15.8" y2="6"/>'
)

ICON_KNOWLEDGE = _icon(
    '<ellipse cx="12" cy="5" rx="8" ry="3"/>'
    '<path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/>'
    '<path d="M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>'
)

ICON_ARCHITECTURE = _icon(
    '<rect x="3" y="3" width="7" height="7" rx="1"/>'
    '<rect x="14" y="3" width="7" height="7" rx="1"/>'
    '<rect x="14" y="14" width="7" height="7" rx="1"/>'
    '<rect x="3" y="14" width="7" height="7" rx="1"/>'
)

ICON_OPPORTUNITY = _icon(
    '<circle cx="11" cy="11" r="7"/><line x1="16.2" y1="16.2" x2="21" y2="21"/>'
    '<circle cx="11" cy="11" r="2.4"/>'
)

ICON_POC = _icon(
    '<path d="M9 2h6"/><path d="M10 2v6l-5.5 9.5A2 2 0 0 0 6.2 21h11.6a2 2 0 0 0 1.7-3.5L14 8V2"/>'
    '<line x1="7" y1="14" x2="17" y2="14"/>'
)

ICON_IMPLEMENTATION = _icon(
    '<rect x="4" y="3" width="16" height="18" rx="2"/>'
    '<line x1="8" y1="8" x2="16" y2="8"/>'
    '<polyline points="8 13 10.5 15.5 16 10"/>'
)

ICON_DEMO = _icon(
    '<rect x="3" y="4" width="18" height="13" rx="2"/>'
    '<polygon points="10.5 8.5 15 10.5 10.5 12.5"/>'
    '<line x1="8" y1="21" x2="16" y2="21"/>'
    '<line x1="12" y1="17" x2="12" y2="21"/>'
)

ICON_PACKAGE = _icon(
    '<path d="M21 8l-9-5-9 5 9 5 9-5z"/>'
    '<path d="M3 8v8l9 5 9-5V8"/>'
    '<line x1="12" y1="13" x2="12" y2="21"/>'
)
