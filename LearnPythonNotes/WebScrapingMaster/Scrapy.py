"""Installing Scrappy
https://scrapy.org/
    pip install Scrapy
    

SCRAPY ARCHITECTURE
    Data Flow

    Spiders     *** Spiders are basically costume classes in Python. They are basically written by a scrappy user to pass responses and extract items from the website'
        "
        "

    Then the engine will schedule the request in the scheduler and then ask for the next request.

    ENGINE  Controls the data flow between the components of the system.
    
    Scheduler   Basically is used to receive requests and schedule them for execution by the engine and then return them to the engine.
    
    Middleware is involved in the data flow process [showen as a rectangle].
    
    The engine sends the request to the downloader via the Internet.
    
    The downloader is responsible for fetching the pages and also feeding them to the engine, wiitch than feeds them to the spiders.
    
    Once the page finishes downloading via the internet, the downloader then generates a response with that page and sends it to the engine.  This also passes through the download middleware.
    
    The downloader middleware are specific hooks that sit between the engine and the downloader, they process their request when they pass it through the engine to the downloader and also provide responses that passes from the downloader to the engine, the engine receives the response from the downloader and sends it to the spider for processing. This also passes through the spider middleware.
    
    The spider processes the response and returns the items the items that have been scraped from the website to the engine, it also passes through the spider middleware,
    
    The spyder middleware are specific hooks that sit between the engine and the spiders.
    They are also able to process the spider inputs which are the responces and also the output the items and the request.
    
    The engine sends the processed items to the item pipelines and then sends the processed request to the schelder and asks if there are any more requests.
    
    Now the item pipeline is basically responsible for processing the items once they have been extracted.
    
    A typical task that the item pipeline will perform or could perform include; cleansing, validation and persistence like storing the items that have been scraped in the database.
    

"""