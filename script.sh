#!/bin/bash

cd debconf/debconf
scrapy crawl schedule
scrapy crawl event_type