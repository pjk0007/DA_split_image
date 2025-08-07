import cv2
import numpy as np
from matplotlib import pyplot as plt
from split.split_by_color import split_by_color
from split.split_by_whitespace import split_by_whitespace
from split.split_by_edges import split_by_edges
from utils.show_all_sections import show_all_sections
from utils.image_to_array import image_to_array

def visualize_labels(labels, highlight_labels):
    # 강조할 라벨만 표시
    display = np.zeros_like(labels, dtype=np.uint8)
    for l in highlight_labels:
        display[labels == l] = 255

    plt.figure(figsize=(10, 20))
    plt.imshow(display, cmap='gray')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # 이미지 경로를 지정하세요
    # image_path = '뉴셀_블랙마카.jpg'
    image_path = '상페-딱딱이복숭아.png'
    image = image_to_array(image_path)
    
    # 시도 목록
    # 1. 색상 기준 섹션 분할
    # from split_by_color import split_by_color
    # img_rgb, sections, boundaries = split_by_color(image, threshold=100)

    # 2. 공백 기준 섹션 분할 (주석 처리된 부분은 필요시 사용)
    # sections, boundaries = split_by_whitespace(image, empty_threshold=1, min_gap_height=160)
    # show_all_sections(sections)

    # 3. 배경 기준 섹션 분할
    # sections, boundaries = split_by_edges(image, connectivity=4)
    # show_all_sections(sections)

    # 2 -> 3. 공백 기준 분할 후 배경 기준 분할
    total_sections = []
    sections, boundaries = split_by_whitespace(image, empty_threshold=1, min_gap_height=160)
    for sec in sections:
        sec_sections, sec_boundaries = split_by_edges(sec, connectivity=4)
        total_sections.extend(sec_sections)
    show_all_sections(total_sections)
    
