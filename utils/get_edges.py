import cv2

def get_edges(image):
    """
    이미지에서 엣지를 추출합니다.
    
    Args:
        image (numpy.ndarray): 입력 이미지 (BGR 형식).
    
    Returns:
        numpy.ndarray: 엣지가 추출된 이미지 (흑백).
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    edges = cv2.Canny(gray, 50, 100)
    return edges