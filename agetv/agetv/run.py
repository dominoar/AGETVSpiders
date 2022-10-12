from scrapy import cmdline

name = 'AGE动漫网'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
