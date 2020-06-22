import scrapy
from tenrikyology.items import TenrikyologyItem

class TenriSpider(scrapy.Spider):

    # On cmd pmt execute "scrapy crawl 'name' "
    name = "tenrikyology" 

    section = dict(
        research = [
            "Blogging-Anecdotes-of-Oyasama",
            "life-of-the-honseki-izo-iburi"],
        scripture = [
            "mikagura-uta-the-songs-for-the-service",
            "ofudesaki-tip-of-the-writing-brush"],
        Tenrikyo101 = [
            "the-eight-dusts-of-the-mind",
            "the-nine-instruments-of-the-body",
            "the-ten-aspects-of-the-cosmic-providence-list"],
        translations = [
            "anecdotes-of-the-honseki",
            "cornerstone",
            "essays-on-truth-of-origin",
            "footsteps-of-our-predecessors",
            "tenrikyo-apocrypha",
            "tenrikyo-fundamentals"]
        )
    header = 'http://tenrikyology.com/'
    major_urls = []
    for tag in section.keys():
        for title in range(len(section[tag])):
            url = header + tag + '/' + section[tag][title]
            major_urls.append(url)
    
    border = '='*50
    print("{}\nMajor Urls are ready\n{}".format(border,border))
    for i in range(len(major_urls)):
        print(i, major_urls[i])

    def start_requests(self):
        print("start_request executed")
        
        # Temp
        major_urls = self.major_urls[3]
        # for url in major_urls:
        #     print(major_urls.index(url), url)

        # for url in major_urls:
        print('='*10,"current url {}".format(major_urls))
        yield scrapy.Request(url=major_urls, callback=self.parse)

    def parse(self, response):
        print('='*10,'PHASE: PARSE','='*10)
        hyperlinks = response.xpath('//div[@class="entry-content"]/ul/li/a/@href').extract()
        
        print('{}\nHYPERLINKS\n{}'.format(self.border,self.border))
        for link in hyperlinks:
            print(hyperlinks.index(link), link)
            yield scrapy.Request(url=link, callback=self.parse_page)

    def parse_page(self, response):
        title = response.xpath('//h1[@class="entry-title"]/text()').extract()
        entry_date = response.xpath('//time[@class="entry-date"]').getall()
        cat = response.xpath('//span[@class="categories-links"]//text()').extract()
        tag = response.xpath('//span[@class="tags-links"]//text()').extract()
        content = response.xpath('//div[@class="entry-content"]//text()').extract()

        item = TenrikyologyItem()
        item['title']=title
        item['entry_date']=entry_date
        item['cat']=cat
        item['tag']=tag
        item['content']=content
        
        print(
            'TITLE: {} \nENTRY DATE: {} \nCAT: {}\nTAG: {}\n'.format(title,entry_date,cat,tag)
        )
        yield item




























