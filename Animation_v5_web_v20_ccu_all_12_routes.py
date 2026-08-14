# ============================================================
# Animation V5 Web v20
# - Responsive 1000x700 stage
# - Entire UI scales together with browser window
# - SVG assets isolated with data URI
# - Point To Point No.1 -> No.2 web animation
# ============================================================

from pathlib import Path
import base64
import json
import re

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# 기본 설정
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"

STAGE_WIDTH = 1000
STAGE_HEIGHT = 700


# ============================================================
# 로고
# ============================================================

AEROCOM_LOGO_X = 28
AEROCOM_LOGO_Y = 24
AEROCOM_LOGO_TARGET_WIDTH = 165

PAZKOREA_LOGO_X = 28
PAZKOREA_LOGO_Y = 58
PAZKOREA_LOGO_TARGET_WIDTH = 165


# ============================================================
# 메인 메뉴
# ============================================================

MAIN_MENU_BUTTON_X = 282
MAIN_MENU_BUTTON_WIDTH = 436
MAIN_MENU_BUTTON_HEIGHT = 105
MAIN_MENU_POINT_Y = 205
MAIN_MENU_CENTRAL_Y = 355
MAIN_MENU_FONT_SIZE = 28


# ============================================================
# Point To Point
# ============================================================

PTP_PIPE_LEFT_X = 310
PTP_PIPE_RIGHT_X = 725
PTP_PIPE_TOP_Y = 115
PTP_PIPE_RIGHT_END_Y = 410

PTP_BLOWER_X = 155
PTP_BLOWER_Y = 490
PTP_BLOWER_TARGET_HEIGHT = 82
PTP_BLOWER_MIRROR_HORIZONTAL = True

PTP_BLOWER_PORT_X_RATIO = 0.105
PTP_BLOWER_PORT_Y_RATIO = 0.010

PTP_BLOWER_PIPE_HORIZONTAL_Y = 430
PTP_BLOWER_PIPE_ELBOW_RADIUS = 28

PTP_STATION1_Y = 292
PTP_STATION2_Y = 292

PTP_SLIDE_STATION_TARGET_HEIGHT = 42
PTP_SLIDE_STATION_WIDTH_SCALE = 1.2
PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO = 0.32

PTP_STATION1_OFFSET_X = 0
PTP_STATION1_OFFSET_Y = 0
PTP_STATION2_OFFSET_X = 0
PTP_STATION2_OFFSET_Y = 0

PTP_STATION_LABEL_OFFSET_X = 68
PTP_STATION_LABEL_OFFSET_Y = -3

PTP_SEND_OFFSET_Y = 29
PTP_SEND_BUTTON_WIDTH = 58
PTP_SEND_BUTTON_HEIGHT = 27

PTP_STATION_HALF_HEIGHT = (
    PTP_SLIDE_STATION_TARGET_HEIGHT
    * 0.5
)

PTP_STATION1_TOP_PIPE_Y = (
    PTP_STATION1_Y
    - PTP_STATION_HALF_HEIGHT
)

PTP_STATION1_BOTTOM_PIPE_Y = (
    PTP_STATION1_Y
    + PTP_STATION_HALF_HEIGHT
)

PTP_STATION2_TOP_PIPE_Y = (
    PTP_STATION2_Y
    - PTP_STATION_HALF_HEIGHT
)

PTP_STATION2_BOTTOM_PIPE_Y = (
    PTP_STATION2_Y
    + PTP_STATION_HALF_HEIGHT
)

# 현재 확정값
PTP_CARRIER_SCALE = 1.1

# Point To Point carrier 기본 표시 높이
# 실제 화면에서는 아래 기본 높이에 PTP_CARRIER_SCALE을 곱합니다.
PTP_CARRIER_BASE_HEIGHT = 25

# Slide Station 상승 거리 / 시간
PTP_SLIDE_STATION_LIFT_DISTANCE = 62
PTP_SLIDE_STATION_MOVE_SECONDS = 0.45

# No.1 -> No.2 애니메이션 시간(초)
PTP_SOURCE_READY_HOLD_SECONDS = 0.30
PTP_SOURCE_STATION_UP_HOLD_SECONDS = 0.12
PTP_SOURCE_INSERT_SECONDS = 0.50
PTP_SOURCE_STATION_DOWN_HOLD_SECONDS = 0.15
PTP_1_TO_2_TRAVEL_SECONDS = 3.20
PTP_DEST_HIDDEN_HOLD_SECONDS = 0.20
PTP_DEST_STATION_UP_HOLD_SECONDS = 0.12
PTP_DEST_OUTPUT_SECONDS = 0.50
PTP_DEST_STATION_DOWN_HOLD_SECONDS = 0.15
PTP_FINAL_CARRIER_HOLD_SECONDS = 1.00

# carrier 외부 대기 / 배출 거리
PTP_CARRIER_SOURCE_READY_OFFSET_X = 42
PTP_CARRIER_DEST_OUTPUT_OFFSET_X = 48


# ============================================================
# Central Control Unit System
# V4 desktop v22 기준 정적 UI
# ============================================================

# ------------------------------------------------------------
# Diverter
# ------------------------------------------------------------
DIVERTER_CENTER_X = 210
DIVERTER_CENTER_Y = 358
DIVERTER_TARGET_WIDTH = 58

DIVERTER_LEFT_Y = 358
DIVERTER_RIGHT_TOP_Y = 344
DIVERTER_RIGHT_MIDDLE_Y = 358
DIVERTER_RIGHT_BOTTOM_Y = 371

# Desktop V22 diverter frames (1-based)
DIVERTER_MIDDLE_FRAME = 2
DIVERTER_TOP_FRAME = 32

# middle -> top
DIVERTER_TO_TOP_START_FRAME = 23

# top -> middle
DIVERTER_TO_MIDDLE_START_FRAME = 33
DIVERTER_TO_MIDDLE_END_FRAME = 42

# middle <-> bottom (Station No.3)
DIVERTER_BOTTOM_FRAME = 12
DIVERTER_TO_BOTTOM_START_FRAME = 3
DIVERTER_TO_BOTTOM_END_FRAME = 12
DIVERTER_BOTTOM_TO_MIDDLE_START_FRAME = 13
DIVERTER_BOTTOM_TO_MIDDLE_END_FRAME = 22


# ------------------------------------------------------------
# Central blower + bypass asset
# ------------------------------------------------------------
# ============================================================
# CCU blower.svg 크기 / 위치 직접 조정
# ============================================================
# TARGET_WIDTH : blower.svg 전체 크기
# OFFSET_X     : + 오른쪽 / - 왼쪽
# OFFSET_Y     : + 아래 / - 위
#
# 데스크톱 V22 원본값:
# BLOWER_TARGET_WIDTH = 165
# BLOWER_VISUAL_LEFT_Y = 361
BLOWER_TARGET_WIDTH = 165
BLOWER_PIPE_CENTER_Y_LOCAL = 22.5
BLOWER_VISUAL_LEFT_Y = 361
BLOWER_VISUAL_OFFSET_X = 1.5
BLOWER_VISUAL_OFFSET_Y = 0


# ------------------------------------------------------------
# Stations
# ------------------------------------------------------------

# TITAN Station No.1
STATION1_CENTER_X = 520
STATION1_TOP_Y = 20
STATION1_TARGET_HEIGHT = 115

# TITAN Station No.2
STATION2_CENTER_X = 520
STATION2_TOP_Y = 175
STATION2_TARGET_HEIGHT = 115

# EWS Station No.3
STATION3_CENTER_X = 255
STATION3_TOP_Y = 455
STATION3_TARGET_HEIGHT = 115

# EWS Station No.4
STATION4_CENTER_X = 675
STATION4_TOP_Y = 455
STATION4_TARGET_HEIGHT = 115


# ------------------------------------------------------------
# TITAN layered station
# ------------------------------------------------------------
TITAN_TOP_INNER_OFFSET_X = 6
TITAN_TOP_INNER_OFFSET_Y = 14

TITAN_MIDDLE_INNER_OFFSET_X = 6
TITAN_MIDDLE_INNER_OFFSET_Y = 14

# ============================================================
# TITAN SVG 세부 크기 / 위치 직접 조정
# ============================================================
#
# station_standard.svg는 기준 본체이므로 실제 SVG 크기로 표시합니다.
# 아래 값은 station_inner.svg / station_door.svg만 별도 미세조정합니다.
#
# SCALE_X/Y : 1.0 = 원본 크기
# OFFSET_X  : + 오른쪽 / - 왼쪽
# OFFSET_Y  : + 아래 / - 위
#
# 데스크톱 V22에서는 front에서 계산한 동일 scale을
# inner와 door에도 그대로 사용합니다.
TITAN_WIDTH_SCALE = 1.0

# station_inner.svg
TITAN_INNER_SCALE_X = 1.0
TITAN_INNER_SCALE_Y = 1.0
TITAN_INNER_ADJUST_X = 0
TITAN_INNER_ADJUST_Y = 0

# station_door.svg
# CLOSED_SCALE_X = 데스크톱 V22의 문 닫힘 원래 값
TITAN_DOOR_CLOSED_SCALE_X = 3.0793915
TITAN_DOOR_SCALE_X = 1.0
TITAN_DOOR_SCALE_Y = 1.0
TITAN_DOOR_ADJUST_X = 0
TITAN_DOOR_ADJUST_Y = 0

TITAN_DOOR_CLOSED_X_LOCAL = 154 / 20.0
TITAN_DOOR_Y_LOCAL = 223 / 20.0


# ------------------------------------------------------------
# EWS split station
# ------------------------------------------------------------
EWS_INLET_LOCAL_X = 77.46
EWS_INLET_LOCAL_Y = 787.98
EWS_INLET_SCALE_MULTIPLIER = 1.0

EWS3_INLET_OFFSET_X = 0
EWS3_INLET_OFFSET_Y = 0

EWS4_INLET_OFFSET_X = 0
EWS4_INLET_OFFSET_Y = 0


# ------------------------------------------------------------
# EWS basket
# ------------------------------------------------------------
BASKET_BACK_TARGET_WIDTH = 35
BASKET_BACK_TOP_Y = 565

BASKET3_BACK_OFFSET_X = -4
BASKET3_BACK_OFFSET_Y = 10

BASKET4_BACK_OFFSET_X = -4
BASKET4_BACK_OFFSET_Y = 10

BASKET_FRONT_TARGET_WIDTH = 46
BASKET_FRONT_TOP_Y = 565

BASKET3_FRONT_OFFSET_X = 0
BASKET3_FRONT_OFFSET_Y = 10

BASKET4_FRONT_OFFSET_X = 0
BASKET4_FRONT_OFFSET_Y = 10


# ------------------------------------------------------------
# Central pipe
# ------------------------------------------------------------
CENTRAL_TOP_PIPE_END_Y = 4
CENTRAL_TOP_PIPE_FLAT_SEGMENT_START_Y = 18

CENTRAL_PIPE_OUTER_WIDTH = 14
CENTRAL_PIPE_INNER_WIDTH = 11


# ------------------------------------------------------------
# Level lines
# ------------------------------------------------------------
CENTRAL_LEVEL_LINES = (
    165,
    312,
    620,
)


# ------------------------------------------------------------
# Labels / controls
# ------------------------------------------------------------
STATION_LABEL_FONT_SIZE = 9

STATION1_LABEL_X = 575
STATION1_LABEL_Y = 34

STATION2_LABEL_X = 575
STATION2_LABEL_Y = 190

STATION3_LABEL_X = 300
STATION3_LABEL_Y = 460

STATION4_LABEL_X = 720
STATION4_LABEL_Y = 460

SEND_BUTTON_WIDTH = 50
SEND_BUTTON_HEIGHT = 21

STATION1_SEND_X = 575
STATION1_SEND_Y = 55

STATION2_SEND_X = 575
STATION2_SEND_Y = 211

STATION3_SEND_X = 300
STATION3_SEND_Y = 481

STATION4_SEND_X = 720
STATION4_SEND_Y = 481


# ------------------------------------------------------------
# CCU 텍스트 / 버튼 / 전체 상하 위치
# ------------------------------------------------------------
# Station No.x 글씨: v13 대비 1.8배
CCU_STATION_LABEL_SCALE = 1.8

# Send 버튼 크기: v13 대비 1.3배
CCU_SEND_BUTTON_SCALE = 1.3

# Send 글씨: v13 대비 1.7배
CCU_SEND_FONT_SCALE = 1.7

# 로고와 Main 버튼을 제외한 CCU 전체를 아래로 이동
# +값 = 아래 / -값 = 위
CCU_CONTENT_OFFSET_Y = 20


# ============================================================
# CCU No.1 -> No.4 테스트 애니메이션
# 데스크톱 V22 좌표 / 시간 기준
# ============================================================

# 목적지 버튼
DEST_BUTTON_WIDTH = 62
DEST_BUTTON_HEIGHT = 21

# Send 버튼 오른쪽과 목적지 버튼 사이 간격
CCU_DEST_BUTTON_GAP_X = 4

# 목적지 버튼끼리의 세로 간격
CCU_DEST_BUTTON_GAP_Y = 2

# carrier 크기
CCU_CARRIER_SCALE_MULTIPLIER = 1.0

# No.1 투입
CARRIER_ENTRY_START_X = STATION1_CENTER_X + 30
CARRIER_ENTRY_START_Y = STATION1_TOP_Y + 38
CARRIER_ENTRY_END_X = STATION1_CENTER_X - 5
CARRIER_ENTRY_END_Y = STATION1_TOP_Y + 38

# No.1 -> pipe
CARRIER_PIPE_START_X = STATION1_CENTER_X
CARRIER_PIPE_START_Y = STATION1_TOP_Y + 118

# No.1 -> diverter top -> bypass
CARRIER_VERTICAL_END_X = STATION1_CENTER_X
CARRIER_VERTICAL_END_Y = 316

CARRIER_TOP_CURVE_C1_X = STATION1_CENTER_X
CARRIER_TOP_CURVE_C1_Y = 333
CARRIER_TOP_CURVE_C2_X = 510
CARRIER_TOP_CURVE_C2_Y = DIVERTER_RIGHT_TOP_Y
CARRIER_TOP_CURVE_END_X = 490
CARRIER_TOP_CURVE_END_Y = DIVERTER_RIGHT_TOP_Y

CARRIER_DIVERTER_TOP_ENTRY_X = 230
CARRIER_DIVERTER_TOP_ENTRY_Y = DIVERTER_RIGHT_TOP_Y

CARRIER_DIVERTER_EXIT_C1_X = 217
CARRIER_DIVERTER_EXIT_C1_Y = DIVERTER_RIGHT_TOP_Y
CARRIER_DIVERTER_EXIT_C2_X = 204
CARRIER_DIVERTER_EXIT_C2_Y = DIVERTER_LEFT_Y
CARRIER_DIVERTER_LEFT_EXIT_X = 190
CARRIER_DIVERTER_LEFT_EXIT_Y = DIVERTER_LEFT_Y

BYPASS_STOP_X = 104
BYPASS_STOP_Y = DIVERTER_LEFT_Y

# bypass -> No.4
CARRIER_NO4_STRAIGHT_END_X = 645
CARRIER_NO4_STRAIGHT_END_Y = DIVERTER_RIGHT_MIDDLE_Y

CARRIER_NO4_CURVE_C1_X = 665
CARRIER_NO4_CURVE_C1_Y = DIVERTER_RIGHT_MIDDLE_Y
CARRIER_NO4_CURVE_C2_X = STATION4_CENTER_X
CARRIER_NO4_CURVE_C2_Y = DIVERTER_RIGHT_MIDDLE_Y + 14
CARRIER_NO4_CURVE_END_X = STATION4_CENTER_X
CARRIER_NO4_CURVE_END_Y = DIVERTER_RIGHT_MIDDLE_Y + 39

