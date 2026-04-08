from enum import Enum
from pathlib import Path
from datetime import datetime


# ------------------------------------------------------------------------------------------------
# Configuracion general
class ConfigBettingtipsToday(Enum):
    FILE_ENCODING = "utf-8"
    FILE_OVERWRITE = True
    FILE_FORMAT = "csv"
    MODEL_TITLES = ("over-under", "both-teams-to-score","correct-score")


class ConfigBettingtipsTodayWithNave(Enum):
    SPIDER_NAME = "bettingtips_today_with_nave_spider"
    START_URLS_WITH_NAVE = [
        "https://www.bettingtips.today/over-under-predictions-tips/",
        "https://www.bettingtips.today/both-teams-to-score-predictions-tips/",
        "https://www.bettingtips.today/correct-score-predictions-tips/",

        "https://www.bettingtips.today/over-under-predictions-tips/tomorrow/",
        "https://www.bettingtips.today/both-teams-to-score-predictions-tips/tomorrow/",
        "https://www.bettingtips.today/correct-score-predictions-tips/tomorrow/",
    ]
    OUTPUT_DIR = Path("output")
    FILE_PREFIX = "data_nav_menu"
    FILE_EXTENSION = ".csv"

    @classmethod
    def generate_filename(cls, suffix: str = None) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        suffix_part = f"_{suffix}" if suffix else ""
        filename = f"{cls.FILE_PREFIX.value}_{timestamp}{suffix_part}{cls.FILE_EXTENSION.value}"
        return str(cls.OUTPUT_DIR.value / filename)


class ConfigBettingtipsTodayWithouNave(Enum):
    SPIDER_NAME = "bettingtips_today_without_nave_spider"
    START_URLS_WITHOUT_NAVE = [
        # "https://www.bettingtips.today/yesterday/",
        "https://www.bettingtips.today/",
        "https://www.bettingtips.today/tomorrow/",
        # "https://www.bettingtips.today/day-after-tomorrow/",
        # "https://www.bettingtips.today/day-future/",
    ]

    OUTPUT_DIR = Path("output")
    FILE_PREFIX = "data"
    FILE_EXTENSION = ".csv"

    @classmethod
    def generate_filename(cls, suffix: str = None) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        suffix_part = f"_{suffix}" if suffix else ""
        filename = f"{cls.FILE_PREFIX.value}_{timestamp}{suffix_part}{cls.FILE_EXTENSION.value}"
        return str(cls.OUTPUT_DIR.value / filename)

