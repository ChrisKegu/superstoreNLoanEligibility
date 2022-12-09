import streamlit as st 
import os
from classes.data_class import data
from classes.data_class import sales_and_profit_per_market
from classes.data_class import monthly_sales_performance
from classes.data_class import dominant_product_category_in_each_market
from classes.data_class import products_making_losses
css_path=os.path.join('static','style.css')

with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
    
#st.write(data.head())
tabs=['Sales and Profit Per Market','Monthly Sales Performances',
'Dominant Product Category in Each Market','Products Making Losses'
]
tab1, tab2, tab3,tab4 = st.tabs(tabs)

with tab1:
   #st.header("Sales and Profilt Per Market")
   st.plotly_chart(sales_and_profit_per_market())
   #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:

    #st.header("A dog")
    #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    #fig=monthly_sales_performance()
    #st.plotly_chart(fig)
    #st.markdown("""""")
    #with st.expander("See narations"):
    st.write('fdfdsf') 
with tab3:
   #st.header("An owl")
   #st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    text='The dominant product category is Office Supplies followed by Technology and Furniture in all markets'
    st.expander(text)
    result,fig=dominant_product_category_in_each_market()
    st.plotly_chart(fig)
   
    with st.expander("See narations"):
        st.write(text)
   
#st.markdown(text)
   #st.dataframe(result)
with tab4:
    num=st.number_input('Number of Products to view')
    if num ==0:
        num=10

    else:
        num=int(num)
        
    result,fig=products_making_losses(num)
    st.plotly_chart(fig)
