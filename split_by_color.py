import cv2
import numpy as np

# 자동 섹션 분할 함수
# 이미지의 각 행(row)별 평균 RGB 값을 계산하여, 윈도우 크기 내에서 색상 차이를 비교하여 섹션을 분할합니다.
# threshold: 색상 차이 임계값
# min_section_height: 최소 섹션 높이
# window: 윈도우 크기 (몇 행을 비교할지)
def split_by_color(image_path, threshold=200, min_section_height=100, window=5):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image_rgb.shape

    # 각 row별 평균 RGB
    row_colors = np.mean(image_rgb, axis=1)  # shape: (h, 3)

    boundaries = [0]

    for y in range(window, h - window):
        # 윗쪽 평균 색
        upper_mean = np.mean(row_colors[y - window:y], axis=0)
        # 아랫쪽 평균 색
        lower_mean = np.mean(row_colors[y:y + window], axis=0)

        diff = np.linalg.norm(upper_mean - lower_mean)

        if diff > threshold and (y - boundaries[-1]) > min_section_height:
            boundaries.append(y)

    # 마지막 줄 포함
    if boundaries[-1] != h:
        boundaries.append(h)

    # 이미지 자르기
    sections = []
    for i in range(len(boundaries) - 1):
        top = boundaries[i]
        bottom = boundaries[i + 1]
        cropped = image_rgb[top:bottom]
        sections.append(cropped)

    return image_rgb, sections, boundaries