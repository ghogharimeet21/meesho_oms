import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] [%(threadName)s] : %(message)s'
)
logger = logging.getLogger(__name__)

from api import create_app
app = create_app()
app.run(host="0.0.0.0", port=5002, debug=True)
