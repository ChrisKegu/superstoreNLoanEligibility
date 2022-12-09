import streamlit as st 
import os
from millify import millify
from classes.data_class import data
css_path=os.path.join('static','style.css')

with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

y2011=data[data['Order_Year']==2011]['Customer_Name'].nunique()
y2012=data[data['Order_Year']==2012]['Customer_Name'].nunique()
y2013=data[data['Order_Year']==2013]['Customer_Name'].nunique()
y2014=data[data['Order_Year']==2014]['Customer_Name'].nunique()
#most_profit=data['Profit'].max()
#most_sold=data['Product_Name'].groupby('Product_Name').count().max()
result=data[['Product_Name','Count']]\
    .groupby(['Product_Name']).count()\
    .sort_values(by=['Count'],ascending=False)
result.reset_index(inplace=True)

most_profit=data[['Product_Name','Profit']]\
    .groupby(['Product_Name']).max()\
    .sort_values(by=['Profit'],ascending=False)
most_profit.reset_index(inplace=True)

most_profit_customer=data[['Customer_Name','Profit']]\
    .groupby(['Customer_Name']).sum()\
    .sort_values(by=['Profit'],ascending=False)
most_profit_customer.reset_index(inplace=True)

#st.write(most_profit_customer.head())
#most_sold=result['Product_Name'].head(1)[0]+' '+str(result['Count'].head(1)[0])
col11, col21, col31 = st.columns(3)
col11.write('Most Purchased Product')
col11.metric(result['Product_Name'].head()[0],result['Count'].head(1)[0], )
col21.write('Most Profitable Product')
col21.metric(most_profit['Product_Name'].head(1)[0], millify(most_profit['Profit'].head(1)[0],precision=2), )
col31.write('Most Profitable \n Customer')
col31.metric(most_profit_customer['Customer_Name'].head()[0], millify(most_profit_customer['Profit'].head(1)[0],precision=2) , )

col1, col2, col3,col4 = st.columns(4)
#st.write(f'Profit=={most_profit}')
#st.write(f'most sold=={most_sold}')
col1.write('No. of Purchases \n in 2011')
col1.metric('', y2011, )
col2.write('No. of Purchases \n in 2012')
col2.metric('', y2012, )
col3.write('No. of Purchases \n in 2013')
col3.metric('', y2013, )
col4.write('No. of Purchases \n in 2014')
col4.metric('', y2014, )
#st.write('Number of unique purchases made by customers in 2011: {}'.format(data[data['Order_Year']==2011]['Customer_Name'].nunique()))
#st.write('Number of unique purchases made by customers in 2012: {}'.format(data[data['Order_Year']==2012]['Customer_Name'].nunique()))
#st.write('Number of unique purchases made by customers in 2013: {}'.format(data[data['Order_Year']==2013]['Customer_Name'].nunique()))
#st.write('Number of unique purchases made by customers in 2014: {}'.format(data[data['Order_Year']==2014]['Customer_Name'].nunique()))
def main():
    #st.title('This is a title')
    #st.subheader('This is a sub header')




    if __name__=='__main__':
        main()