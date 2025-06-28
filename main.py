from color_formatter import ColorFormatter
from programmers import ProgrammersAPI
from dotenv import load_dotenv
import logging
import sys
import os 

load_dotenv()

PROGRAMMERS_ID = os.environ.get("PROGRAMMERS_ID")
COOKIE = os.environ.get("COOKIE")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(ColorFormatter(datefmt="%H:%M:%S"))

logger.handlers = [console_handler]

logging.info("설정 파일 불러오기 완료.")
logging.info(f" ㄴ ID: {PROGRAMMERS_ID}")
logging.info(f" ㄴ COOKIE: {COOKIE[:20]}...")
print()

programmers = ProgrammersAPI(PROGRAMMERS_ID, COOKIE)

curriculum_data = programmers.get_curriculum()

logging.info(f"캠퍼스 커리큘럼: {curriculum_data['weeksCount']}주차")

for i in range(1, curriculum_data["weeksCount"] + 1):
    print()
    logging.info(f"{i}주차 강의를 불러옵니다.")

    for part in curriculum_data["weeks"][i-1]["parts"]:
        part_data = programmers.get_part(part['id'])
        logging.info(f"{i}주차 {part_data['title']} | 강의 수: {part_data['lessonsCount']}")

        for lesson in part_data["lessons"]:
            if lesson["isFinished"] == False and lesson["type"] == "Video":
                status = programmers.finish_video(lesson['id'])
                if status == 200:
                    logging.info(f"강의 \"{lesson['title']}\"를 자동으로 이수했습니다. (ID: {lesson['id']})")
                else:
                    logging.error(f"강의 \"{lesson['title']}\"를 이수하는데 실패했습니다. (ID: {lesson['id']})")
