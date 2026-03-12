import logging
logger = logging.getLogger(__name__)
if username == "admin" and password == "pass":
    logger.info("admin logged in successfully")
else:
    logger.warning("Invalid login attempt")