CARRIER_NO4_PIPE_END_X = STATION4_CENTER_X
CARRIER_NO4_PIPE_END_Y = STATION4_TOP_Y

# No.4 내부 / 배출 / 바스켓
EWS4_HIDDEN_START_X = STATION4_CENTER_X + 11
# Web browser EWS No.4 hidden-start tuning
# +값을 크게 하면 캐리어가 더 아래에서 내부 이동을 시작합니다.
# v15의 +12에서는 캐리어 상단이 station 위로 노출되어 +32로 보정.
EWS4_HIDDEN_START_Y = STATION4_TOP_Y + 32

EWS4_OUTPUT_X = 686
EWS4_OUTPUT_Y = 500

EWS4_EMERGE_END_X = 686
EWS4_EMERGE_END_Y = 550

EWS4_BASKET_DROP_X = 670
EWS4_BASKET_DROP_Y = 610

EWS4_BASKET_DROP_ROTATION_DEG = -45.0

# 시간
TITAN_SEND_DOOR_OPEN_SECONDS = 0.35
TITAN_SEND_ENTRY_SECONDS = 0.60
TITAN_SEND_DOOR_CLOSE_SECONDS = 0.35
TITAN_SEND_TO_PIPE_SECONDS = 0.50

# No.1 도어 열림 -> carrier 투입 -> 도어 닫힘 구간 속도
# 1.0 = 기존 속도
# 0.8 = 기존의 80% 속도 = 시간은 1.25배 길어짐
TITAN_LOAD_SEQUENCE_SPEED = 0.8

NO1_TO_BYPASS_SECONDS = 3.20
BYPASS_TO_NO4_SECONDS = 3.00

EWS_RECEIVE_INSIDE_SECONDS = 0.85
EWS_RECEIVE_EMERGE_SECONDS = 0.45
EWS_RECEIVE_DROP_SECONDS = 0.90

# TITAN door open state (desktop V22)
TITAN_DOOR_OPEN_SCALE_X = 1.0
TITAN_DOOR_OPEN_X_LOCAL = 89 / 20.0


# ============================================================
# CCU No.4 -> No.1 테스트 애니메이션
# 데스크톱 V22 좌표 / 시간 기준
# ============================================================

# No.4 EWS 투입구 안착 위치
EWS4_SEND_LOAD_X = STATION4_CENTER_X - 9
EWS4_SEND_LOAD_Y = STATION4_TOP_Y + 104

# No.1 TITAN 투입과 동일한 수평 접근 거리
EWS4_SEND_ENTRY_DISTANCE_X = (
    CARRIER_ENTRY_START_X
    - CARRIER_ENTRY_END_X
)

EWS4_SEND_ENTRY_START_X = (
    EWS4_SEND_LOAD_X
    + EWS4_SEND_ENTRY_DISTANCE_X
)
EWS4_SEND_ENTRY_START_Y = EWS4_SEND_LOAD_Y

# 투입구에서 X 고정 수직 상승
EWS4_SEND_HIDDEN_X = EWS4_SEND_LOAD_X
EWS4_SEND_HIDDEN_Y = STATION4_TOP_Y + 60

# carrier 전체가 EWS 본체에 가려진 뒤
# 상부 배관 중심 X로 수평 이동
EWS4_SEND_HIDDEN_PIPE_X = CARRIER_NO4_PIPE_END_X
EWS4_SEND_HIDDEN_PIPE_Y = EWS4_SEND_HIDDEN_Y

# 상부 배관으로 다시 수직 상승
EWS4_SEND_PIPE_EXIT_X = CARRIER_NO4_PIPE_END_X
EWS4_SEND_PIPE_EXIT_Y = CARRIER_NO4_PIPE_END_Y

# No.1 수신
NO1_RECEIVE_PIPE_X = CARRIER_PIPE_START_X
NO1_RECEIVE_PIPE_Y = CARRIER_PIPE_START_Y

NO1_RECEIVE_BODY_X = STATION1_CENTER_X
NO1_RECEIVE_BODY_HIDDEN_Y = STATION1_TOP_Y + 20

NO1_RECEIVE_OUTPUT_X = STATION1_CENTER_X - 1.5
NO1_RECEIVE_OUTPUT_HIDDEN_Y = STATION1_TOP_Y + 20
NO1_RECEIVE_OUTPUT_EMERGE_Y = STATION1_TOP_Y + 76

NO1_RECEIVE_BASKET_DROP_X = NO1_RECEIVE_OUTPUT_X
NO1_RECEIVE_BASKET_DROP_Y = STATION1_TOP_Y + 103

# No.4 송신 시간
EWS4_SEND_ENTRY_SECONDS = 0.60
EWS4_SEND_LOAD_HOLD_SECONDS = 0.12
EWS4_SEND_VERTICAL_HIDE_SECONDS = 0.50
EWS4_SEND_HIDDEN_SHIFT_SECONDS = 0.15
EWS4_SEND_PIPE_RISE_SECONDS = 0.30

# 배관 이동 시간
NO4_TO_BYPASS_SECONDS = 3.00
BYPASS_TO_NO1_SECONDS = 3.20

# No.1 수신 시간
NO1_RECEIVE_RISE_SECONDS = 0.65
NO1_RECEIVE_HIDDEN_WAIT_SECONDS = 0.70
NO1_RECEIVE_REDIRECT_SECONDS = 0.25
NO1_RECEIVE_EMERGE_SECONDS = 0.40
NO1_RECEIVE_DROP_SECONDS = 0.75

NO1_RECEIVE_DROP_ROTATION_DEG = -45.0

# Station No.2 TITAN 수신은 No.1과 같은 낙하각
NO2_RECEIVE_DROP_ROTATION_DEG = NO1_RECEIVE_DROP_ROTATION_DEG

# Station No.3 EWS 수신은 No.4와 같은 낙하각
EWS3_BASKET_DROP_ROTATION_DEG = EWS4_BASKET_DROP_ROTATION_DEG

# No.2 -> No.1 직통 수직배관 상승 시 X 미세조정
TITAN_2_TO_1_DIRECT_PIPE_OFFSET_X = 3.0


# ============================================================
# 색상
# ============================================================

PIPE_OUTLINE = "#282828"
PIPE_FILL = "#cdcdff"
LABEL_RED = "#dc0000"


# ============================================================
# 좌표 -> Stage 백분율
# ============================================================

def px(value: float) -> str:
    return (
        f"{value / STAGE_WIDTH * 100:.6f}%"
    )


def py(value: float) -> str:
    return (
        f"{value / STAGE_HEIGHT * 100:.6f}%"
    )


def pw(value: float) -> str:
    return (
        f"{value / STAGE_WIDTH * 100:.6f}%"
    )


def ph(value: float) -> str:
    return (
        f"{value / STAGE_HEIGHT * 100:.6f}%"
    )


# ============================================================
# Streamlit
# ============================================================

st.set_page_config(
    page_title="Aerocom System Simulator",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.html(
    """
    <style>
        html,
        body,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        .stApp {
            background: #ffffff !important;
            overflow: hidden !important;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        footer {
            display: none !important;
        }

        .block-container,
        [data-testid="stMainBlockContainer"] {
            width: 100% !important;
            max-width: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* PTP의 JavaScript animation iframe도 브라우저 높이에 맞춥니다. */
        [data-testid="stCustomComponentV1"],
        [data-testid="stCustomComponentV1"] iframe,
        iframe[title="st.iframe"] {
            width: 100% !important;
            height: 100vh !important;
            border: 0 !important;
        }
    </style>
    """
)


# ============================================================
# Asset helpers
# ============================================================

def read_svg(filename: str) -> str:
    path = ASSET_DIR / filename

    if not path.exists():
        return ""

    return path.read_text(
        encoding="utf-8",
        errors="ignore",
    )


def file_data_uri(filename: str) -> str:
    path = ASSET_DIR / filename

    if not path.exists():
        return ""

    data = base64.b64encode(
        path.read_bytes()
    ).decode("ascii")

    return (
        "data:image/svg+xml;base64,"
        + data
    )


def svg_string_data_uri(
    svg_text: str,
) -> str:

    data = base64.b64encode(
        svg_text.encode("utf-8")
    ).decode("ascii")

    return (
        "data:image/svg+xml;base64,"
        + data
    )


def binary_file_data_uri(
    path: Path,
    mime_type: str,
) -> str:
    if not path.exists():
        return ""

    data = base64.b64encode(
        path.read_bytes()
    ).decode("ascii")

    return (
        f"data:{mime_type};base64,"
        + data
    )


def first_existing_asset(
    *names: str,
) -> Path | None:
    for name in names:
        path = ASSET_DIR / name

        if path.exists():
            return path

    return None


def natural_sort_key_path(
    path: Path,
):
    return [
        int(part)
        if part.isdigit()
        else part.lower()
        for part in re.split(
            r"(\d+)",
            path.name,
        )
    ]


def svg_viewbox(
    svg_text: str,
    default=(0.0, 0.0, 100.0, 100.0),
):
    match = re.search(
        r'viewBox\s*=\s*["\']\s*'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)'
        r'\s*["\']',
        svg_text,
        flags=re.IGNORECASE,
    )

    if not match:
        return default

    return (
        float(match.group(1)),
        float(match.group(2)),
        float(match.group(3)),
        float(match.group(4)),
    )


def svg_intrinsic_box(
    svg_text: str,
    default=(0.0, 0.0, 100.0, 100.0),
):
    """
    SVG 실제 좌표계 크기를 읽습니다.

    1) viewBox가 있으면 viewBox 사용
    2) viewBox가 없으면 <svg width="..." height="..."> 사용

    FFDec에서 추출한 blower.svg / station_standard.svg /
    station_inner.svg / station_door.svg는 viewBox 없이
    width/height만 있기 때문에 이 처리가 반드시 필요합니다.
    """
    viewbox_match = re.search(
        r'viewBox\s*=\s*["\']\s*'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)'
        r'\s*["\']',
        svg_text,
        flags=re.IGNORECASE,
    )

    if viewbox_match:
        return (
            float(viewbox_match.group(1)),
            float(viewbox_match.group(2)),
            float(viewbox_match.group(3)),
            float(viewbox_match.group(4)),
        )

    width_match = re.search(
        r'<svg\b[^>]*\bwidth\s*=\s*["\']\s*'
        r'([-\d.]+)'
        r'(?:px)?\s*["\']',
        svg_text,
        flags=re.IGNORECASE,
    )

    height_match = re.search(
        r'<svg\b[^>]*\bheight\s*=\s*["\']\s*'
        r'([-\d.]+)'
        r'(?:px)?\s*["\']',
        svg_text,
        flags=re.IGNORECASE,
    )

    if width_match and height_match:
        return (
            0.0,
            0.0,
            float(width_match.group(1)),
            float(height_match.group(1)),
        )

    return default


def svg_viewbox_size(
    svg_text: str,
    default=(100.0, 100.0),
):
    match = re.search(
        r'viewBox\s*=\s*["\']\s*'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)\s+'
        r'([-\d.]+)'
        r'\s*["\']',
        svg_text,
        flags=re.IGNORECASE,
    )

    if not match:
        return default

    return (
        float(match.group(3)),
        float(match.group(4)),
    )


AEROCOM_URI = file_data_uri(
    "aerocom_logo.svg"
)

PAZKOREA_URI = file_data_uri(
    "pazkorea_logo.svg"
)

SLIDE_STATION_SVG_TEXT = read_svg(
    "슬라이드 스테이션.svg"
)

SLIDE_STATION_URI = file_data_uri(
    "슬라이드 스테이션.svg"
)

PTP_BLOWER_SVG_TEXT = read_svg(
    "blower(PTP용).svg"
)

PTP_BLOWER_URI = file_data_uri(
    "blower(PTP용).svg"
)

CARRIER_SVG_TEXT = read_svg(
    "carrier.svg"
)

CARRIER_URI = file_data_uri(
    "carrier.svg"
)


# ============================================================
# CCU assets
# ============================================================

TITAN_STANDARD_SVG_TEXT = read_svg(
    "station_standard.svg"
)

if not TITAN_STANDARD_SVG_TEXT:
    TITAN_STANDARD_SVG_TEXT = read_svg(
        "100.svg"
    )

TITAN_STANDARD_PATH = first_existing_asset(
    "station_standard.svg",
    "100.svg",
)

TITAN_STANDARD_URI = (
    binary_file_data_uri(
        TITAN_STANDARD_PATH,
        "image/svg+xml",
    )
    if TITAN_STANDARD_PATH
    else ""
)


TITAN_INNER_SVG_TEXT = read_svg(
    "station_inner.svg"
)

if not TITAN_INNER_SVG_TEXT:
    TITAN_INNER_SVG_TEXT = read_svg(
        "98.svg"
    )

TITAN_INNER_PATH = first_existing_asset(
    "station_inner.svg",
    "98.svg",
)

TITAN_INNER_URI = (
    binary_file_data_uri(
        TITAN_INNER_PATH,
        "image/svg+xml",
    )
    if TITAN_INNER_PATH
    else ""
)


TITAN_DOOR_SVG_TEXT = read_svg(
    "station_door.svg"
)

if not TITAN_DOOR_SVG_TEXT:
    TITAN_DOOR_SVG_TEXT = read_svg(
        "99.svg"
    )

TITAN_DOOR_PATH = first_existing_asset(
    "station_door.svg",
    "99.svg",
)

TITAN_DOOR_URI = (
    binary_file_data_uri(
        TITAN_DOOR_PATH,
        "image/svg+xml",
    )
    if TITAN_DOOR_PATH
    else ""
)


EWS_BODY_PATH = first_existing_asset(
    "EWS 스테이션 본체.svg",
    "EWS_station_body.svg",
)

EWS_BODY_SVG_TEXT = (
    EWS_BODY_PATH.read_text(
        encoding="utf-8",
        errors="ignore",
    )
    if EWS_BODY_PATH
    else ""
)

EWS_BODY_URI = (
    binary_file_data_uri(
        EWS_BODY_PATH,
        "image/svg+xml",
    )
    if EWS_BODY_PATH
    else ""
)


EWS_INLET_PATH = first_existing_asset(
    "EWS 스테이션 투입구.svg",
    "EWS_station_inlet.svg",
)

EWS_INLET_SVG_TEXT = (
    EWS_INLET_PATH.read_text(
        encoding="utf-8",
        errors="ignore",
    )
    if EWS_INLET_PATH
    else ""
)

EWS_INLET_URI = (
    binary_file_data_uri(
        EWS_INLET_PATH,
        "image/svg+xml",
    )
    if EWS_INLET_PATH
    else ""
)


EWS_FALLBACK_PATH = first_existing_asset(
    "EWS 스테이션.svg",
    "ews_station.svg",
    "EWS_station.svg",
)

EWS_FALLBACK_SVG_TEXT = (
    EWS_FALLBACK_PATH.read_text(
        encoding="utf-8",
        errors="ignore",
    )
    if EWS_FALLBACK_PATH
    else ""
)

EWS_FALLBACK_URI = (
    binary_file_data_uri(
        EWS_FALLBACK_PATH,
        "image/svg+xml",
    )
    if EWS_FALLBACK_PATH
    else ""
)


BASKET_BACK_PATH = first_existing_asset(
    "basket back.svg",
    "basket_back.svg",
)

BASKET_BACK_URI = (
    binary_file_data_uri(
        BASKET_BACK_PATH,
        "image/svg+xml",
    )
    if BASKET_BACK_PATH
    else ""
)


