
from scrapy.selector import Selector
import pandas as pd

my_list = []

with open('credit_union.html', 'r', encoding='utf-8') as f:
    response_text = f.read()

respone_full = Selector(text=response_text)

matches = respone_full.xpath('//div[@class="et_pb_ajax_pagination_container"]//article')

for match in matches:
    title = match.xpath('.//h3/a//text()').get()
    link = match.xpath('.//h3/a//@href').get()
    
    my_list.append({
        'Title': title,
        'Link': link
    })
    
print(my_list)
print(len(my_list))

df = pd.DataFrame(my_list)
df.to_excel('output.xlsx', index=False)









