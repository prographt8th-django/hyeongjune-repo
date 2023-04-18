import logging

logger = logging.getLogger(__name__)


def export_celery_log(log_path, message):
    logger.info(f'{log_path} {message}')
