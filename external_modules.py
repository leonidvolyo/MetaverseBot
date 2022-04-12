##########################################################################
# Attepmt to bypass Cloudflare (antibot system) using external modules

"""import cloudscraper
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
scraper.get("http://sandbox.game")  # => "<!DOCTYPE html><html><head>..."""

"""import cfscrape
#scraper = cfscrape.create_scraper()  # returns a CloudScraper instance
scraper = cfscrape.CloudflareScraper()  # CloudScraper inherits from requests.Session
scraper.get("http://sandbox.game")"""

"""import undetected_chromedriver as uc
driver = uc.Chrome()
driver.get('https://nowsecure.nl') # known url using cloudflare's "under attack mode"
"""
