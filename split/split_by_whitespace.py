import cv2
import numpy as np
from utils.image_to_array import image_to_array

# 공백 기준 섹션 분할 함수
# TODO:
# 현재는 밝은 영역을 공백으로 판단
# 검은색이더라도 충분히 넓은 영역은 공백으로 판단할 수 있도록 개선 필요
# 현재 row에서 min_gap_height 이상 공백이 있으면 섹션으로 분할
# empty_threshold: 공백으로 판단할 밝기 차이 임계값
# min_gap_height: 최소 공백 높이
# 이 값보다 작은 공백은 섹션으로 분할하지 않음

def split_by_whitespace(image, empty_threshold=8, min_gap_height=150):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    # 행마다 평균 밝기 계산
    row_means = np.mean(gray, axis=1)

    # 일정 밝기 이상이 연속된 줄 수만큼 나오면 공백으로 판단
    empty_rows = row_means > (255 - empty_threshold)
    empty_row_indices = []

    count = 0
    for i, is_empty in enumerate(empty_rows):
        if is_empty:
            count += 1
        else:
            if count >= min_gap_height:
                empty_row_indices.append(i - count // 2)  # 공백 중간을 경계로
            count = 0
    if count >= min_gap_height:
        empty_row_indices.append(h - count // 2)

    # 섹션 경계 설정
    boundaries = [0] + empty_row_indices + [h]

    # 이미지 자르기
    sections = []
    for i in range(len(boundaries) - 1):
        top = boundaries[i]
        bottom = boundaries[i + 1]
        cropped = image[top:bottom]
        sections.append(cropped)

    return sections, boundaries