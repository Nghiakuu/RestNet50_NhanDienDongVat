import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import streamlit as st
from utils import chuan_hoa_nhan
from data import doc_ten_tieng_anh

@st.cache_resource
def tai_mo_hinh():
    """Tải mô hình ResNet50 đã được huấn luyện sẵn"""
    return ResNet50(weights='imagenet')

def kiem_tra_dong_vat(image):
    """
    Kiểm tra xem ảnh có phải là động vật hay không
    Trả về True nếu là động vật, False nếu không phải
    """
    # Resize ảnh về kích thước 224x224
    image = image.resize((224, 224))
    
    # Chuyển ảnh thành mảng numpy và tiền xử lý
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Dự đoán kết quả đầu tiên
    preds = tai_mo_hinh().predict(img_array)
    decoded_preds = decode_predictions(preds, top=1)[0]
    
    # Đọc danh sách động vật từ module data
    danh_sach_dong_vat = doc_ten_tieng_anh()
    
    # Debug: In ra tên class trước và sau khi chuẩn hóa
    #st.write("Debug - Tên class gốc:", decoded_preds[0][1])
    class_name = chuan_hoa_nhan(decoded_preds[0][1])
    #st.write("Debug - Tên class sau khi chuẩn hóa:", class_name)

    
    # Kiểm tra kết quả đầu tiên
    return class_name in danh_sach_dong_vat

def du_doan(hinh_anh, ten_tieng_viet, ten_tieng_anh_chuan):
    """Thực hiện dự đoán trên hình ảnh đầu vào"""
    # Chuyen doi anh thanh RGB
    if hinh_anh.mode != "RGB":
        hinh_anh = hinh_anh.convert("RGB")
    
    # Tai mo hinh
    mo_hinh = tai_mo_hinh()

    img = hinh_anh.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Du doan
    ket_qua = mo_hinh.predict(img_array)
    decoded = decode_predictions(ket_qua, top=3)[0]
    
    # Chuyen doi ket qua sang tieng Viet
    ket_qua = []
    for _, nhan, diem in decoded:
        nhan_chuan = chuan_hoa_nhan(nhan)
        try:
            idx = ten_tieng_anh_chuan.index(nhan_chuan)
            ten_vi = ten_tieng_viet[idx] if idx < len(ten_tieng_viet) else nhan
            ket_qua.append((nhan, ten_vi, diem))
        except ValueError:
            ket_qua.append((nhan, nhan, diem))
    
    return ket_qua 