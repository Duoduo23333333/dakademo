import streamlit as st
from datetime import datetime, time, timedelta
from PIL import Image  # 导入Pillow图像处理库
import requests
import base64
from io import BytesIO



# 设置开始和结束时间
start_time = time(0, 0)
end_time = time(23, 59)

# 计算时间间隔（单位为分钟）
time_step = 1
time_interval = int(timedelta(hours=1).total_seconds() / 60 / time_step)

# 在发起请求前调用 st.image() 方法，显示占位符图片
placeholder_image = Image.open("./sample.jpg")
image_placeholder = st.image(placeholder_image, output_format="JPEG", use_column_width=True)




# 将小时和分钟设置为两个独立的下拉框
col1, col2 ,_,col3,col4,col5= st.columns([16, 16, 6, 30, 16, 16])
with col1:
    hour1 = st.selectbox("① 截图时间", range(start_time.hour, end_time.hour+1), format_func=lambda x: f"{x} 时", key="hour1")
with col2:
    minute1 = st.selectbox("", range(0, 60, time_step), format_func=lambda x: f"{x} 分", key="min1")
with col3:
    date = st.date_input("② 运动日期",key="ss1")
with col4:
    hour = st.selectbox("", range(start_time.hour, end_time.hour+1), format_func=lambda x: f"{x} 时", key="hour")
with col5:
    minute = st.selectbox("", range(0, 60, time_step), format_func=lambda x: f"{x} 分", key="min")




c1, c2 ,_,c3,_,c4= st.columns([16, 16,  6, 20,6, 36])
with c1:
    v1 = st.selectbox("③ 平均配速", range(0, 60, 1), format_func=lambda x: f"{x} 分")
with c2:
    v2 = st.selectbox("", range(0, 60, 1), format_func=lambda x: f"{x} 秒")
with c3:
    float_values = [1, 1.01, 1.02, 2, 2.01, 2.02,3, 3.01, 3.02, 4, 4.01, 4.02, 5, 5.01, 5.02, 6, 6.01, 6.02, 7, 7.01, 7.02, 8, 8.01, 8.02,9, 9.01, 9.02, 9.98, 9.99]
    kms = st.selectbox("④ 公里数",  options=float_values, format_func=lambda x: f"{x} Km")
with c4:
    name = st.text_input("⑤ 名字")


hour1_str = f"{hour1:02d}"
minute1_str = f"{minute1:02d}"
date_str = date.strftime("%Y/%m/%d")
hour_str = f"{hour:02d}"
minute_str = f"{minute:02d}"
text1=hour1_str+":"+minute1_str
text2=f"{name}"
text3=date_str+" "+hour_str+":"+minute_str
text4='{:.2f}'.format(kms)
text5= f"{v1:02d}"
text6= f"{v2:02d}"




uploaded_file = st.file_uploader("⑥ 头像", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # 获取Base64编码
    text0 = base64.b64encode(uploaded_file.read()).decode()



if uploaded_file is None:
    st.warning("上传头像后可提交")
else:
    if st.button("生成图片", use_container_width=True):
        url = "https://b-ps-aclcsxgizt.cn-hangzhou.fcapp.run/api"
        data = {
            "text0": text0,
            "text1": text1,
            "text2": text2,
            "text3": text3,
            "text4": text4,
            "text5": text5,
            "text6": text6
        }
        response = requests.post(url, data=data)
        ba=response.text
        image2 = Image.open(BytesIO(base64.b64decode(ba)))
        image_placeholder.empty()
        image_placeholder.image(image2, output_format="JPEG", use_column_width=True)