BASKET_FRONT_PATH = first_existing_asset(
    "basket.svg",
)

BASKET_FRONT_URI = (
    binary_file_data_uri(
        BASKET_FRONT_PATH,
        "image/svg+xml",
    )
    if BASKET_FRONT_PATH
    else ""
)


CENTRAL_BLOWER_PATH = first_existing_asset(
    "blower.svg",
    "71.svg",
)

CENTRAL_BLOWER_SVG_TEXT = (
    CENTRAL_BLOWER_PATH.read_text(
        encoding="utf-8",
        errors="ignore",
    )
    if CENTRAL_BLOWER_PATH
    else ""
)

CENTRAL_BLOWER_URI = (
    binary_file_data_uri(
        CENTRAL_BLOWER_PATH,
        "image/svg+xml",
    )
    if CENTRAL_BLOWER_PATH
    else ""
)


DIVERTER_URI = ""
DIVERTER_FRAME_URIS = {}

diverter_folder = (
    ASSET_DIR
    / "diverter_frames"
)

if diverter_folder.exists():
    diverter_frames = sorted(
        diverter_folder.rglob("*.png"),
        key=natural_sort_key_path,
    )

    if diverter_frames:
        # v20: middle/top/bottom 전체 전환 프레임
        needed_frame_numbers = list(
            range(
                DIVERTER_MIDDLE_FRAME,
                DIVERTER_TO_MIDDLE_END_FRAME + 1,
            )
        )

        for frame_number in needed_frame_numbers:
            frame_index = frame_number - 1

            if (
                0
                <= frame_index
                < len(diverter_frames)
            ):
                DIVERTER_FRAME_URIS[
                    frame_number
                ] = binary_file_data_uri(
                    diverter_frames[
                        frame_index
                    ],
                    "image/png",
                )

        DIVERTER_URI = (
            DIVERTER_FRAME_URIS.get(
                DIVERTER_MIDDLE_FRAME,
                "",
            )
        )


# ============================================================
# Responsive stage CSS
# ============================================================

def common_stage_css() -> str:
    return f"""
    <style>
        * {{
            box-sizing: border-box;
        }}

        .web-stage-wrap {{
            position: relative;
            width: 100vw;
            height: 100vh;

            display: flex;
            justify-content: center;
            align-items: flex-start;

            background: #ffffff;
            overflow: hidden;
        }}

        /*
        1000 x 700 전체 장면을 통째로 확대/축소합니다.

        브라우저 가로폭과 세로높이 중 작은 제한에 맞춰
        항상 1000:700 비율을 유지합니다.
        */
        .web-stage {{
            position: relative;

            width: min(
                100vw,
                calc(100vh * {STAGE_WIDTH / STAGE_HEIGHT:.10f})
            );

            aspect-ratio:
                {STAGE_WIDTH}
                /
                {STAGE_HEIGHT};

            flex: 0 0 auto;

            background: #ffffff;
            font-family:
                Arial,
                "Malgun Gothic",
                sans-serif;

            overflow: hidden;

            /*
            cqw 단위를 사용하기 위한 container.
            1000px 기준 글씨 14px = 1.4cqw
            */
            container-type: inline-size;
        }}

        .menu-button {{
            position: absolute;

            display: flex;
            align-items: center;
            justify-content: center;

            text-decoration: none !important;

            background: #d9d9d9;

            border:
                0.10cqw
                solid
                #333333;

            border-radius: 1.8cqw;

            color: #000000 !important;

            font-weight: 700;
            line-height: 1.1;

            cursor: pointer;
            user-select: none;
            overflow: hidden;
        }}

        .menu-button:hover {{
            background: #e5e5e5;
        }}

        .menu-button:active {{
            background: #cfcfcf;
        }}

        .main-return {{
            position: absolute;

            right: {px(25)};
            top: {py(20)};

            width: {pw(65)};
            height: {ph(27)};

            display: flex;
            align-items: center;
            justify-content: center;

            border:
                0.10cqw
                solid
                #999999;

            border-radius: 0.4cqw;

            background: #eeeeee;

            color: #111111 !important;
            text-decoration: none !important;

            font-size: 1.2cqw;
            font-weight: 600;

            z-index: 200;
        }}

        .ptp-station-label {{
            position: absolute;

            color: {LABEL_RED};

            font-size: 1.8cqw;
            font-weight: 700;
            line-height: 1;

            white-space: nowrap;

            z-index: 100;
        }}

        .ptp-send {{
            position: absolute;

            border:
                0.10cqw
                solid
                #aaaaaa;

            background:
                linear-gradient(
                    #f4f4f4,
                    #dddddd
                );

            color: #111111;

            font-size: 1.7cqw;

            display: flex;
            align-items: center;
            justify-content: center;

            box-shadow:
                inset
                0
                0
                0
                0.10cqw
                #eeeeee;

            z-index: 100;
            user-select: none;
        }}

        .placeholder-title {{
            position: absolute;

            left: 50%;
            top: 43%;

            transform:
                translate(
                    -50%,
                    -50%
                );

            font-size: 2.8cqw;
            font-weight: 700;

            color: #111111;

            white-space: nowrap;
        }}

        .placeholder-sub {{
            position: absolute;

            left: 50%;
            top: 50%;

            transform:
                translate(
                    -50%,
                    -50%
                );

            font-size: 1.5cqw;

            color: #555555;

            white-space: nowrap;
        }}
    </style>
    """


# ============================================================
# Responsive image
# ============================================================

def image_html(
    uri: str,
    x: float,
    y: float,
    width: float,
    height: float | None = None,
    z: int = 100,
    extra_style: str = "",
) -> str:

    if not uri:
        return ""

    if height is None:
        height_css = "height:auto;"
    else:
        height_css = (
            f"height:{ph(height)};"
        )

    return f"""
        <img
            src="{uri}"
            draggable="false"

            style="
                position:absolute;

                left:{px(x)};
                top:{py(y)};

                width:{pw(width)};
                {height_css}

                z-index:{z};

                display:block;

                {extra_style}
            "
        />
    """


def logo_html(
    uri: str,
    x: float,
    y: float,
    width: float,
) -> str:

    return image_html(
        uri=uri,
        x=x,
        y=y,
        width=width,
        height=None,
        z=100,
    )


# ============================================================
# PTP blower
# ============================================================

def ptp_blower_html():
    if not (
        PTP_BLOWER_URI
        and PTP_BLOWER_SVG_TEXT
    ):
        return (
            "",
            PTP_BLOWER_X,
            PTP_BLOWER_Y,
        )

    vb_w, vb_h = svg_viewbox_size(
        PTP_BLOWER_SVG_TEXT,
        default=(
            37.5,
            56.5,
        ),
    )

    scale = (
        PTP_BLOWER_TARGET_HEIGHT
        / vb_h
    )

    width = (
        vb_w
        * scale
    )

    mirror_style = ""

    if PTP_BLOWER_MIRROR_HORIZONTAL:
        mirror_style = (
            "transform:scaleX(-1);"
            "transform-origin:center center;"
        )

    html = image_html(
        uri=PTP_BLOWER_URI,
        x=PTP_BLOWER_X,
        y=PTP_BLOWER_Y,
        width=width,
        height=PTP_BLOWER_TARGET_HEIGHT,
        z=20,
        extra_style=mirror_style,
    )

    if PTP_BLOWER_MIRROR_HORIZONTAL:
        port_x = (
            PTP_BLOWER_X
            + width
            * PTP_BLOWER_PORT_X_RATIO
        )
    else:
        port_x = (
            PTP_BLOWER_X
            + width
            * (
                1.0
                - PTP_BLOWER_PORT_X_RATIO
            )
        )

    port_y = (
        PTP_BLOWER_Y
        + PTP_BLOWER_TARGET_HEIGHT
        * PTP_BLOWER_PORT_Y_RATIO
    )

    return (
        html,
        port_x,
        port_y,
    )


# ============================================================
# PTP slide station
# ============================================================

def ptp_slide_station_html(
    station_no: int,
    pipe_x: float,
    center_y: float,
) -> str:

    if not (
        SLIDE_STATION_URI
        and SLIDE_STATION_SVG_TEXT
    ):
        return ""

    vb_w, vb_h = svg_viewbox_size(
        SLIDE_STATION_SVG_TEXT,
        default=(
            177.0,
            319.57,
        ),
    )

    scale = (
        PTP_SLIDE_STATION_TARGET_HEIGHT
        / vb_h
    )

    width = (
        vb_w
        * scale
    )

    if station_no == 1:
        offset_x = (
            PTP_STATION1_OFFSET_X
        )
        offset_y = (
            PTP_STATION1_OFFSET_Y
        )
    else:
        offset_x = (
            PTP_STATION2_OFFSET_X
        )
        offset_y = (
            PTP_STATION2_OFFSET_Y
        )

    left = (
        pipe_x
        - width
        * PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO
        + offset_x
    )

    top = (
        center_y
        - PTP_SLIDE_STATION_TARGET_HEIGHT
        / 2
        + offset_y
    )

    return image_html(
        uri=SLIDE_STATION_URI,
        x=left,
        y=top,
        width=width,
        height=(
            PTP_SLIDE_STATION_TARGET_HEIGHT
        ),
        z=30,
    )


# ============================================================
# PTP pipe
# ============================================================

def ptp_pipe_image_html(
    blower_port_x: float,
    blower_port_y: float,
) -> str:

    r = (
        PTP_BLOWER_PIPE_ELBOW_RADIUS
    )

    k = 0.5522847498

    elbow_start_y = (
        PTP_BLOWER_PIPE_HORIZONTAL_Y
        + r
    )

    elbow_end_x = (
        blower_port_x
        + r
    )

    lower_path = (
        f"M {blower_port_x:.3f} "
        f"{blower_port_y:.3f} "

        f"L {blower_port_x:.3f} "
        f"{elbow_start_y:.3f} "

        f"C {blower_port_x:.3f} "
        f"{elbow_start_y - k*r:.3f}, "

        f"{elbow_end_x - k*r:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y:.3f}, "

        f"{elbow_end_x:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y:.3f} "

        f"L {PTP_PIPE_LEFT_X - 28:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y:.3f} "

        f"C {PTP_PIPE_LEFT_X - 12:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y:.3f}, "

        f"{PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y - 12:.3f}, "

        f"{PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_BLOWER_PIPE_HORIZONTAL_Y - 30:.3f} "

        f"L {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_STATION1_BOTTOM_PIPE_Y:.3f}"
    )

    upper_path = (
        f"M {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_STATION1_TOP_PIPE_Y:.3f} "

        f"L {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 28:.3f} "

        f"C {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 12:.3f}, "

        f"{PTP_PIPE_LEFT_X + 12:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f}, "

        f"{PTP_PIPE_LEFT_X + 28:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f} "

        f"L {PTP_PIPE_RIGHT_X - 28:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f} "

        f"C {PTP_PIPE_RIGHT_X - 12:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f}, "

        f"{PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 12:.3f}, "

        f"{PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 28:.3f} "

        f"L {PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_STATION2_TOP_PIPE_Y:.3f}"
    )

    right_lower_path = (
        f"M {PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_STATION2_BOTTOM_PIPE_Y:.3f} "

        f"L {PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_PIPE_RIGHT_END_Y:.3f}"
    )

    def double_stroke(
        path_d: str,
    ) -> str:

        return f"""
        <path
            d="{path_d}"

            fill="none"

            stroke="{PIPE_OUTLINE}"
            stroke-width="16"

            stroke-linecap="butt"
            stroke-linejoin="round"
        />

        <path
            d="{path_d}"

            fill="none"

            stroke="{PIPE_FILL}"
            stroke-width="13"

            stroke-linecap="butt"
            stroke-linejoin="round"
        />
        """

    pipe_svg = f"""
    <svg
        xmlns="http://www.w3.org/2000/svg"

        viewBox="
            0
            0
            {STAGE_WIDTH}
            {STAGE_HEIGHT}
        "

        width="{STAGE_WIDTH}"
        height="{STAGE_HEIGHT}"
    >
        {double_stroke(lower_path)}
        {double_stroke(upper_path)}
        {double_stroke(right_lower_path)}
    </svg>
    """

    pipe_uri = (
        svg_string_data_uri(
            pipe_svg
        )
    )

    return image_html(
        uri=pipe_uri,
        x=0,
        y=0,
        width=STAGE_WIDTH,
        height=STAGE_HEIGHT,
        z=5,
        extra_style=(
            "pointer-events:none;"
        ),
    )


# ============================================================
# CCU HTML helpers
# ============================================================

def centered_image_html(
    uri: str,
    center_x: float,
    top_y: float,
    width: float,
    z: int,
    extra_style: str = "",
) -> str:
    if not uri:
        return ""

    return f"""
        <img
            src="{uri}"
            draggable="false"
            style="
                position:absolute;
                left:{px(center_x)};
                top:{py(top_y)};
                width:{pw(width)};
                height:auto;
                transform:translateX(-50%);
                transform-origin:center center;
                z-index:{z};
                display:block;
                {extra_style}
            "
        />
    """


def centered_middle_image_html(
    uri: str,
    center_x: float,
    center_y: float,
    width: float,
    z: int,
    mirror_horizontal: bool = False,
) -> str:
    if not uri:
        return ""

    mirror = (
        " scaleX(-1)"
        if mirror_horizontal
        else ""
    )

    return f"""
        <img
            src="{uri}"
            draggable="false"
            style="
                position:absolute;
                left:{px(center_x)};
                top:{py(center_y)};
                width:{pw(width)};
                height:auto;
                transform:
                    translate(-50%, -50%)
                    {mirror};
                transform-origin:center center;
                z-index:{z};
                display:block;
            "
        />
    """


