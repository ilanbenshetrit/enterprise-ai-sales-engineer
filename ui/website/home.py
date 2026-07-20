"""
SixStage Corporate Header Test
"""

import streamlit as st

from theme import apply_theme
from components.header import render_header
from components.hero import render_hero
from components.promo_carousel import render_promo_carousel
from components.stats import render_stats
from components.about import render_about
from components.vision import render_vision
from components.flagship_band import render_flagship_band
from components.product_grid import render_product_grid
from components.services import render_services
from components.cta import render_cta
from components.footer import render_footer


def render_home():

    apply_theme()

    render_header()
    render_hero()
    render_promo_carousel()
    render_stats()
    render_about()
    render_vision()
    render_flagship_band()
    render_product_grid()
    render_services()
    render_cta()
    render_footer()
