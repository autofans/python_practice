import requests
from lxml import etree

header = {"User-Agent": "Mozilla/5.0 "
                        "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "BDqhfp=%E9%A3%8E%E6%99%AF%26%260-10-1undefined%26%260%26%261; winWH=%5E6_1920x968; BDIMGISLOGIN=0; BAIDUID=19FBEEE1668459725F370796E07DEAFB:FG=1; BIDUPSID=19FBEEE1668459725F370796E07DEAFB; PSTM=1560746509; H_WISE_SIDS=132693_125704_132922_100807_131676_131656_128064_131888_133679_120131_133763_131602_133016_132909_133042_131246_132439_130762_132378_131518_118897_118869_118856_118824_118792_132840_132604_107318_133159_132590_132783_130122_133351_133302_132890_129647_132250_124633_132557_132538_133472_131906_128892_133848_132552_132675_132543_129643_131423_133414_133418_133808_110085_131574_127969_123289_131753_132283_127417_132281_133729; BDUSS=NNWkFQNkdLZGp2V2Y4RnEtQm1SQ0dOdFBqY2RpS3lqd0NpVDE3LWxTN2w5RXBkSVFBQUFBJCQAAAAAAAAAAAEAAAAUxnhAYXV0b2ZhbnMyMDA1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOVnI13lZyNdME; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; cleanHistoryStatus=0; indexPageSugList=%5B%22%E9%A3%8E%E6%99%AF%22%2C%22%E4%BA%BA%E7%89%A9%22%2C%22%E6%B1%BD%E8%BD%A6%22%2C%22%E7%8E%8B%E4%B8%BD%E5%9D%A4%22%2C%22%E5%8A%A0%E8%97%A4%E5%B0%8F%E9%9B%AA%22%2C%22%E5%BC%A0%E5%AD%90%E6%9E%AB%22%5D; session_name=; session_id=1571850972367; userFrom=null; BCLID=8733091134875800632; BDSFRCVID=qOIOJeCT5G3DA77w43wXMeSsIprULoQTTPjcTR5qJ04BtyCVN15nEG0Ptf1tNTK-Nb29ogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJF8oKP5fC83qKbxKPoHK4tJqGLqqTkXKKOLV-TMBp7keq8CDxt2jTtvjltJJURDBCTgQhF-WK5RVh72y5jDyb_7Mf7XBbkOMCcx3DbkQlQpsIJMbfFWbT8U5f520-rhaKviaKOjBMb1JhbDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6oQjHtfJjFff5vfL5rtKRTffjrnhPF3Kf4PXP6-3h0t3b7R5C05bK-5fUnEbqb5yJ8X3tvyQl3nLIQ2-U_a-lF2Mhom2fb4X6o0h4oxJpOJ5J6J2fbcHlrDhCTvbURvD--g3-AqBM5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCKKhD-m3e; ZD_ENTRY=baidu; H_PS_PSSID=1436_21080_20698_29568_29221_26350",
"Host": "image.baidu.com",
"Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1571847543593_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E4%BA%BA%E7%89%A9",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1"}

word = "风景"

url = "https://image.baidu.com/search/index?" \
      "tn=baiduimage&ipn=r&ct=201326592&cl=2&lm" \
      "=-1&st=-1&fm=result&fr=&sf=1&fmq=1571847611174_R&pv=&i" \
      "c=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0" \
      "&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%s" % word

res = requests.get(url, headers=header).text

print(res)

html = etree.HTML(res)
a = html.xpath('//li[@class="imgitem"]/div[@class="imgbox"]/a/img/@class')
print(a)