def ccu_titan_station_html(
    center_x: float,
    top_y: float,
    target_height: float,
    inner_offset_x: float,
    inner_offset_y: float,
) -> str:
    if not (
        TITAN_STANDARD_URI
        and TITAN_STANDARD_SVG_TEXT
    ):
        return ""

    _, _, front_w, front_h = svg_intrinsic_box(
        TITAN_STANDARD_SVG_TEXT,
        default=(
            0,
            0,
            100,
            100,
        ),
    )

    if front_h <= 0:
        return ""

    scale = (
        target_height
        / front_h
    )

    front_width = (
        front_w
        * scale
    )

    front_left = (
        center_x
        - front_width / 2
    )

    # --------------------------------------------------------
    # Qt desktop의 QGraphicsSvgItem.boundingRect()와
    # browser SVG viewBox의 가로 보이는 폭 차이를 보정합니다.
    #
    # 모든 레이어의 X 위치와 폭을 동일한 center_x 기준으로
    # 압축하므로 front / inner / door 정렬은 그대로 유지됩니다.
    # --------------------------------------------------------
    def titan_x(value: float) -> float:
        return (
            center_x
            + (
                value
                - center_x
            )
            * TITAN_WIDTH_SCALE
        )

    def titan_w(value: float) -> float:
        return (
            value
            * TITAN_WIDTH_SCALE
        )

    html_parts = []

    # --------------------------------------------------------
    # station_inner.svg
    # --------------------------------------------------------
    if (
        TITAN_INNER_URI
        and TITAN_INNER_SVG_TEXT
    ):
        _, _, inner_w, inner_h = svg_intrinsic_box(
            TITAN_INNER_SVG_TEXT,
            default=(
                0,
                0,
                front_w,
                front_h,
            ),
        )

        html_parts.append(
            image_html(
                uri=TITAN_INNER_URI,
                x=(
                    titan_x(
                        front_left
                        + inner_offset_x
                    )
                    + TITAN_INNER_ADJUST_X
                ),
                y=(
                    top_y
                    + inner_offset_y
                    + TITAN_INNER_ADJUST_Y
                ),
                width=(
                    titan_w(
                        inner_w
                        * scale
                    )
                    * TITAN_INNER_SCALE_X
                ),
                height=(
                    inner_h
                    * scale
                    * TITAN_INNER_SCALE_Y
                ),
                # Web Z-order:
                # inner(47) -> carrier(48) -> door(49) -> front(50)
                z=47,
            )
        )

    # --------------------------------------------------------
    # station_door.svg - closed state
    # --------------------------------------------------------
    if (
        TITAN_DOOR_URI
        and TITAN_DOOR_SVG_TEXT
    ):
        _, _, door_w, door_h = svg_intrinsic_box(
            TITAN_DOOR_SVG_TEXT,
            default=(
                0,
                0,
                10,
                10,
            ),
        )

        door_x = (
            front_left
            + TITAN_DOOR_CLOSED_X_LOCAL
            * scale
        )

        door_y = (
            top_y
            + TITAN_DOOR_Y_LOCAL
            * scale
        )

        html_parts.append(
            image_html(
                uri=TITAN_DOOR_URI,
                x=(
                    titan_x(
                        door_x
                    )
                    + TITAN_DOOR_ADJUST_X
                ),
                y=(
                    door_y
                    + TITAN_DOOR_ADJUST_Y
                ),
                width=(
                    titan_w(
                        door_w
                        * scale
                        * TITAN_DOOR_CLOSED_SCALE_X
                    )
                    * TITAN_DOOR_SCALE_X
                ),
                height=(
                    door_h
                    * scale
                    * TITAN_DOOR_SCALE_Y
                ),
                z=49,
            )
        )

    # --------------------------------------------------------
    # station_standard.svg - front
    # --------------------------------------------------------
    html_parts.append(
        image_html(
            uri=TITAN_STANDARD_URI,
            x=titan_x(
                front_left
            ),
            y=top_y,
            width=titan_w(
                front_width
            ),
            height=target_height,
            z=50,
        )
    )

    return "".join(
        html_parts
    )


def ccu_ews_station_html(
    center_x: float,
    top_y: float,
    target_height: float,
    inlet_offset_x: float,
    inlet_offset_y: float,
) -> str:
    # split EWS 우선
    if (
        EWS_BODY_URI
        and EWS_BODY_SVG_TEXT
        and EWS_INLET_URI
        and EWS_INLET_SVG_TEXT
    ):
        _, _, body_w, body_h = svg_viewbox(
            EWS_BODY_SVG_TEXT,
            default=(
                0,
                0,
                438,
                1044,
            ),
        )

        if body_h <= 0:
            return ""

        body_scale = (
            target_height
            / body_h
        )

        body_width = (
            body_w
            * body_scale
        )

        body_left = (
            center_x
            - body_width / 2
        )

        _, _, inlet_w, inlet_h = svg_viewbox(
            EWS_INLET_SVG_TEXT,
            default=(
                0,
                0,
                100,
                100,
            ),
        )

        inlet_scale = (
            body_scale
            * EWS_INLET_SCALE_MULTIPLIER
        )

        inlet_left = (
            body_left
            + EWS_INLET_LOCAL_X
            * body_scale
            + inlet_offset_x
        )

        inlet_top = (
            top_y
            + EWS_INLET_LOCAL_Y
            * body_scale
            + inlet_offset_y
        )

        inlet_html = image_html(
            uri=EWS_INLET_URI,
            x=inlet_left,
            y=inlet_top,
            width=(
                inlet_w
                * inlet_scale
            ),
            height=(
                inlet_h
                * inlet_scale
            ),
            z=57,
        )

        body_html = image_html(
            uri=EWS_BODY_URI,
            x=body_left,
            y=top_y,
            width=body_width,
            height=target_height,
            z=60,
        )

        return (
            inlet_html
            + body_html
        )

    # fallback 통합 SVG
    if (
        EWS_FALLBACK_URI
        and EWS_FALLBACK_SVG_TEXT
    ):
        _, _, vb_w, vb_h = svg_viewbox(
            EWS_FALLBACK_SVG_TEXT,
            default=(
                0,
                0,
                438,
                1044,
            ),
        )

        if vb_h <= 0:
            return ""

        width = (
            vb_w
            * target_height
            / vb_h
        )

        return image_html(
            uri=EWS_FALLBACK_URI,
            x=(
                center_x
                - width / 2
            ),
            y=top_y,
            width=width,
            height=target_height,
            z=60,
        )

    return ""


def ccu_basket_html(
    uri: str,
    center_x: float,
    top_y: float,
    target_width: float,
    z: int,
) -> str:
    if not uri:
        return ""

    return centered_image_html(
        uri=uri,
        center_x=center_x,
        top_y=top_y,
        width=target_width,
        z=z,
    )


def ccu_blower_html() -> str:
    if not (
        CENTRAL_BLOWER_URI
        and CENTRAL_BLOWER_SVG_TEXT
    ):
        return ""

    _, _, vb_w, _ = svg_intrinsic_box(
        CENTRAL_BLOWER_SVG_TEXT,
        default=(
            0,
            0,
            165,
            100,
        ),
    )

    if vb_w <= 0:
        return ""

    scale = (
        BLOWER_TARGET_WIDTH
        / vb_w
    )

    diverter_left_x = (
        DIVERTER_CENTER_X
        - DIVERTER_TARGET_WIDTH / 2
    )

    # Qt V22에서 negative X scale을 사용했기 때문에
    # setPos X가 visible right edge에 해당합니다.
    #
    # v11: 바이패스의 디버터 접속 중심 Y는
    # DIVERTER_LEFT_Y와 동일하게 맞춥니다.
    visible_left_x = (
        diverter_left_x
        + BLOWER_VISUAL_OFFSET_X
        - BLOWER_TARGET_WIDTH
    )

    top_y = (
        BLOWER_VISUAL_LEFT_Y
        + BLOWER_VISUAL_OFFSET_Y
        - BLOWER_PIPE_CENTER_Y_LOCAL
        * scale
    )

    return image_html(
        uri=CENTRAL_BLOWER_URI,
        x=visible_left_x,
        y=top_y,
        width=BLOWER_TARGET_WIDTH,
        height=None,
        z=20,
        extra_style=(
            "transform:scaleX(-1);"
            "transform-origin:center center;"
        ),
    )


def ccu_pipe_svg_html() -> str:
    top_path = (
        f"M 230 {DIVERTER_RIGHT_TOP_Y} "
        f"L 490 {DIVERTER_RIGHT_TOP_Y} "
        f"C 510 {DIVERTER_RIGHT_TOP_Y}, "
        f"520 {DIVERTER_RIGHT_TOP_Y - 10}, "
        f"520 {DIVERTER_RIGHT_TOP_Y - 28} "
        f"L 520 {CENTRAL_TOP_PIPE_FLAT_SEGMENT_START_Y}"
    )

    middle_path = (
        f"M 230 {DIVERTER_RIGHT_MIDDLE_Y} "
        f"L 645 {DIVERTER_RIGHT_MIDDLE_Y} "
        f"C 665 {DIVERTER_RIGHT_MIDDLE_Y}, "
        f"675 {DIVERTER_RIGHT_MIDDLE_Y + 14}, "
        f"675 {DIVERTER_RIGHT_MIDDLE_Y + 39} "
        f"L 675 465"
    )

    bottom_path = (
        f"M 230 {DIVERTER_RIGHT_BOTTOM_Y} "
        f"L 238 {DIVERTER_RIGHT_BOTTOM_Y} "
        f"C 250 {DIVERTER_RIGHT_BOTTOM_Y}, "
        f"255 {DIVERTER_RIGHT_BOTTOM_Y + 14}, "
        f"255 {DIVERTER_RIGHT_BOTTOM_Y + 34} "
        f"L 255 465"
    )

    def round_double(
        d: str,
    ) -> str:
        return f"""
            <path
                d="{d}"
                fill="none"
                stroke="{PIPE_OUTLINE}"
                stroke-width="{CENTRAL_PIPE_OUTER_WIDTH}"
                stroke-linecap="round"
                stroke-linejoin="round"
            />
            <path
                d="{d}"
                fill="none"
                stroke="{PIPE_FILL}"
                stroke-width="{CENTRAL_PIPE_INNER_WIDTH}"
                stroke-linecap="round"
                stroke-linejoin="round"
            />
        """

    flat_d = (
        f"M 520 "
        f"{CENTRAL_TOP_PIPE_FLAT_SEGMENT_START_Y} "
        f"L 520 "
        f"{CENTRAL_TOP_PIPE_END_Y}"
    )

    pipe_svg = f"""
        <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 {STAGE_WIDTH} {STAGE_HEIGHT}"
            width="{STAGE_WIDTH}"
            height="{STAGE_HEIGHT}"
        >
            {round_double(top_path)}
            {round_double(middle_path)}
            {round_double(bottom_path)}

            <path
                d="{flat_d}"
                fill="none"
                stroke="{PIPE_OUTLINE}"
                stroke-width="{CENTRAL_PIPE_OUTER_WIDTH}"
                stroke-linecap="butt"
            />
            <path
                d="{flat_d}"
                fill="none"
                stroke="{PIPE_FILL}"
                stroke-width="{CENTRAL_PIPE_INNER_WIDTH}"
                stroke-linecap="butt"
            />
        </svg>
    """

    return image_html(
        uri=svg_string_data_uri(
            pipe_svg
        ),
        x=0,
        y=0,
        width=STAGE_WIDTH,
        height=STAGE_HEIGHT,
        z=5,
        extra_style=(
            "pointer-events:none;"
        ),
    )


def ccu_level_lines_html() -> str:
    lines = []

    for y in CENTRAL_LEVEL_LINES:
        lines.append(
            f"""
            <div
                style="
                    position:absolute;
                    left:{px(20)};
                    top:{py(y)};
                    width:{pw(960)};
                    border-top:
                        0.10cqw
                        dashed
                        #464646;
                    z-index:1;
                "
            ></div>
            """
        )

    return "".join(
        lines
    )


# ============================================================
# 메인 화면
# ============================================================

def show_main_menu():
    html = f"""
    {common_stage_css()}

    <div class="web-stage-wrap">

        <div class="web-stage">

            {logo_html(
                AEROCOM_URI,
                AEROCOM_LOGO_X,
                AEROCOM_LOGO_Y,
                AEROCOM_LOGO_TARGET_WIDTH,
            )}

            {logo_html(
                PAZKOREA_URI,
                PAZKOREA_LOGO_X,
                PAZKOREA_LOGO_Y,
                PAZKOREA_LOGO_TARGET_WIDTH,
            )}

            <a
                class="menu-button"
                href="?view=ptp"

                style="
                    left:{px(MAIN_MENU_BUTTON_X)};
                    top:{py(MAIN_MENU_POINT_Y)};

                    width:{pw(MAIN_MENU_BUTTON_WIDTH)};
                    height:{ph(MAIN_MENU_BUTTON_HEIGHT)};

                    font-size:
                        {MAIN_MENU_FONT_SIZE / 10:.3f}cqw;
                "
            >
                Point To Point System
            </a>

            <a
                class="menu-button"
                href="?view=central"

                style="
                    left:{px(MAIN_MENU_BUTTON_X)};
                    top:{py(MAIN_MENU_CENTRAL_Y)};

                    width:{pw(MAIN_MENU_BUTTON_WIDTH)};
                    height:{ph(MAIN_MENU_BUTTON_HEIGHT)};

                    font-size:
                        {MAIN_MENU_FONT_SIZE / 10:.3f}cqw;
                "
            >
                Central Control Unit System
            </a>

        </div>

    </div>
    """

    st.html(
        html
    )


# ============================================================
# Point To Point
# ============================================================

