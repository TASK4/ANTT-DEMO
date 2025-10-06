import logging

# Cấu hình logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='generated_logs.log',
    filemode='w'
)

# Tạo đối tượng logger
logger = logging.getLogger('CustomLogger')

# Sinh các loại log khác nhau
logger.debug("Debug message for troubleshooting")
logger.info("Info message for system events")
logger.warning("Warning: Disk space is running low")
logger.error("Error encountered while connecting to the database")
logger.critical("Critical: System shutdown initiated due to overheating")