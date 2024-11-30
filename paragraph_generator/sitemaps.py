# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        # List of views to include in the sitemap
        return ['index', 'dashboard', 'generate_paragraph']

    def location(self, item):
        return reverse(item)