def show_point_to_point():
    # --------------------------------------------------------
    # Main button
    #
    # PTP animation itself is inside components.html() iframe.
    # iframe 내부에서 top.location을 변경하면 브라우저/Streamlit
    # 환경에 따라 차단될 수 있으므로 Main은 Streamlit 본체 버튼을
    # 화면 위에 overlay하여 처리합니다.
    # --------------------------------------------------------
    st.html(
        """
        <style>
            div[data-testid="stButton"] {
                position: fixed !important;

                /*
                stage width =
                min(100vw, 100vh * 1000/700)

                아래 값도 동일한 비율로 반응형 확대/축소됩니다.
                */
                right: calc(
                    max(0px, 50vw - 71.428571vh)
                    + min(2.5vw, 3.571429vh)
                ) !important;

                top: min(2vw, 2.857143vh) !important;

                width: min(6.5vw, 9.285714vh) !important;
                height: min(2.7vw, 3.857143vh) !important;

                margin: 0 !important;
                padding: 0 !important;

                z-index: 99999 !important;
            }

            div[data-testid="stButton"] button {
                width: 100% !important;
                height: 100% !important;
                min-height: 0 !important;

                margin: 0 !important;
                padding: 0 !important;

                border: 1px solid #999999 !important;
                border-radius: 4px !important;

                background: #eeeeee !important;
                color: #111111 !important;

                font-size: min(1.2vw, 1.714286vh) !important;
                font-weight: 600 !important;
                line-height: 1 !important;
            }

            div[data-testid="stButton"] button:hover {
                background: #e4e4e4 !important;
            }
        </style>
        """
    )

    if st.button(
        "Main",
        key="ptp_main_native",
    ):
        st.query_params["view"] = "main"
        st.rerun()

    (
        blower_html,
        blower_port_x,
        blower_port_y,
    ) = ptp_blower_html()

    pipe_html = (
        ptp_pipe_image_html(
            blower_port_x,
            blower_port_y,
        )
    )

    # --------------------------------------------------------
    # Slide Station geometry
    # --------------------------------------------------------
    station_vb_w, station_vb_h = svg_viewbox_size(
        SLIDE_STATION_SVG_TEXT,
        default=(
            177.0,
            319.57,
        ),
    )

    station_scale = (
        PTP_SLIDE_STATION_TARGET_HEIGHT
        / station_vb_h
    )

    station_width = (
        station_vb_w
        * station_scale
    )

    station1_left = (
        PTP_PIPE_LEFT_X
        - station_width
        * PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO
        + PTP_STATION1_OFFSET_X
    )

    station1_top = (
        PTP_STATION1_Y
        - PTP_SLIDE_STATION_TARGET_HEIGHT / 2
        + PTP_STATION1_OFFSET_Y
    )

    station2_left = (
        PTP_PIPE_RIGHT_X
        - station_width
        * PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO
        + PTP_STATION2_OFFSET_X
    )

    station2_top = (
        PTP_STATION2_Y
        - PTP_SLIDE_STATION_TARGET_HEIGHT / 2
        + PTP_STATION2_OFFSET_Y
    )

    station1_html = image_html(
        uri=SLIDE_STATION_URI,
        x=station1_left,
        y=station1_top,
        width=station_width,
        height=PTP_SLIDE_STATION_TARGET_HEIGHT,
        z=30,
        extra_style=(
            f"transform:scaleX({PTP_SLIDE_STATION_WIDTH_SCALE});"
            f"transform-origin:"
            f"{PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO * 100}% center;"
        ),
    ).replace(
        "<img",
        '<img id="ptp-station-1"',
        1,
    )

    station2_html = image_html(
        uri=SLIDE_STATION_URI,
        x=station2_left,
        y=station2_top,
        width=station_width,
        height=PTP_SLIDE_STATION_TARGET_HEIGHT,
        z=30,
        extra_style=(
            f"transform:scaleX({PTP_SLIDE_STATION_WIDTH_SCALE});"
            f"transform-origin:"
            f"{PTP_SLIDE_STATION_PIPE_ANCHOR_X_RATIO * 100}% center;"
        ),
    ).replace(
        "<img",
        '<img id="ptp-station-2"',
        1,
    )

    # --------------------------------------------------------
    # Carrier geometry
    # --------------------------------------------------------
    carrier_vb_w, carrier_vb_h = svg_viewbox_size(
        CARRIER_SVG_TEXT,
        default=(
            18.0,
            35.0,
        ),
    )

    carrier_height = (
        PTP_CARRIER_BASE_HEIGHT
        * PTP_CARRIER_SCALE
    )

    carrier_width = (
        carrier_height
        * carrier_vb_w
        / carrier_vb_h
    )

    # No.1 -> No.2 이동용 hidden SVG path
    route_d = (
        f"M {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_STATION1_Y:.3f} "

        f"L {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 28:.3f} "

        f"C {PTP_PIPE_LEFT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 12:.3f}, "

        f"{PTP_PIPE_LEFT_X + 12:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f}, "

        f"{PTP_PIPE_LEFT_X + 28:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f} "

        f"L {PTP_PIPE_RIGHT_X - 28:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f} "

        f"C {PTP_PIPE_RIGHT_X - 12:.3f} "
        f"{PTP_PIPE_TOP_Y:.3f}, "

        f"{PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 12:.3f}, "

        f"{PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_PIPE_TOP_Y + 28:.3f} "

        f"L {PTP_PIPE_RIGHT_X:.3f} "
        f"{PTP_STATION2_Y:.3f}"
    )

    html = f"""
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">

        {common_stage_css()}

        <style>
            html,
            body {{
                margin: 0;
                padding: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: #ffffff;
            }}

            .ptp-send {{
                cursor: pointer;
                padding: 0;
                font-family:
                    Arial,
                    "Malgun Gothic",
                    sans-serif;
            }}

            .ptp-send:disabled {{
                cursor: default;
                opacity: 0.65;
            }}

            #ptp-carrier {{
                position: absolute;
                display: none;
                z-index: 25;
                transform-origin: center center;
                pointer-events: none;
            }}

            #ptp-motion-svg {{
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                opacity: 0;
                pointer-events: none;
                z-index: -1;
            }}
        </style>
    </head>

    <body>
        <div class="web-stage-wrap">
            <div class="web-stage" id="ptp-stage">

                {logo_html(
                    AEROCOM_URI,
                    AEROCOM_LOGO_X,
                    AEROCOM_LOGO_Y,
                    AEROCOM_LOGO_TARGET_WIDTH,
                )}

                {logo_html(
                    PAZKOREA_URI,
                    PAZKOREA_LOGO_X,
                    PAZKOREA_LOGO_Y,
                    PAZKOREA_LOGO_TARGET_WIDTH,
                )}

                {pipe_html}
                {blower_html}

                {station1_html}
                {station2_html}

                <img
                    id="ptp-carrier"
                    src="{CARRIER_URI}"
                    draggable="false"
                    style="
                        width:{pw(carrier_width)};
                        height:{ph(carrier_height)};
                    "
                />

                <svg
                    id="ptp-motion-svg"
                    viewBox="
                        0 0
                        {STAGE_WIDTH}
                        {STAGE_HEIGHT}
                    "
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        id="ptp-route-1to2"
                        d="{route_d}"
                        fill="none"
                        stroke="none"
                    />
                </svg>

                <div
                    class="ptp-station-label"
                    style="
                        left:{
                            px(
                                PTP_PIPE_LEFT_X
                                + PTP_STATION_LABEL_OFFSET_X
                            )
                        };

                        top:{
                            py(
                                PTP_STATION1_Y
                                + PTP_STATION_LABEL_OFFSET_Y
                            )
                        };
                    "
                >
                    Station No.1
                </div>

                <button
                    id="ptp-send-1"
                    class="ptp-send"
                    type="button"
                    style="
                        left:{
                            px(
                                PTP_PIPE_LEFT_X
                                + PTP_STATION_LABEL_OFFSET_X
                            )
                        };

                        top:{
                            py(
                                PTP_STATION1_Y
                                + PTP_SEND_OFFSET_Y
                            )
                        };

                        width:{
                            pw(
                                PTP_SEND_BUTTON_WIDTH
                            )
                        };

                        height:{
                            ph(
                                PTP_SEND_BUTTON_HEIGHT
                            )
                        };
                    "
                >
                    Send
                </button>

                <div
                    class="ptp-station-label"
                    style="
                        left:{
                            px(
                                PTP_PIPE_RIGHT_X
                                + PTP_STATION_LABEL_OFFSET_X
                            )
                        };

                        top:{
                            py(
                                PTP_STATION2_Y
                                + PTP_STATION_LABEL_OFFSET_Y
                            )
                        };
                    "
                >
                    Station No.2
                </div>

                <button
                    id="ptp-send-2"
                    class="ptp-send"
                    type="button"
                    style="
                        left:{
                            px(
                                PTP_PIPE_RIGHT_X
                                + PTP_STATION_LABEL_OFFSET_X
                            )
                        };

                        top:{
                            py(
                                PTP_STATION2_Y
                                + PTP_SEND_OFFSET_Y
                            )
                        };

                        width:{
                            pw(
                                PTP_SEND_BUTTON_WIDTH
                            )
                        };

                        height:{
                            ph(
                                PTP_SEND_BUTTON_HEIGHT
                            )
                        };
                    "
                >
                    Send
                </button>

            </div>
        </div>

        <script>
        (() => {{
            const STAGE_W = {STAGE_WIDTH};
            const STAGE_H = {STAGE_HEIGHT};

            const PIPE_LEFT_X = {PTP_PIPE_LEFT_X};
            const PIPE_RIGHT_X = {PTP_PIPE_RIGHT_X};

            const STATION1_Y = {PTP_STATION1_Y};
            const STATION2_Y = {PTP_STATION2_Y};

            const STATION1_BASE_TOP = {station1_top:.6f};
            const STATION2_BASE_TOP = {station2_top:.6f};

            const LIFT_DISTANCE = {PTP_SLIDE_STATION_LIFT_DISTANCE};

            const CARRIER_W = {carrier_width:.6f};
            const CARRIER_H = {carrier_height:.6f};

            const SOURCE1_READY_X =
                PIPE_LEFT_X
                + {PTP_CARRIER_SOURCE_READY_OFFSET_X};

            const SOURCE2_READY_X =
                PIPE_RIGHT_X
                + {PTP_CARRIER_SOURCE_READY_OFFSET_X};

            const DEST2_OUTPUT_X =
                PIPE_RIGHT_X
                + {PTP_CARRIER_DEST_OUTPUT_OFFSET_X};

            const DEST1_OUTPUT_X =
                PIPE_LEFT_X
                + {PTP_CARRIER_DEST_OUTPUT_OFFSET_X};

            const MOVE_MS =
                {PTP_SLIDE_STATION_MOVE_SECONDS * 1000:.3f};

            const SOURCE_READY_HOLD_MS =
                {PTP_SOURCE_READY_HOLD_SECONDS * 1000:.3f};

            const SOURCE_UP_HOLD_MS =
                {PTP_SOURCE_STATION_UP_HOLD_SECONDS * 1000:.3f};

            const SOURCE_INSERT_MS =
                {PTP_SOURCE_INSERT_SECONDS * 1000:.3f};

            const SOURCE_DOWN_HOLD_MS =
                {PTP_SOURCE_STATION_DOWN_HOLD_SECONDS * 1000:.3f};

            const TRAVEL_MS =
                {PTP_1_TO_2_TRAVEL_SECONDS * 1000:.3f};

            const DEST_HIDDEN_HOLD_MS =
                {PTP_DEST_HIDDEN_HOLD_SECONDS * 1000:.3f};

            const DEST_UP_HOLD_MS =
                {PTP_DEST_STATION_UP_HOLD_SECONDS * 1000:.3f};

            const DEST_OUTPUT_MS =
                {PTP_DEST_OUTPUT_SECONDS * 1000:.3f};

            const DEST_DOWN_HOLD_MS =
                {PTP_DEST_STATION_DOWN_HOLD_SECONDS * 1000:.3f};

            const FINAL_HOLD_MS =
                {PTP_FINAL_CARRIER_HOLD_SECONDS * 1000:.3f};

            const station1 =
                document.getElementById(
                    "ptp-station-1"
                );

            const station2 =
                document.getElementById(
                    "ptp-station-2"
                );

            const carrier =
                document.getElementById(
                    "ptp-carrier"
                );

            const route =
                document.getElementById(
                    "ptp-route-1to2"
                );

            const send1 =
                document.getElementById(
                    "ptp-send-1"
                );

            const send2 =
                document.getElementById(
                    "ptp-send-2"
                );

            let running = false;


            function xPct(x) {{
                return (
                    x
                    / STAGE_W
                    * 100
                ) + "%";
            }}


            function yPct(y) {{
                return (
                    y
                    / STAGE_H
                    * 100
                ) + "%";
            }}


            function smoothstep(t) {{
                t = Math.max(
                    0,
                    Math.min(
                        1,
                        t
                    )
                );

                return (
                    t
                    * t
                    * (
                        3
                        - 2 * t
                    )
                );
            }}


            function sleep(ms) {{
                return new Promise(
                    resolve =>
                        setTimeout(
                            resolve,
                            ms
                        )
                );
            }}


            function setCarrier(
                x,
                y,
                rotationDeg = 0
            ) {{
                carrier.style.left =
                    xPct(
                        x
                        - CARRIER_W / 2
                    );

                carrier.style.top =
                    yPct(
                        y
                        - CARRIER_H / 2
                    );

                carrier.style.transform =
                    `rotate(${{rotationDeg}}deg)`;

                carrier.style.display =
                    "block";
            }}


            function setStationTop(
                station,
                designTop
            ) {{
                station.style.top =
                    yPct(
                        designTop
                    );
            }}


            function animate(
                duration,
                update
            ) {{
                return new Promise(
                    resolve => {{
                        const start =
                            performance.now();

                        function frame(now) {{
                            const raw =
                                duration <= 0
                                ? 1
                                : (
                                    now
                                    - start
                                )
                                / duration;

                            const t =
                                Math.max(
                                    0,
                                    Math.min(
                                        1,
                                        raw
                                    )
                                );

                            update(
                                smoothstep(
                                    t
                                ),
                                t
                            );

                            if (t < 1) {{
                                requestAnimationFrame(
                                    frame
                                );
                            }}
                            else {{
                                resolve();
                            }}
                        }}

                        requestAnimationFrame(
                            frame
                        );
                    }}
                );
            }}


            async function moveStation(
                station,
                baseTop,
                fromLift,
                toLift
            ) {{
                await animate(
                    MOVE_MS,
                    eased => {{
                        const lift =
                            fromLift
                            + (
                                toLift
                                - fromLift
                            )
                            * eased;

                        setStationTop(
                            station,
                            baseTop
                            - lift
                        );
                    }}
                );
            }}


            async function insertCarrier() {{
                await animate(
                    SOURCE_INSERT_MS,
                    eased => {{
                        const x =
                            SOURCE1_READY_X
                            + (
                                PIPE_LEFT_X
                                - SOURCE1_READY_X
                            )
                            * eased;

                        setCarrier(
                            x,
                            STATION1_Y,
                            0
                        );
                    }}
                );
            }}


            async function travelCarrier() {{
                const total =
                    route.getTotalLength();

                await animate(
                    TRAVEL_MS,
                    (_eased, rawT) => {{
                        /*
                        배관 이송 자체는 일정 속도에 가깝게 보이도록
                        rawT를 사용합니다.
                        */
                        const distance =
                            total
                            * rawT;

                        const p =
                            route.getPointAtLength(
                                distance
                            );

                        const p2 =
                            route.getPointAtLength(
                                Math.min(
                                    total,
                                    distance + 1.5
                                )
                            );

                        const angle =
                            Math.atan2(
                                p2.y - p.y,
                                p2.x - p.x
                            )
                            * 180
                            / Math.PI
                            - 90;

                        setCarrier(
                            p.x,
                            p.y,
                            angle
                        );
                    }}
                );

                setCarrier(
                    PIPE_RIGHT_X,
                    STATION2_Y,
                    0
                );
            }}


            async function outputCarrier() {{
                await animate(
                    DEST_OUTPUT_MS,
                    eased => {{
                        const x =
                            PIPE_RIGHT_X
                            + (
                                DEST2_OUTPUT_X
                                - PIPE_RIGHT_X
                            )
                            * eased;

                        setCarrier(
                            x,
                            STATION2_Y,
                            0
                        );
                    }}
                );
            }}


            // ------------------------------------------------
            // No.2 -> No.1
            // ------------------------------------------------

            async function insertCarrier2To1() {{
                await animate(
                    SOURCE_INSERT_MS,
                    eased => {{
                        const x =
                            SOURCE2_READY_X
                            + (
                                PIPE_RIGHT_X
                                - SOURCE2_READY_X
                            )
                            * eased;

                        setCarrier(
                            x,
                            STATION2_Y,
                            0
                        );
                    }}
                );
            }}


            async function travelCarrier2To1() {{
                const total =
                    route.getTotalLength();

                await animate(
                    TRAVEL_MS,
                    (_eased, rawT) => {{
                        /*
                        동일한 SVG route를 끝 -> 시작 방향으로 읽어
                        No.2 -> No.1을 구현합니다.
                        */
                        const distance =
                            total
                            * (
                                1
                                - rawT
                            );

                        const p =
                            route.getPointAtLength(
                                distance
                            );

                        const p2 =
                            route.getPointAtLength(
                                Math.max(
                                    0,
                                    distance - 1.5
                                )
                            );

                        const angle =
                            Math.atan2(
                                p2.y - p.y,
                                p2.x - p.x
                            )
                            * 180
                            / Math.PI
                            - 90;

                        setCarrier(
                            p.x,
                            p.y,
                            angle
                        );
                    }}
                );

                setCarrier(
                    PIPE_LEFT_X,
                    STATION1_Y,
                    0
                );
            }}


            async function outputCarrier2To1() {{
                await animate(
                    DEST_OUTPUT_MS,
                    eased => {{
                        const x =
                            PIPE_LEFT_X
                            + (
                                DEST1_OUTPUT_X
                                - PIPE_LEFT_X
                            )
                            * eased;

                        setCarrier(
                            x,
                            STATION1_Y,
                            0
                        );
                    }}
                );
            }}


            function resetScene() {{
                setStationTop(
                    station1,
                    STATION1_BASE_TOP
                );

                setStationTop(
                    station2,
                    STATION2_BASE_TOP
                );

                carrier.style.display =
                    "none";

                carrier.style.transform =
                    "rotate(0deg)";
            }}


            async function run1To2() {{
                if (running) {{
                    return;
                }}

                running = true;

                send1.disabled = true;
                send2.disabled = true;

                resetScene();

                try {{
                    // 1. No.1 오른쪽에 carrier 등장
                    setCarrier(
                        SOURCE1_READY_X,
                        STATION1_Y,
                        0
                    );

                    await sleep(
                        SOURCE_READY_HOLD_MS
                    );

                    // 2. No.1 slide station 상승
                    await moveStation(
                        station1,
                        STATION1_BASE_TOP,
                        0,
                        LIFT_DISTANCE
                    );

                    await sleep(
                        SOURCE_UP_HOLD_MS
                    );

                    // 3. carrier 투입
                    await insertCarrier();

                    // 4. station 원위치
                    await moveStation(
                        station1,
                        STATION1_BASE_TOP,
                        LIFT_DISTANCE,
                        0
                    );

                    await sleep(
                        SOURCE_DOWN_HOLD_MS
                    );

                    // 5. No.1 -> No.2 배관 이송
                    await travelCarrier();

                    // 6. No.2 내부에서 잠시 대기
                    await sleep(
                        DEST_HIDDEN_HOLD_MS
                    );

                    // 7. No.2 slide station 상승
                    await moveStation(
                        station2,
                        STATION2_BASE_TOP,
                        0,
                        LIFT_DISTANCE
                    );

                    await sleep(
                        DEST_UP_HOLD_MS
                    );

                    // 8. 오른쪽 배출
                    await outputCarrier();

                    // 9. No.2 station 원위치
                    await moveStation(
                        station2,
                        STATION2_BASE_TOP,
                        LIFT_DISTANCE,
                        0
                    );

                    await sleep(
                        DEST_DOWN_HOLD_MS
                    );

                    // 10. 최종 위치 1초 유지
                    await sleep(
                        FINAL_HOLD_MS
                    );

                    carrier.style.display =
                        "none";
                }}
                finally {{
                    running = false;

                    send1.disabled = false;
                    send2.disabled = false;
                }}
            }}


            async function run2To1() {{
                if (running) {{
                    return;
                }}

                running = true;

                send1.disabled = true;
                send2.disabled = true;

                resetScene();

                try {{
                    // 1. No.2 오른쪽에 carrier 등장
                    setCarrier(
                        SOURCE2_READY_X,
                        STATION2_Y,
                        0
                    );

                    await sleep(
                        SOURCE_READY_HOLD_MS
                    );

                    // 2. No.2 slide station 상승
                    await moveStation(
                        station2,
                        STATION2_BASE_TOP,
                        0,
                        LIFT_DISTANCE
                    );

                    await sleep(
                        SOURCE_UP_HOLD_MS
                    );

                    // 3. carrier를 오른쪽 -> 왼쪽으로 투입
                    await insertCarrier2To1();

                    // 4. No.2 station 원위치
                    await moveStation(
                        station2,
                        STATION2_BASE_TOP,
                        LIFT_DISTANCE,
                        0
                    );

                    await sleep(
                        SOURCE_DOWN_HOLD_MS
                    );

                    // 5. No.2 -> No.1 배관 이송
                    await travelCarrier2To1();

                    // 6. No.1 내부에서 잠시 대기
                    await sleep(
                        DEST_HIDDEN_HOLD_MS
                    );

                    // 7. No.1 slide station 상승
                    await moveStation(
                        station1,
                        STATION1_BASE_TOP,
                        0,
                        LIFT_DISTANCE
                    );

                    await sleep(
                        DEST_UP_HOLD_MS
                    );

                    // 8. No.1 오른쪽으로 배출
                    await outputCarrier2To1();

                    // 9. No.1 station 원위치
                    await moveStation(
                        station1,
                        STATION1_BASE_TOP,
                        LIFT_DISTANCE,
                        0
                    );

                    await sleep(
                        DEST_DOWN_HOLD_MS
                    );

                    // 10. 최종 위치 1초 유지
                    await sleep(
                        FINAL_HOLD_MS
                    );

                    carrier.style.display =
                        "none";
                }}
                finally {{
                    running = false;

                    send1.disabled = false;
                    send2.disabled = false;
                }}
            }}


            send1.addEventListener(
                "click",
                run1To2
            );

            send2.addEventListener(
                "click",
                run2To1
            );

            resetScene();
        }})();
        </script>
    </body>
    </html>
    """

    components.html(
        html,
        height=700,
        scrolling=False,
    )


