import streamlit as st
from PIL import Image
from utils import lay_thong_tin_dong_vat, chuan_hoa_nhan
from model import du_doan
from data import tai_danh_sach_ten, doc_ten_tieng_anh
import base64

def image_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Cau hinh trang
st.set_page_config(
    page_title="Nhan dien Dong vat AI",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tay chinh
st.markdown("""
    <style>
    /* Thiet lap font chu va mau nen chinh */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Tiêu đề chính */
    .main .block-container h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Tiêu đề phụ */
    .main .block-container h3 {
        color: #34495e;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Nút tải lên */
    .stFileUploader {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    /* Nút nhận diện */
    .stButton>button {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 12px 30px;
        border-radius: 25px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton>button:hover {
        background: linear-gradient(45deg, #45a049, #4CAF50);
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    
    /* Kết quả nhận diện */
    .result-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .result-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    
    /* Thông tin */
    .stInfo {
        background-color: #e8f5e9;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Link Wikipedia */
    .wiki-link {
        color: #2196F3;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .wiki-link:hover {
        color: #1976D2;
        text-decoration: underline;
    }
    
    /* Loading spinner */
    .stSpinner {
        margin: 2rem 0;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main .block-container h1 {
            font-size: 2rem;
        }
        
        .stButton>button {
            padding: 10px 20px;
            font-size: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Tạo container để căn giữa hình ảnh
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("images/Logo.png", width=100)
    
    st.title("🐾 Nhận diện Động vật AI")
    st.markdown("---")
    st.markdown("""
    ### 📝 Hướng dẫn sử dụng
    1. Tải lên hình ảnh động vật
    2. Nhấn nút "Nhận diện"
    3. Xem kết quả và thông tin chi tiết
    
    ### ℹ️ Thông tin
    - Sử dụng mô hình ResNet50
    - Hỗ trợ nhiều loài động vật
    - Độ chính xác...
    """)
    st.markdown("---")
    st.markdown("Made by NghiaNT")

# Giao dien chinh
st.title('🐾 Nhận diện động vật AI')
st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h3>📸 Tải lên hình ảnh động vật để nhận diện</h3>
        <p style='color: #666;'>Ứng dụng này sử dụng mô hình ResNet50 đã được huấn luyện trên tập dữ liệu ImageNet
        để nhận diện các loài động vật trong hình ảnh của bạn.</p>
    </div>
""", unsafe_allow_html=True)

# Tao hai cot
col1, col2 = st.columns(2)

with col1:
    # Upload file
    uploaded_file = st.file_uploader("Chọn một hình ảnh...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Hiển thị ảnh
        image = Image.open(uploaded_file)
        st.image(image, caption='Hình ảnh đã tải lên', use_container_width=True) # use_container_width  use_column_width
        
        # Nut nhan diend
        if st.button('🔍 Nhận diện'):
            with st.spinner('Đang phân tích hình ảnh...'):
                # Tải danh sách tên
                ten_tieng_viet = tai_danh_sach_ten()
                ten_tieng_anh = doc_ten_tieng_anh()
                ten_tieng_anh_chuan = [chuan_hoa_nhan(ten) for ten in ten_tieng_anh]
                
                # Thuc hien du doan
                ket_qua = du_doan(image, ten_tieng_viet, ten_tieng_anh_chuan)
                
                if ket_qua:
                    with col2:
                        st.markdown("### 📊 Kết quả nhận diện")
                        
                        # Hiển thị top 3 kết quả
                        wiki_url = None
                        ten_vi_top1 = None
                        for i, (_, ten_vi, diem) in enumerate(ket_qua):
                            if i == 0:
                                accuracy_img = "images/High.png"
                                ten_vi_top1 = ten_vi
                            elif i == 1:
                                accuracy_img = "images/Medium.png"
                            else:
                                accuracy_img = "images/Low.png"
                            img_base64 = image_to_base64(accuracy_img)
                            if diem > 0.5:
                                accuracy_text = "Cao"
                            elif diem > 0.3:
                                accuracy_text = "Trung bình"
                            else:
                                accuracy_text = "Thấp"

                            st.markdown(f"""
                                <div style="
                                    display: flex;
                                    align-items: center;
                                    justify-content: space-between;
                                    background: #fff;
                                    border-radius: 16px;
                                    box-shadow: 0 4px 12px rgba(44,62,80,0.08);
                                    padding: 1.2rem 1.5rem;
                                    margin-bottom: 1.2rem;
                                    border: 1px solid #e0e0e0;
                                ">
                                    <div>
                                        <h4 style='color: #2c3e50; margin-bottom: 0.5rem; margin-top: 0;'>#{i+1} {ten_vi}</h4>
                                        <p style='color: #666; margin: 0;'>Độ chính xác: {diem*100:.2f}% ({accuracy_text})</p>
                                    </div>
                                    <img src="data:image/png;base64,{img_base64}" style="width: 100px; height: 100px; margin-left: 20px;">
                                </div>
                            """, unsafe_allow_html=True)
                            # Lấy thông tin về loài động vật cho kết quả đầu tiên
                            if i == 0:
                                wiki_url = lay_thong_tin_dong_vat(ten_vi)
                        # Hiển thị link wiki ra ngoài, dưới cùng khối #1
                        if wiki_url and ten_vi_top1:
                            st.markdown(f"""
                                <div style='text-align: center; margin: 0 auto 1.5rem auto; max-width: 400px; border: 1px solid #e0e0e0; border-radius: 12px; background: #f5f7fa; padding: 1rem;'>
                                    <a href='{wiki_url}' target='_blank' class='wiki-link' style='font-size: 1.1rem; font-weight: 600;'>
                                        🔗 Tìm hiểu thêm về {ten_vi_top1}
                                    </a>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        st.markdown("""
                            <div style='margin-top: 2rem; padding: 1rem; background-color: #f8f9fa; border-radius: 10px;'>
                                <h4 style='color: #2c3e50; margin-bottom: 1rem;'>💡 Lưu ý</h4>
                                <ul style='color: #666; margin: 0; padding-left: 1.5rem;'>
                                    <li>Kết quả được sắp xếp theo độ chính xác giảm dần</li>
                                    <li>Độ chính xác được tính theo phần trăm</li>
                                    <li>Bạn có thể tìm hiểu thêm về loài động vật qua link Wikipedia</li>
                                </ul>
                            </div>
                        """, unsafe_allow_html=True)
    else:
        with col2:
            st.markdown("""
        <div style="
            background-color: #e8f5e9;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            color: #222;
            font-size: 1.1rem;
        ">
            👈 Vui lòng tải lên một hình ảnh để bắt đầu nhận diện
        </div>
    """, unsafe_allow_html=True)