from google_images_download_master import bing_scraper
from googletrans import Translator

translator=Translator();

cn_key=input("key: ")
key=translator.translate(cn_key).text


response=bing_scraper.googleimagesdownload()  
arguments = {"url":"https://www.bing.com/images/search?q="+key+"+icon","download":True,"limit":2,"print_urls":True,"chromedriver":".\google_images_download_master\chromedriver"} 
paths = response.download(arguments) 
print(paths) 