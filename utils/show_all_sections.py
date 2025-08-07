import cv2
import matplotlib.pyplot as plt

# 시각화 함수
def show_all_sections(sections, columns=4, figsize=(12, 16)):
    rows = (len(sections) + columns - 1) // columns  # 필요한 행 수 계산
    plt.figure(figsize=figsize)

    for i, sec in enumerate(sections):
        cv2.imwrite(f'out/section_{i}.png', sec)  # 각 섹션을 파일로 저장
        plt.subplot(rows, columns, i + 1)
        plt.imshow(sec)
        # plt.axis('off')
        plt.title(f"Section {i}")

    plt.tight_layout()
    plt.show()