# ============================================================
# Central placeholder
# ============================================================

def show_central_placeholder():
    # --------------------------------------------------------
    # CCU animation lives inside a component iframe.
    # Main stays in the Streamlit parent document.
    # --------------------------------------------------------
    st.html(
        """
        <style>
            div[data-testid="stButton"] {
                position: fixed !important;
                right: calc(
                    max(0px, 50vw - 71.428571vh)
                    + min(2.5vw, 3.571429vh)
                ) !important;
                top: min(2vw, 2.857143vh) !important;
                width: min(6.5vw, 9.285714vh) !important;
                height: min(2.7vw, 3.857143vh) !important;
                margin: 0 !important;
                padding: 0 !important;
                z-index: 99999 !important;
            }

            div[data-testid="stButton"] button {
                width: 100% !important;
                height: 100% !important;
                min-height: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
                border: 1px solid #999999 !important;
                border-radius: 4px !important;
                background: #eeeeee !important;
                color: #111111 !important;
                font-size: min(1.2vw, 1.714286vh) !important;
                font-weight: 600 !important;
                line-height: 1 !important;
            }
        </style>
        """
    )

    if st.button(
        "Main",
        key="ccu_main_native",
    ):
        st.query_params["view"] = "main"
        st.rerun()

    # ========================================================
    # Static assets
    # ========================================================
    pipe_html = ccu_pipe_svg_html()
    blower_html = ccu_blower_html()

    diverter_html = centered_middle_image_html(
        uri=DIVERTER_URI,
        center_x=DIVERTER_CENTER_X,
        center_y=DIVERTER_CENTER_Y,
        width=DIVERTER_TARGET_WIDTH,
        z=30,
        mirror_horizontal=True,
    )

    if diverter_html:
        diverter_html = diverter_html.replace(
            "<img",
            '<img id="ccu-diverter"',
            1,
        )

    def add_image_ids(
        html_text: str,
        ids,
    ) -> str:
        parts = html_text.split("<img")
        if len(parts) <= 1:
            return html_text

        result = parts[0]
        for index, part in enumerate(parts[1:]):
            if index < len(ids):
                result += f'<img id="{ids[index]}"' + part
            else:
                result += "<img" + part
        return result

    titan1_html = ccu_titan_station_html(
        center_x=STATION1_CENTER_X,
        top_y=STATION1_TOP_Y,
        target_height=STATION1_TARGET_HEIGHT,
        inner_offset_x=TITAN_TOP_INNER_OFFSET_X,
        inner_offset_y=TITAN_TOP_INNER_OFFSET_Y,
    )
    titan1_html = add_image_ids(
        titan1_html,
        (
            "ccu-titan1-inner",
            "ccu-titan1-door",
            "ccu-titan1-front",
        ),
    )

    titan2_html = ccu_titan_station_html(
        center_x=STATION2_CENTER_X,
        top_y=STATION2_TOP_Y,
        target_height=STATION2_TARGET_HEIGHT,
        inner_offset_x=TITAN_MIDDLE_INNER_OFFSET_X,
        inner_offset_y=TITAN_MIDDLE_INNER_OFFSET_Y,
    )
    titan2_html = add_image_ids(
        titan2_html,
        (
            "ccu-titan2-inner",
            "ccu-titan2-door",
            "ccu-titan2-front",
        ),
    )

    ews3_html = ccu_ews_station_html(
        center_x=STATION3_CENTER_X,
        top_y=STATION3_TOP_Y,
        target_height=STATION3_TARGET_HEIGHT,
        inlet_offset_x=EWS3_INLET_OFFSET_X,
        inlet_offset_y=EWS3_INLET_OFFSET_Y,
    )

    ews4_html = ccu_ews_station_html(
        center_x=STATION4_CENTER_X,
        top_y=STATION4_TOP_Y,
        target_height=STATION4_TARGET_HEIGHT,
        inlet_offset_x=EWS4_INLET_OFFSET_X,
        inlet_offset_y=EWS4_INLET_OFFSET_Y,
    )

    basket3_back_html = ccu_basket_html(
        uri=BASKET_BACK_URI,
        center_x=(STATION3_CENTER_X + BASKET3_BACK_OFFSET_X),
        top_y=(BASKET_BACK_TOP_Y + BASKET3_BACK_OFFSET_Y),
        target_width=BASKET_BACK_TARGET_WIDTH,
        z=55,
    )
    basket4_back_html = ccu_basket_html(
        uri=BASKET_BACK_URI,
        center_x=(STATION4_CENTER_X + BASKET4_BACK_OFFSET_X),
        top_y=(BASKET_BACK_TOP_Y + BASKET4_BACK_OFFSET_Y),
        target_width=BASKET_BACK_TARGET_WIDTH,
        z=55,
    )
    basket3_front_html = ccu_basket_html(
        uri=BASKET_FRONT_URI,
        center_x=(STATION3_CENTER_X + BASKET3_FRONT_OFFSET_X),
        top_y=(BASKET_FRONT_TOP_Y + BASKET3_FRONT_OFFSET_Y),
        target_width=BASKET_FRONT_TARGET_WIDTH,
        z=70,
    )
    basket4_front_html = ccu_basket_html(
        uri=BASKET_FRONT_URI,
        center_x=(STATION4_CENTER_X + BASKET4_FRONT_OFFSET_X),
        top_y=(BASKET_FRONT_TOP_Y + BASKET4_FRONT_OFFSET_Y),
        target_width=BASKET_FRONT_TARGET_WIDTH,
        z=70,
    )

    level_lines_html = ccu_level_lines_html()

    # ========================================================
    # Labels / Send buttons
    # ========================================================
    station_ui = {
        1: {
            "label": (STATION1_LABEL_X, STATION1_LABEL_Y),
            "send": (STATION1_SEND_X, STATION1_SEND_Y),
        },
        2: {
            "label": (STATION2_LABEL_X, STATION2_LABEL_Y),
            "send": (STATION2_SEND_X, STATION2_SEND_Y),
        },
        3: {
            "label": (STATION3_LABEL_X, STATION3_LABEL_Y),
            "send": (STATION3_SEND_X, STATION3_SEND_Y),
        },
        4: {
            "label": (STATION4_LABEL_X, STATION4_LABEL_Y),
            "send": (STATION4_SEND_X, STATION4_SEND_Y),
        },
    }

    label_html = ""
    send_html = ""
    dest_html = ""

    for station_no in range(1, 5):
        label_x, label_y = station_ui[station_no]["label"]
        send_x, send_y = station_ui[station_no]["send"]

        label_html += f"""
            <div
                class="ccu-station-label"
                style="left:{px(label_x)}; top:{py(label_y)};"
            >Station No.{station_no}</div>
        """

        send_html += f"""
            <button
                class="ccu-send"
                id="ccu-send-{station_no}"
                data-source="{station_no}"
                type="button"
                style="
                    left:{px(send_x)};
                    top:{py(send_y)};
                    width:{pw(SEND_BUTTON_WIDTH * CCU_SEND_BUTTON_SCALE)};
                    height:{ph(SEND_BUTTON_HEIGHT * CCU_SEND_BUTTON_SCALE)};
                "
            >Send</button>
        """

        destinations = [
            destination
            for destination in range(1, 5)
            if destination != station_no
        ]

        for dest_index, destination in enumerate(destinations):
            dest_x = (
                send_x
                + SEND_BUTTON_WIDTH * CCU_SEND_BUTTON_SCALE
                + CCU_DEST_BUTTON_GAP_X
            )
            dest_y = (
                send_y
                + dest_index
                * (
                    DEST_BUTTON_HEIGHT * CCU_SEND_BUTTON_SCALE
                    + CCU_DEST_BUTTON_GAP_Y
                )
            )

            dest_html += f"""
                <button
                    class="ccu-dest"
                    id="ccu-dest-{station_no}-{destination}"
                    data-source="{station_no}"
                    data-destination="{destination}"
                    type="button"
                    style="
                        left:{px(dest_x)};
                        top:{py(dest_y)};
                        width:{pw(DEST_BUTTON_WIDTH * CCU_SEND_BUTTON_SCALE)};
                        height:{ph(DEST_BUTTON_HEIGHT * CCU_SEND_BUTTON_SCALE)};
                    "
                >to No.{destination}</button>
            """

    # ========================================================
    # Carrier geometry
    # ========================================================
    _, _, titan_front_w, titan_front_h = svg_intrinsic_box(
        TITAN_STANDARD_SVG_TEXT,
        default=(0, 0, 37, 91.95),
    )
    titan_scale = (
        STATION1_TARGET_HEIGHT / titan_front_h
        if titan_front_h > 0
        else 1.0
    )

    _, _, carrier_intrinsic_w, carrier_intrinsic_h = svg_intrinsic_box(
        CARRIER_SVG_TEXT,
        default=(0, 0, 12, 30),
    )
    carrier_width = (
        carrier_intrinsic_w
        * titan_scale
        * CCU_CARRIER_SCALE_MULTIPLIER
    )
    carrier_height = (
        carrier_intrinsic_h
        * titan_scale
        * CCU_CARRIER_SCALE_MULTIPLIER
    )

    # ========================================================
    # Generic station configuration (desktop V22 mapping)
    # ========================================================
    def station_config(station_no: int):
        if station_no == 1:
            center_x = STATION1_CENTER_X
            top_y = STATION1_TOP_Y
        elif station_no == 2:
            center_x = STATION2_CENTER_X
            top_y = STATION2_TOP_Y
        elif station_no == 3:
            center_x = STATION3_CENTER_X
            top_y = STATION3_TOP_Y
        else:
            center_x = STATION4_CENTER_X
            top_y = STATION4_TOP_Y

        if station_no in (1, 2):
            dx = center_x - STATION1_CENTER_X
            dy = top_y - STATION1_TOP_Y
            return {
                "no": station_no,
                "type": "titan",
                "branch": "top",
                "center_x": center_x,
                "top_y": top_y,
                "entry_start": [CARRIER_ENTRY_START_X + dx, CARRIER_ENTRY_START_Y + dy],
                "entry_end": [CARRIER_ENTRY_END_X + dx, CARRIER_ENTRY_END_Y + dy],
                "pipe": [CARRIER_PIPE_START_X + dx, CARRIER_PIPE_START_Y + dy],
                "receive_body": [NO1_RECEIVE_BODY_X + dx, NO1_RECEIVE_BODY_HIDDEN_Y + dy],
                "receive_output_hidden": [NO1_RECEIVE_OUTPUT_X + dx, NO1_RECEIVE_OUTPUT_HIDDEN_Y + dy],
                "receive_output_emerge": [NO1_RECEIVE_OUTPUT_X + dx, NO1_RECEIVE_OUTPUT_EMERGE_Y + dy],
                "receive_basket_drop": [NO1_RECEIVE_BASKET_DROP_X + dx, NO1_RECEIVE_BASKET_DROP_Y + dy],
                "drop_rotation": (
                    NO1_RECEIVE_DROP_ROTATION_DEG
                    if station_no == 1
                    else NO2_RECEIVE_DROP_ROTATION_DEG
                ),
            }

        dx = center_x - STATION4_CENTER_X
        dy = top_y - STATION4_TOP_Y
        return {
            "no": station_no,
            "type": "ews",
            "branch": "middle" if station_no == 4 else "bottom",
            "center_x": center_x,
            "top_y": top_y,
            "send_entry_start": [EWS4_SEND_ENTRY_START_X + dx, EWS4_SEND_ENTRY_START_Y + dy],
            "send_load": [EWS4_SEND_LOAD_X + dx, EWS4_SEND_LOAD_Y + dy],
            "send_hidden": [EWS4_SEND_HIDDEN_X + dx, EWS4_SEND_HIDDEN_Y + dy],
            "send_hidden_pipe": [EWS4_SEND_HIDDEN_PIPE_X + dx, EWS4_SEND_HIDDEN_PIPE_Y + dy],
            "pipe": [EWS4_SEND_PIPE_EXIT_X + dx, EWS4_SEND_PIPE_EXIT_Y + dy],
            "receive_hidden_start": [EWS4_HIDDEN_START_X + dx, EWS4_HIDDEN_START_Y + dy],
            "receive_output": [EWS4_OUTPUT_X + dx, EWS4_OUTPUT_Y + dy],
            "receive_emerge": [EWS4_EMERGE_END_X + dx, EWS4_EMERGE_END_Y + dy],
            "receive_basket_drop": [EWS4_BASKET_DROP_X + dx, EWS4_BASKET_DROP_Y + dy],
            "drop_rotation": (
                EWS4_BASKET_DROP_ROTATION_DEG
                if station_no == 4
                else EWS3_BASKET_DROP_ROTATION_DEG
            ),
        }

    station_configs = {
        station_no: station_config(station_no)
        for station_no in range(1, 5)
    }
    station_configs_json = json.dumps(station_configs)

    # ========================================================
    # Generic pipe motion paths
    # ========================================================
    def station_to_bypass_path(station_no: int) -> str:
        cfg = station_configs[station_no]
        pipe_x, pipe_y = cfg["pipe"]
        branch = cfg["branch"]

        if branch == "top":
            return (
                f"M {pipe_x} {pipe_y} "
                f"L {CARRIER_VERTICAL_END_X} {CARRIER_VERTICAL_END_Y} "
                f"C {CARRIER_TOP_CURVE_C1_X} {CARRIER_TOP_CURVE_C1_Y}, "
                f"{CARRIER_TOP_CURVE_C2_X} {CARRIER_TOP_CURVE_C2_Y}, "
                f"{CARRIER_TOP_CURVE_END_X} {CARRIER_TOP_CURVE_END_Y} "
                f"L {CARRIER_DIVERTER_TOP_ENTRY_X} {CARRIER_DIVERTER_TOP_ENTRY_Y} "
                f"C {CARRIER_DIVERTER_EXIT_C1_X} {CARRIER_DIVERTER_EXIT_C1_Y}, "
                f"{CARRIER_DIVERTER_EXIT_C2_X} {CARRIER_DIVERTER_EXIT_C2_Y}, "
                f"{CARRIER_DIVERTER_LEFT_EXIT_X} {CARRIER_DIVERTER_LEFT_EXIT_Y} "
                f"L {BYPASS_STOP_X} {BYPASS_STOP_Y}"
            )

        if branch == "middle":
            return (
                f"M {pipe_x} {pipe_y} "
                f"L {CARRIER_NO4_CURVE_END_X} {CARRIER_NO4_CURVE_END_Y} "
                f"C {CARRIER_NO4_CURVE_C2_X} {CARRIER_NO4_CURVE_C2_Y}, "
                f"{CARRIER_NO4_CURVE_C1_X} {CARRIER_NO4_CURVE_C1_Y}, "
                f"{CARRIER_NO4_STRAIGHT_END_X} {CARRIER_NO4_STRAIGHT_END_Y} "
                f"L {BYPASS_STOP_X} {BYPASS_STOP_Y}"
            )

        # bottom = Station No.3
        bottom_curve_end_x = STATION3_CENTER_X
        bottom_curve_end_y = DIVERTER_RIGHT_BOTTOM_Y + 34
        bottom_curve_c2_x = STATION3_CENTER_X
        bottom_curve_c2_y = DIVERTER_RIGHT_BOTTOM_Y + 14
        bottom_curve_c1_x = 250
        bottom_straight_x = 238
        return (
            f"M {pipe_x} {pipe_y} "
            f"L {bottom_curve_end_x} {bottom_curve_end_y} "
            f"C {bottom_curve_c2_x} {bottom_curve_c2_y}, "
            f"{bottom_curve_c1_x} {DIVERTER_RIGHT_BOTTOM_Y}, "
            f"{bottom_straight_x} {DIVERTER_RIGHT_BOTTOM_Y} "
            f"L 230 {DIVERTER_RIGHT_BOTTOM_Y} "
            f"C 217 {DIVERTER_RIGHT_BOTTOM_Y}, "
            f"204 {DIVERTER_LEFT_Y}, "
            f"{CARRIER_DIVERTER_LEFT_EXIT_X} {CARRIER_DIVERTER_LEFT_EXIT_Y} "
            f"L {BYPASS_STOP_X} {BYPASS_STOP_Y}"
        )

    def bypass_to_station_path(station_no: int) -> str:
        cfg = station_configs[station_no]
        pipe_x, pipe_y = cfg["pipe"]
        branch = cfg["branch"]

        if branch == "top":
            return (
                f"M {BYPASS_STOP_X} {BYPASS_STOP_Y} "
                f"L {CARRIER_DIVERTER_LEFT_EXIT_X} {CARRIER_DIVERTER_LEFT_EXIT_Y} "
                f"C {CARRIER_DIVERTER_EXIT_C2_X} {CARRIER_DIVERTER_EXIT_C2_Y}, "
                f"{CARRIER_DIVERTER_EXIT_C1_X} {CARRIER_DIVERTER_EXIT_C1_Y}, "
                f"{CARRIER_DIVERTER_TOP_ENTRY_X} {CARRIER_DIVERTER_TOP_ENTRY_Y} "
                f"L {CARRIER_TOP_CURVE_END_X} {CARRIER_TOP_CURVE_END_Y} "
                f"C {CARRIER_TOP_CURVE_C2_X} {CARRIER_TOP_CURVE_C2_Y}, "
                f"{CARRIER_TOP_CURVE_C1_X} {CARRIER_TOP_CURVE_C1_Y}, "
                f"{CARRIER_VERTICAL_END_X} {CARRIER_VERTICAL_END_Y} "
                f"L {pipe_x} {pipe_y}"
            )

        if branch == "middle":
            return (
                f"M {BYPASS_STOP_X} {BYPASS_STOP_Y} "
                f"L {CARRIER_NO4_STRAIGHT_END_X} {CARRIER_NO4_STRAIGHT_END_Y} "
                f"C {CARRIER_NO4_CURVE_C1_X} {CARRIER_NO4_CURVE_C1_Y}, "
                f"{CARRIER_NO4_CURVE_C2_X} {CARRIER_NO4_CURVE_C2_Y}, "
                f"{CARRIER_NO4_CURVE_END_X} {CARRIER_NO4_CURVE_END_Y} "
                f"L {pipe_x} {pipe_y}"
            )

        bottom_curve_end_x = STATION3_CENTER_X
        bottom_curve_end_y = DIVERTER_RIGHT_BOTTOM_Y + 34
        bottom_curve_c2_x = STATION3_CENTER_X
        bottom_curve_c2_y = DIVERTER_RIGHT_BOTTOM_Y + 14
        bottom_curve_c1_x = 250
        bottom_straight_x = 238
        return (
            f"M {BYPASS_STOP_X} {BYPASS_STOP_Y} "
            f"L {CARRIER_DIVERTER_LEFT_EXIT_X} {CARRIER_DIVERTER_LEFT_EXIT_Y} "
            f"C 204 {DIVERTER_LEFT_Y}, "
            f"217 {DIVERTER_RIGHT_BOTTOM_Y}, "
            f"230 {DIVERTER_RIGHT_BOTTOM_Y} "
            f"L {bottom_straight_x} {DIVERTER_RIGHT_BOTTOM_Y} "
            f"C {bottom_curve_c1_x} {DIVERTER_RIGHT_BOTTOM_Y}, "
            f"{bottom_curve_c2_x} {bottom_curve_c2_y}, "
            f"{bottom_curve_end_x} {bottom_curve_end_y} "
            f"L {pipe_x} {pipe_y}"
        )

    source_paths = {
        station_no: station_to_bypass_path(station_no)
        for station_no in range(1, 5)
    }
    destination_paths = {
        station_no: bypass_to_station_path(station_no)
        for station_no in range(1, 5)
    }

    motion_paths_html = ""
    for station_no in range(1, 5):
        motion_paths_html += f"""
            <path
                id="ccu-src-path-{station_no}"
                d="{source_paths[station_no]}"
                fill="none"
                stroke="none"
            />
            <path
                id="ccu-dst-path-{station_no}"
                d="{destination_paths[station_no]}"
                fill="none"
                stroke="none"
            />
        """

    # ========================================================
    # TITAN door geometry for No.1 and No.2
    # ========================================================
    _, _, door_intrinsic_w, door_intrinsic_h = svg_intrinsic_box(
        TITAN_DOOR_SVG_TEXT,
        default=(0, 0, 4.2, 33.4),
    )

    titan_front_width = (
        titan_front_w
        * titan_scale
        * TITAN_WIDTH_SCALE
    )

    titan_door_configs = {}
    for station_no, center_x, top_y in (
        (1, STATION1_CENTER_X, STATION1_TOP_Y),
        (2, STATION2_CENTER_X, STATION2_TOP_Y),
    ):
        front_left = center_x - titan_front_width / 2
        titan_door_configs[station_no] = {
            "front_left": front_left,
            "top_y": top_y,
            "door_y": (
                top_y
                + TITAN_DOOR_Y_LOCAL * titan_scale
                + TITAN_DOOR_ADJUST_Y
            ),
            "door_height": (
                door_intrinsic_h
                * titan_scale
                * TITAN_DOOR_SCALE_Y
            ),
        }

    titan_door_configs_json = json.dumps(titan_door_configs)
    diverter_frames_json = json.dumps(DIVERTER_FRAME_URIS)

    # ========================================================
    # HTML / JavaScript
    # ========================================================
    html = f"""
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        {common_stage_css()}
        <style>
            html, body {{
                margin:0;
                padding:0;
                width:100%;
                height:100%;
                overflow:hidden;
                background:#ffffff;
            }}

            .ccu-content {{
                position:absolute;
                left:0;
                top:{py(CCU_CONTENT_OFFSET_Y)};
                width:100%;
                height:100%;
                z-index:1;
            }}

            .ccu-station-label {{
                position:absolute;
                color:{LABEL_RED};
                font-size:1.8cqw;
                font-weight:700;
                line-height:1;
                white-space:nowrap;
                z-index:100;
            }}

            .ccu-send,
            .ccu-dest {{
                position:absolute;
                display:flex;
                justify-content:center;
                align-items:center;
                padding:0;
                border:0.10cqw solid #aaaaaa;
                background:linear-gradient(#f4f4f4,#dddddd);
                color:#111111;
                font-family:Arial,"Malgun Gothic",sans-serif;
                font-size:1.7cqw;
                cursor:pointer;
                z-index:200;
            }}

            .ccu-send:disabled,
            .ccu-dest:disabled {{
                cursor:default;
                opacity:0.60;
            }}

            .ccu-dest {{
                display:none;
                z-index:210;
            }}

            #ccu-carrier {{
                position:absolute;
                display:none;
                width:{pw(carrier_width)};
                height:{ph(carrier_height)};
                transform-origin:center center;
                pointer-events:none;
                z-index:60;
            }}

            #ccu-motion-svg {{
                position:absolute;
                left:0;
                top:0;
                width:100%;
                height:100%;
                opacity:0;
                pointer-events:none;
                z-index:-1;
            }}
        </style>
    </head>
    <body>
        <div class="web-stage-wrap">
            <div class="web-stage">
                <div class="ccu-content">
                    {level_lines_html}
                    {pipe_html}
                    {blower_html}
                    {diverter_html}

                    {basket3_back_html}
                    {basket4_back_html}

                    {titan1_html}
                    {titan2_html}
                    {ews3_html}
                    {ews4_html}

                    <img
                        id="ccu-carrier"
                        src="{CARRIER_URI}"
                        draggable="false"
                    />

                    {basket3_front_html}
                    {basket4_front_html}

                    {label_html}
                    {send_html}
                    {dest_html}

                    <svg
                        id="ccu-motion-svg"
                        viewBox="0 0 {STAGE_WIDTH} {STAGE_HEIGHT}"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        {motion_paths_html}
                    </svg>
                </div>

                {logo_html(
                    AEROCOM_URI,
                    AEROCOM_LOGO_X,
                    AEROCOM_LOGO_Y,
                    AEROCOM_LOGO_TARGET_WIDTH,
                )}
                {logo_html(
                    PAZKOREA_URI,
                    PAZKOREA_LOGO_X,
                    PAZKOREA_LOGO_Y,
                    PAZKOREA_LOGO_TARGET_WIDTH,
                )}
            </div>
        </div>

        <script>
        (() => {{
            const STAGE_W = {STAGE_WIDTH};
            const STAGE_H = {STAGE_HEIGHT};
            const CARRIER_W = {carrier_width:.8f};
            const CARRIER_H = {carrier_height:.8f};

            const stationConfigs = {station_configs_json};
            const titanDoorConfigs = {titan_door_configs_json};
            const diverterFrames = {diverter_frames_json};

            const carrier = document.getElementById("ccu-carrier");
            const diverter = document.getElementById("ccu-diverter");

            const sendButtons = Array.from(
                document.querySelectorAll(".ccu-send")
            );
            const destButtons = Array.from(
                document.querySelectorAll(".ccu-dest")
            );

            const titanLayers = {{
                1: {{
                    inner: document.getElementById("ccu-titan1-inner"),
                    door: document.getElementById("ccu-titan1-door"),
                    front: document.getElementById("ccu-titan1-front"),
                }},
                2: {{
                    inner: document.getElementById("ccu-titan2-inner"),
                    door: document.getElementById("ccu-titan2-door"),
                    front: document.getElementById("ccu-titan2-front"),
                }},
            }};

            Object.values(titanLayers).forEach(layers => {{
                if (layers.inner) layers.inner.style.zIndex = "47";
                if (layers.door) layers.door.style.zIndex = "49";
                if (layers.front) layers.front.style.zIndex = "50";
            }});

            const sourcePaths = {{}};
            const destinationPaths = {{}};
            for (let no = 1; no <= 4; no += 1) {{
                sourcePaths[no] = document.getElementById(`ccu-src-path-${{no}}`);
                destinationPaths[no] = document.getElementById(`ccu-dst-path-${{no}}`);
            }}

            let running = false;
            let diverterAlignment = "middle";
            const currentDoorFraction = {{1: 1.0, 2: 1.0}};

            function xPct(x) {{ return (x / STAGE_W * 100) + "%"; }}
            function yPct(y) {{ return (y / STAGE_H * 100) + "%"; }}
            function sleep(ms) {{
                return new Promise(resolve => setTimeout(resolve, ms));
            }}
            function clamp01(t) {{ return Math.max(0, Math.min(1, t)); }}
            function smoothstep(t) {{
                t = clamp01(t);
                return t * t * (3 - 2 * t);
            }}
            function lerp(a, b, t) {{ return a + (b - a) * t; }}

            function animate(duration, update) {{
                return new Promise(resolve => {{
                    const start = performance.now();
                    function frame(now) {{
                        const raw = duration <= 0 ? 1 : (now - start) / duration;
                        const t = clamp01(raw);
                        update(t);
                        if (t < 1) requestAnimationFrame(frame);
                        else resolve();
                    }}
                    requestAnimationFrame(frame);
                }});
            }}

            function setCarrier(x, y, rotationDeg = 0, zIndex = 40) {{
                carrier.style.left = xPct(x - CARRIER_W / 2);
                carrier.style.top = yPct(y - CARRIER_H / 2);
                carrier.style.transform = `rotate(${{rotationDeg}}deg)`;
                carrier.style.zIndex = String(Math.round(zIndex));
                carrier.style.display = "block";
            }}

            async function moveCarrierLinear(
                from,
                to,
                duration,
                zIndex,
                rotationDeg = 0,
                easing = "smooth"
            ) {{
                await animate(duration, t => {{
                    const u = easing === "linear" ? t : smoothstep(t);
                    setCarrier(
                        lerp(from[0], to[0], u),
                        lerp(from[1], to[1], u),
                        rotationDeg,
                        zIndex
                    );
                }});
            }}

            async function moveOnPath(path, duration, zIndex = 40) {{
                const total = path.getTotalLength();
                await animate(duration, t => {{
                    const distance = total * t;
                    const p = path.getPointAtLength(distance);
                    const p2 = path.getPointAtLength(
                        Math.min(total, distance + 1.5)
                    );
                    const angle = Math.atan2(
                        p2.y - p.y,
                        p2.x - p.x
                    ) * 180 / Math.PI - 90;
                    setCarrier(p.x, p.y, angle, zIndex);
                }});
            }}

            // -------------------------------------------------
            // TITAN door: station 1 / 2 common
            // -------------------------------------------------
            function setDoorFraction(stationNo, fraction) {{
                const layers = titanLayers[stationNo];
                const cfg = titanDoorConfigs[stationNo];
                if (!layers || !layers.door || !cfg) return;

                const f = clamp01(fraction);
                currentDoorFraction[stationNo] = f;

                const scaleX =
                    {TITAN_DOOR_OPEN_SCALE_X}
                    + f * (
                        {TITAN_DOOR_CLOSED_SCALE_X}
                        - {TITAN_DOOR_OPEN_SCALE_X}
                    );

                const xLocal =
                    {TITAN_DOOR_OPEN_X_LOCAL}
                    + f * (
                        {TITAN_DOOR_CLOSED_X_LOCAL}
                        - {TITAN_DOOR_OPEN_X_LOCAL}
                    );

                const x =
                    cfg.front_left
                    + xLocal * {titan_scale:.10f}
                    + {TITAN_DOOR_ADJUST_X};

                const width =
                    {door_intrinsic_w:.10f}
                    * {titan_scale:.10f}
                    * scaleX
                    * {TITAN_DOOR_SCALE_X};

                layers.door.style.left = xPct(x);
                layers.door.style.top = yPct(cfg.door_y);
                layers.door.style.width = xPct(width);
                layers.door.style.height = yPct(cfg.door_height);
            }}

            async function animateDoor(stationNo, targetFraction, duration) {{
                const startFraction = currentDoorFraction[stationNo];
                await animate(duration, t => {{
                    const u = smoothstep(t);
                    setDoorFraction(
                        stationNo,
                        lerp(startFraction, targetFraction, u)
                    );
                }});
            }}

            // -------------------------------------------------
            // Diverter top / middle / bottom
            // -------------------------------------------------
            function setDiverterFrame(frameNumber) {{
                if (!diverter) return;
                const uri = diverterFrames[String(frameNumber)];
                if (uri) diverter.src = uri;
            }}

            async function animateDiverterFrames(startFrame, endFrame) {{
                const step = endFrame >= startFrame ? 1 : -1;
                for (let frame = startFrame; ; frame += step) {{
                    setDiverterFrame(frame);
                    if (frame === endFrame) break;
                    await sleep(50);
                }}
            }}

            async function alignDiverter(target) {{
                if (diverterAlignment === target) return;

                // Any non-middle state first returns to middle.
                if (diverterAlignment === "top") {{
                    await animateDiverterFrames(
                        {DIVERTER_TO_MIDDLE_START_FRAME},
                        {DIVERTER_TO_MIDDLE_END_FRAME}
                    );
                    diverterAlignment = "middle";
                }} else if (diverterAlignment === "bottom") {{
                    await animateDiverterFrames(
                        {DIVERTER_BOTTOM_TO_MIDDLE_START_FRAME},
                        {DIVERTER_BOTTOM_TO_MIDDLE_END_FRAME}
                    );
                    diverterAlignment = "middle";
                }}

                if (target === "top") {{
                    await animateDiverterFrames(
                        {DIVERTER_TO_TOP_START_FRAME},
                        {DIVERTER_TOP_FRAME}
                    );
                    diverterAlignment = "top";
                }} else if (target === "bottom") {{
                    await animateDiverterFrames(
                        {DIVERTER_TO_BOTTOM_START_FRAME},
                        {DIVERTER_TO_BOTTOM_END_FRAME}
                    );
                    diverterAlignment = "bottom";
                }} else {{
                    setDiverterFrame({DIVERTER_MIDDLE_FRAME});
                    diverterAlignment = "middle";
                }}
            }}

            function travelMilliseconds(stationNo, path) {{
                const reference = (
                    stationNo === 1 || stationNo === 2
                    ? sourcePaths[1]
                    : sourcePaths[4]
                );
                const baseSeconds = (
                    stationNo === 1 || stationNo === 2
                    ? {BYPASS_TO_NO1_SECONDS}
                    : {NO4_TO_BYPASS_SECONDS}
                );
                const ratio = path.getTotalLength() / reference.getTotalLength();
                return Math.max(0.65, baseSeconds * ratio) * 1000;
            }}

            // -------------------------------------------------
            // Source animation
            // -------------------------------------------------
            async function sendTitan(src, directRoute, sourceAlignPromise) {{
                const no = src.no;
                setDoorFraction(no, 1);

                // Before docking:
                // inner -> door -> front -> carrier
                setCarrier(src.entry_start[0], src.entry_start[1], 0, 51);

                await animateDoor(
                    no,
                    0,
                    ({TITAN_SEND_DOOR_OPEN_SECONDS} / {TITAN_LOAD_SEQUENCE_SPEED}) * 1000
                );

                await moveCarrierLinear(
                    src.entry_start,
                    src.entry_end,
                    ({TITAN_SEND_ENTRY_SECONDS} / {TITAN_LOAD_SEQUENCE_SPEED}) * 1000,
                    51,
                    0
                );

                // Docked:
                // inner(47) -> carrier(48) -> door(49) -> front(50)
                setCarrier(src.entry_end[0], src.entry_end[1], 0, 48);

                await animateDoor(
                    no,
                    1,
                    ({TITAN_SEND_DOOR_CLOSE_SECONDS} / {TITAN_LOAD_SEQUENCE_SPEED}) * 1000
                );

                // No.2 -> No.1 direct route starts immediately upward.
                if (directRoute && src.no === 2) {{
                    await sourceAlignPromise;
                    return src.entry_end;
                }}

                await moveCarrierLinear(
                    src.entry_end,
                    src.pipe,
                    {TITAN_SEND_TO_PIPE_SECONDS} * 1000,
                    48,
                    0
                );

                await sourceAlignPromise;
                return src.pipe;
            }}

            async function sendEws(src, sourceAlignPromise) {{
                setCarrier(
                    src.send_entry_start[0],
                    src.send_entry_start[1],
                    0,
                    58
                );

                await moveCarrierLinear(
                    src.send_entry_start,
                    src.send_load,
                    {EWS4_SEND_ENTRY_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                await sleep({EWS4_SEND_LOAD_HOLD_SECONDS} * 1000);
                await sourceAlignPromise;

                // X fixed vertical hide.
                await moveCarrierLinear(
                    src.send_load,
                    src.send_hidden,
                    {EWS4_SEND_VERTICAL_HIDE_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                // Only after fully hidden, shift horizontally to pipe center.
                await moveCarrierLinear(
                    src.send_hidden,
                    src.send_hidden_pipe,
                    {EWS4_SEND_HIDDEN_SHIFT_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                await moveCarrierLinear(
                    src.send_hidden_pipe,
                    src.pipe,
                    {EWS4_SEND_PIPE_RISE_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                return src.pipe;
            }}

            // -------------------------------------------------
            // Destination animation
            // -------------------------------------------------
            async function receiveTitan(dst, alreadyAtBody = false) {{
                const no = dst.no;
                setDoorFraction(no, 1);

                if (!alreadyAtBody) {{
                    await moveCarrierLinear(
                        dst.pipe,
                        dst.receive_body,
                        {NO1_RECEIVE_RISE_SECONDS} * 1000,
                        48,
                        0,
                        "linear"
                    );
                }} else {{
                    setCarrier(
                        dst.receive_body[0],
                        dst.receive_body[1],
                        0,
                        48
                    );
                }}

                const hiddenStart = performance.now();

                await moveCarrierLinear(
                    dst.receive_body,
                    dst.receive_output_hidden,
                    {NO1_RECEIVE_REDIRECT_SECONDS} * 1000,
                    48,
                    0
                );

                const hiddenElapsed = performance.now() - hiddenStart;
                await sleep(
                    Math.max(
                        0,
                        {NO1_RECEIVE_HIDDEN_WAIT_SECONDS} * 1000
                        - hiddenElapsed
                    )
                );

                await moveCarrierLinear(
                    dst.receive_output_hidden,
                    dst.receive_output_emerge,
                    {NO1_RECEIVE_EMERGE_SECONDS} * 1000,
                    48,
                    0,
                    "linear"
                );

                await animate({NO1_RECEIVE_DROP_SECONDS} * 1000, t => {{
                    const dropT = t * t;
                    const rotationT = smoothstep(t);
                    setCarrier(
                        lerp(
                            dst.receive_output_emerge[0],
                            dst.receive_basket_drop[0],
                            dropT
                        ),
                        lerp(
                            dst.receive_output_emerge[1],
                            dst.receive_basket_drop[1],
                            dropT
                        ),
                        dst.drop_rotation * rotationT,
                        48
                    );
                }});
            }}

            async function receiveEws(dst) {{
                // Match desktop: after pipe arrival, carrier is placed behind EWS.
                setCarrier(
                    dst.receive_hidden_start[0],
                    dst.receive_hidden_start[1],
                    0,
                    58
                );

                await moveCarrierLinear(
                    dst.receive_hidden_start,
                    dst.receive_output,
                    {EWS_RECEIVE_INSIDE_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                await moveCarrierLinear(
                    dst.receive_output,
                    dst.receive_emerge,
                    {EWS_RECEIVE_EMERGE_SECONDS} * 1000,
                    58,
                    0,
                    "linear"
                );

                await animate({EWS_RECEIVE_DROP_SECONDS} * 1000, t => {{
                    const dropT = t * t;
                    const rotationT = smoothstep(t);
                    setCarrier(
                        lerp(dst.receive_emerge[0], dst.receive_basket_drop[0], dropT),
                        lerp(dst.receive_emerge[1], dst.receive_basket_drop[1], dropT),
                        dst.drop_rotation * rotationT,
                        58
                    );
                }});
            }}

            // -------------------------------------------------
            // Direct TITAN 1 <-> 2
            // -------------------------------------------------
            async function directTitanTransfer(sourceNo, destinationNo, startPoint) {{
                const dst = stationConfigs[destinationNo];
                const referenceSpeed =
                    sourcePaths[1].getTotalLength()
                    / Math.max(0.01, {BYPASS_TO_NO1_SECONDS});

                const directDistance = Math.abs(
                    dst.receive_body[1] - startPoint[1]
                );
                const duration = Math.max(
                    0.20,
                    directDistance / Math.max(1.0, referenceSpeed)
                ) * 1000;

                await animate(duration, t => {{
                    let x = lerp(startPoint[0], dst.receive_body[0], t);
                    const y = lerp(startPoint[1], dst.receive_body[1], t);

                    if (sourceNo === 2 && destinationNo === 1) {{
                        x += {TITAN_2_TO_1_DIRECT_PIPE_OFFSET_X};
                    }}

                    setCarrier(x, y, 0, 48);
                }});

                setCarrier(
                    dst.receive_body[0],
                    dst.receive_body[1],
                    0,
                    48
                );
            }}

            // -------------------------------------------------
            // All 12 routes
            // -------------------------------------------------
            async function runTransport(sourceNo, destinationNo) {{
                if (running || sourceNo === destinationNo) return;

                running = true;
                hideDestinations();
                setControlsRunning(true);

                const src = stationConfigs[sourceNo];
                const dst = stationConfigs[destinationNo];
                const directTitanRoute = (
                    src.type === "titan"
                    && dst.type === "titan"
                );

                // Start every run with TITAN doors closed.
                setDoorFraction(1, 1);
                setDoorFraction(2, 1);

                try {{
                    const sourceAlignPromise = directTitanRoute
                        ? Promise.resolve()
                        : alignDiverter(src.branch);

                    let sourceStart;
                    if (src.type === "titan") {{
                        sourceStart = await sendTitan(
                            src,
                            directTitanRoute,
                            sourceAlignPromise
                        );
                    }} else {{
                        sourceStart = await sendEws(
                            src,
                            sourceAlignPromise
                        );
                    }}

                    if (directTitanRoute) {{
                        await directTitanTransfer(
                            sourceNo,
                            destinationNo,
                            sourceStart
                        );
                        await receiveTitan(dst, true);
                        return;
                    }}

                    // Source -> bypass
                    const srcPath = sourcePaths[sourceNo];
                    await moveOnPath(
                        srcPath,
                        travelMilliseconds(sourceNo, srcPath),
                        40
                    );

                    setCarrier(
                        {BYPASS_STOP_X},
                        {BYPASS_STOP_Y},
                        src.type === "titan" ? -90 : 90,
                        40
                    );

                    // Stop at bypass while destination port aligns.
                    await alignDiverter(dst.branch);

                    // Bypass -> destination
                    const dstPath = destinationPaths[destinationNo];
                    await moveOnPath(
                        dstPath,
                        travelMilliseconds(destinationNo, dstPath),
                        40
                    );

                    if (dst.type === "titan") {{
                        setCarrier(dst.pipe[0], dst.pipe[1], 0, 40);
                        await receiveTitan(dst, false);
                    }} else {{
                        await receiveEws(dst);
                    }}
                }} finally {{
                    carrier.style.display = "none";
                    setDoorFraction(1, 1);
                    setDoorFraction(2, 1);
                    running = false;
                    setControlsRunning(false);
                }}
            }}

            // -------------------------------------------------
            // UI controls
            // -------------------------------------------------
            function hideDestinations() {{
                destButtons.forEach(button => {{
                    button.style.display = "none";
                }});
            }}

            function showDestinations(sourceNo) {{
                hideDestinations();
                destButtons.forEach(button => {{
                    if (Number(button.dataset.source) === sourceNo) {{
                        button.style.display = "flex";
                    }}
                }});
            }}

            function setControlsRunning(active) {{
                sendButtons.forEach(button => {{
                    button.disabled = active;
                }});
                destButtons.forEach(button => {{
                    button.disabled = active;
                }});
            }}

            sendButtons.forEach(button => {{
                button.addEventListener("click", () => {{
                    if (running) return;
                    const sourceNo = Number(button.dataset.source);
                    const group = destButtons.filter(
                        item => Number(item.dataset.source) === sourceNo
                    );
                    const currentlyVisible = group.some(
                        item => item.style.display === "flex"
                    );
                    if (currentlyVisible) hideDestinations();
                    else showDestinations(sourceNo);
                }});
            }});

            destButtons.forEach(button => {{
                button.addEventListener("click", () => {{
                    if (running) return;
                    runTransport(
                        Number(button.dataset.source),
                        Number(button.dataset.destination)
                    );
                }});
            }});

            // Initial scene.
            setDiverterFrame({DIVERTER_MIDDLE_FRAME});
            diverterAlignment = "middle";
            setDoorFraction(1, 1);
            setDoorFraction(2, 1);
            carrier.style.display = "none";
            hideDestinations();
            setControlsRunning(false);
        }})();
        </script>
    </body>
    </html>
    """

    components.html(
        html,
        height=700,
        scrolling=False,
    )


# ============================================================
# 화면 전환
# ============================================================

view = st.query_params.get(
    "view",
    "main",
)

if view == "ptp":
    show_point_to_point()

elif view == "central":
    show_central_placeholder()

else:
    show_main_menu()
