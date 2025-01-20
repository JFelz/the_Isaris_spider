from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
  name = "Operations"
  start_urls = [
        # "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
        "https://www.google.com/about/careers/applications/jobs/results/",
    ]

  def parse(self, response):
         for job in response.css("div.sMn82b"):
            yield {
                # "text": quote.css("span.text::text").get(),
                # "author": quote.css("small.author::text").get(),
                # "tags": quote.css("div.tags a.tag::text").getall(),
                "title": job.css("h3.QJPWVe::text").re(r"Operations.*"),
                "location": job.css("span.r0wTof::text").re(r"USA.*"),
                "company": job.css("span.RP7SMd span::text").get(),
                # print(dict(title=title, location=location, company=company)),
            }
