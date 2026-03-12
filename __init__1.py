import logging
from flask import Flask

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application started successfully")
