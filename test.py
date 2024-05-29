import streamlit as st

st.title('Trà sữa CoTAI')

size = st.radio('Cỡ', options=('Nhỏ (20K)', 'Vừa (30K)', 'Lớn (40K)'), horizontal=True)
n = st.number_input('Số lượng', min_value=1, max_value=100, step=1)
st.write('Thêm')
milk = st.checkbox('Sữa (5K)')
cafe = st.checkbox('Cà phê (10K)')
st.write(n, size, milk, cafe)

if st.button('Đặt', use_container_width=True):
  # TO-DO: tính số tiền phải trả
  money = 0
  st.success('Đặt hàng thành công, số tiền phải trả: ' + str(money) + 'K')
  st.balloons()