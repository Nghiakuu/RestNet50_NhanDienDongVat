import streamlit as st

@st.cache_resource
def doc_ten_tieng_viet():
    """Đọc danh sách tên tiếng Việt từ file"""
    with open('animal_classes_vi.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

@st.cache_resource
def tai_danh_sach_ten():
    """Tải danh sách tên tiếng Việt"""
    return doc_ten_tieng_viet()

def doc_ten_tieng_anh():
    """Đọc danh sách tên tiếng Anh từ file"""
    with open('imagenet_classes.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()] 