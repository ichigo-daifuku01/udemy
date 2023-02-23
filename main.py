import streamlit as st
import numpy as np
import pandas  as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'





left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム') 
  
expander1 = st.expander('問い合わせ1')
expander1.warning('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.warning('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.warning('問い合わせ3の回答')

#if st.checkbox('show image'):
#   img = Image.open('background3.jpg') 
#   st.image(img, caption='background', use_column_width=True)
