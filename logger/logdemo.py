import logging
logging.basicConfig(filename='hcllog.log',filemode='a',level=logging.DEBUG)
logging.debug("Hello from debug")
logging.info("hello from warning")
logging.error("hello from error")
logging.critical("hello from critical")