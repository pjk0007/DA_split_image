import cv2
import numpy as np

def split_by_edges(image, connectivity=4):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 엣지 추출
    edges = cv2.Canny(gray, 140, 150)
    binary = (edges == 0).astype(np.uint8) * 255

    # 연결된 영역 라벨링
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        binary, connectivity=connectivity
    )

    h, w = edges.shape
    bg_labels = []
    boundaries = []

    # 배경 라벨 찾기
    for label in range(1, num_labels):  # 0번 라벨은 무시 (전체 배경)
        x, y, width, height, area = stats[label]
        if x == 0 and (x + width) == w:
            bg_labels.append(label)
            boundaries.append((y, y + height))

    sections = []

    before_bottom = -1
    new_boundaries = []

    # 섹션 분할
    for boundary in boundaries:
        top, bottom = boundary
        if top < before_bottom:
            sections.append(image[before_bottom : bottom])
            new_boundaries.append((before_bottom, bottom))
        elif top > before_bottom + 1:
            sections.append(image[before_bottom : top])
            new_boundaries.append((before_bottom, top))

            sections.append(image[top : bottom])
            new_boundaries.append((top, bottom))
        else:
            sections.append(image[top : bottom])
            new_boundaries.append((top, bottom))

        before_bottom = bottom

    return sections, new_boundaries
