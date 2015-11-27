import pprint
import asyncWebPageClient

def main():
    cl = AsyncWebPageClient()
    url_collection = deque(['http://steamcommunity.com/market/listings/730/Shadow%20Case%20Key',\
                            'http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29',\
                            'http://steamcommunity.com/market/listings/730/Shadow%20Case',\
                            'http://steamcommunity.com/market/listings/730/AWP%20%7C%20Asiimov%20%28Field-Tested%29',\
                            'http://steamcommunity.com/market/listings/730/AK-47%20%7C%20Frontside%20Misty%20%28Field-Tested%29',\
                            'http://steamcommunity.com/market/listings/730/%E2%98%85%20Flip%20Knife%20%7C%20Doppler%20%28Factory%20New%29',\
                            'http://steamcommunity.com/market/listings/730/M4A1-S%20%7C%20Hyper%20Beast%20%28Field-Tested%29',\
                            'http://steamcommunity.com/market/listings/730/Glock-18%20%7C%20Water%20Elemental%20%28Field-Tested%29'])
    resp = cl.get_pages(url_collection)

    for dict in resp:
        pprint.pprint(dict)

if __name__ == "__main__":
    main()
