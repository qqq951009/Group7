from google_images_download_master import bing_scraper

def crawler_bing(key):
    response=bing_scraper.googleimagesdownload()  
    arguments = {"url":"https://www.bing.com/images/search?q="+key,"download":True,"prefix":key,"limit":1,"print_urls":True,"chromedriver":".\google_images_download_master\chromedriver"} 
    paths = response.download(arguments)
    return paths
