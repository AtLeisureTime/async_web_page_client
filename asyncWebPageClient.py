from urllib2 import Request, urlopen, URLError
import threading
from collections import deque

class AsyncWebPageClient:
    def __init__(self, num_thread = 2):
        self.__num_thread = num_thread
        self.__url_collection = deque()
        self.__page_collection = deque()
        self.__mutex = threading.RLock()

    def __get_page(self, url):
        req = Request(url)
        try:
            resp = urlopen(req)
        except URLError as e:
            # failed to reach a server || the server couldn't fulfill the request
            return {'status_code': -1, 'err': e, 'url': url}
        else:
            return {'status_code': resp.getcode(), 'url': url, 'content': resp.read()}

    def __get_url(self):
        with self.__mutex:
            try:
                url = self.__url_collection.pop()
            except IndexError:
                return
            else:
                return url
            
    def __process_urls(self):
        url = self.__get_url()
        while url:
            page_dict = self.__get_page(url)
            with self.__mutex:
                self.__page_collection.append(page_dict)
            url = self.__get_url()
        
    def get_pages(self, url_collection):    
        self.__url_collection = url_collection
       
        thr_list = []
        for i in range(0, self.__num_thread):
            thr_list.append(threading.Thread(target=self.__process_urls))            
            thr_list[i].start()

        for i in range(0, self.__num_thread):
            thr_list[i].join()        

        return self.__page_collection
