from split_by_color import split_by_color
from show_all_sections import show_all_sections


if __name__ == "__main__":
    # 이미지 경로를 지정하세요
    image_path = '상페-딱딱이복숭아.png'
    
    # 시도 목록
    # 1. 색상 기준 섹션 분할
    img_rgb, sections, boundaries = split_by_color(image_path)

    # 2. 오브젝트 기준 섹션 분할 (이 부분은 구현되지 않았습니다)
    # sections = split_by_object(image_path)

    # 시각화
    show_all_sections(sections)