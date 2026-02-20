#dz1
import logging
from datetime import datetime

logging.basicConfig(
    filename="info_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

current_date = datetime.now().strftime("%Y-%m-%d")

logging.info(f"Дата: {current_date}")

#dz2
import logging

logging.basicConfig(
    filename="error_log.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    number = int(input("Введіть число: "))
    result = 10 / number
    print(result)

except Exception as e:
    logging.error(f"Сталася помилка: {e}")