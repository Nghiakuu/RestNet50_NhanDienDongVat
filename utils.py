import requests

def lay_thong_tin_dong_vat(ten_dong_vat):
    """Lấy thông tin về loài động vật từ Wikipedia"""
    try:
        url = f"https://vi.wikipedia.org/wiki/{ten_dong_vat}"
        response = requests.get(url)
        if response.status_code == 200:
            return url
        return None
    except:
        return None

def chuan_hoa_nhan(nhan):
    """Chuẩn hóa nhãn bằng cách thay thế dấu gạch dưới và chuyển về chữ thường"""
    return nhan.replace('_', ' ') 