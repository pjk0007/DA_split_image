import matplotlib.pyplot as plt

# 시각화 함수
def show_all_sections(sections, columns=3, figsize=(12, 16)):
    rows = (len(sections) + columns - 1) // columns  # 필요한 행 수 계산
    plt.figure(figsize=figsize)

    for i, sec in enumerate(sections):
        plt.subplot(rows, columns, i + 1)
        plt.imshow(sec)
        plt.axis('off')
        plt.title(f"Section {i}")

    plt.tight_layout()
    plt.show()