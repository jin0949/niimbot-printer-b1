# Niimbot B1 Printer Control Module

Niimbot B1 라벨 프린터 제어를 위한 Python 모듈입니다. 라벨 프린팅을 위한 기본적인 프린터 제어 및 이미지 출력 기능을 제공합니다.

## 프린터 사양

- 라벨 크기: 40mm x 30mm
- 이미지 해상도: 320 x 240 pixels (1:8 비율)

## 주요 기능

- 프린터 상태 모니터링
- 라벨 타입 및 농도 설정
- 이미지 프린팅
- 프린터 하트비트 체크
- RFID 및 디바이스 정보 조회

## 테스트 구성

- `test_printer_info`: 프린터 기본 정보 테스트
- `test_printer_heartbeat`: 하트비트 기능 테스트
- `test_printer_settings`: 프린터 설정 테스트
- `test_print_status`: 프린트 상태 확인
- `test_print_flow`: 프린팅 프로세스 테스트
- `test_print`: 실제 이미지 출력 테스트

## 사용 제한사항

- 단일 출력만 지원 (연속 출력시 print_image 반복 필요)
- 프린터 명령은 정의된 순서대로 전송 필요
- OS별 시리얼 포트 설정 필요 (Linux/Windows)

## 프린팅 프로세스

1. 프린터 초기화 및 설정
2. 프린트 시작 명령
3. 이미지 전송
4. 프린트 종료
5. 완료 대기

## 테스트 실행

```bash
pytest test_niimbot.py
```

## 주의사항

- 프린터 설정 후 안정화를 위해 5초 대기 필요
- 프린터 상태 확인 후 출력 진행 권장
- 에러 발생시 상세 로그 확인 가능

---
Perplexity로부터의 답변: pplx.ai/share
