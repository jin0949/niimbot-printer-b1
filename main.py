import time
from PIL import Image
from src.niimbot.niimbot_printer import NiimbotPrint
import logging

"""
Niimbot B1 프린터 제어 모듈

라벨 크기: 320(width) x 240(height) pixels
실제 용지: 40mm x 30mm (1:8 비율)

참고사항:
- 단일 출력만 지원 (연속 출력 불가능 만약 하고싶으면 print_image loop 돌려야함)
- 프린트 명령은 정해진 순서대로 전송해야 함
- 시리얼 포트는 OS별 설정 필요 (Linux/Windows)
"""


def print_image(printer: NiimbotPrint, image: Image.Image):
    try:
        # 프린트 시작
        assert printer.start_print(), "Failed to start print"
        assert printer.allow_print_clear(), "Failed to allow print clear"
        assert printer.start_page_print(), "Failed to start page print"

        # 이미지 설정 및 전송
        assert printer.set_dimension(image.height, image.width), "Failed to set dimensions"
        printer.send_image(image)

        # 프린트 종료
        assert printer.end_page_print(), "Failed to end page print"

        # 프린트 완료 대기
        while (status := printer.get_print_status()) and status['progress1'] != 100:
            time.sleep(0.1)

        assert printer.end_print(), "Failed to end print"

    except Exception as e:
        logging.error(f"Print failed: {str(e)}")
        raise RuntimeError(f"Print failed: {str(e)}") from e


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        niimbot = NiimbotPrint(label_type=1, density=5)

        # 5초 대기하는 이유는 setting이 사전에 되어야지 똑바로 출력하기 때문
        time.sleep(5)

        heartbeat = niimbot.heartbeat()
        print(heartbeat)
        assert heartbeat["powerlevel"] is not None, "connection error"

        # 테스트 이미지 로드 및 출력
        img = Image.open("./tests/img/test_print.png")
        print_image(niimbot, img)

        # 연속 출력
        # count = 3
        # for _ in range(count):
        #     print_image(niimbot, img)

    except Exception as e:
        logging.error(f"Error: {e}")
        exit(1)
