import streamlit as st 
import os
from classes.data_class import data
from classes.data_class import sales_and_profit_per_market
from classes.data_class import profit_by_segment
from classes.data_class import sales_by_order_priority
from classes.data_class import average_shipping_cost_per_region
from classes.data_class import products_market_target
from classes.data_class import annual_sales_performance_by_categories
from classes.data_class import monthly_sales_performance
from classes.data_class import quarterly_sales_performance
from classes.data_class import percentage_changes
from classes.data_class import weekly_performance
from classes.data_class import customer_distribution_by_country
from classes.data_class import month_over_month_sales
#"Profit and Profit Margins by segments"
css_path=os.path.join('static','style.css')

with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

#st.markdown("Profit By Segments")
with st.expander("Profit By Segments"):
        
        result, fig=profit_by_segment()
        st.plotly_chart(fig)

with st.expander("Sales Performance"):
    tabs=['Sales','Sales Growth',
    'Demographics','Month Over Month Sales',
    '% Changes in Sales']
    tab1, tab2, tab3,tab4,tab5 = st.tabs(tabs)
    with tab1: 
        graph=st.radio('Display',('Order Priority','Weekly Sales',
        'Monthly Sales','Quarterly Sales',
        'Annual Sales'),horizontal=True)
        text='_'*100
        st.write(text)
        if graph=='Order Priority':
            visual_display=st.radio('Type',('Visual','Tabular'),horizontal=True)
            result,fig=sales_by_order_priority()
            #display graph or dataframe
            if visual_display=='Visual':
                st.plotly_chart(fig)
            elif visual_display=='Tabular':
                #result=result[['Order_Priority','Sales']]
                st.write('Sales By Order Priority')
                st.dataframe(result,use_container_width=True)
        elif graph=='Monthly Sales':

            fig=monthly_sales_performance()
            st.plotly_chart(fig)
            st.write('December is the month with most sales as February is seen as the month with the least sales')
            #result,fig=annual_sales_performance_by_categories()
            #st.plotly_chart(fig)
        elif graph=='Quarterly Sales':
            visual_display=st.radio('Display Type',('Bar','Line','Tabular'),horizontal=True)

            #graph_type=st.radio('Graph Type',('Bar','Line'),horizontal =True)
            
            result=quarterly_sales_performance(visual_display)
            if visual_display=='Tabular':
               
                st.dataframe(result,use_container_width=True)
            elif visual_display=='Bar' or visual_display=='Line':
                st.plotly_chart(result)
        elif graph=='Annual Sales':
            visual_display=st.radio('Display Type',('Bar','Line','Tabular'),horizontal=True)
            result,fig=annual_sales_performance_by_categories()
            if visual_display=='Line':
                st.plotly_chart(fig)
            elif visual_display=='Tabular':
                st.write('Annual Sales By Categories')
                st.dataframe(result,use_container_width=True)
            elif visual_display=='Bar':
                pass
        elif graph=='Weekly Sales':
            result,fig=weekly_performance()
            visual_display=st.radio('Display Type',('Bar','Line','Tabular'),horizontal=True)
            if visual_display=='Tabular':
                st.write('Weekly Sales Performance')
                cols=['Week','Order_Month','Order_Year','Sales']
                st.dataframe(result[cols],use_container_width=True)
            elif visual_display=='Line':
                st.plotly_chart(fig)
                
    with tab4: 
        #month over month performance
        result,fig=month_over_month_sales()
        visual_display=st.radio('Display Type',('Line','Tabular'),horizontal=True)
        if visual_display=='Line':
            #display graph for month over month using plotly chart
            st.plotly_chart(fig)
        elif visual_display=='Tabular':
            #display data for month over month in tabular form using st.dataframe
            cols=['Order_Year','Order_Month','Sales','Previous_Month']
            
            st.dataframe(result,use_container_width=True)
    with tab2:
        
        st.markdown("""""")
        #with st.expander("See narations"):
        #st.write('December is the month with most sales as February is seen as the month with the least sales')
        graph_type1=st.radio('Graph Type',('Trend','Sales','Profit','Sales And Profit Per Market'),horizontal =True)
        result,fig=percentage_changes(graph_type1)
        st.plotly_chart(fig)
    with tab3:
        num_display=st.text_input('Enter number to display',placeholder='Enter number of entries here')
        if num_display=='':
            pass
        else:
            num_display=int(num_display)
            result,fig=customer_distribution_by_country(num_display)
            visual_display=st.radio('Display Type',('Map','Tabular'),horizontal=True)
            
            if visual_display=='Map':
                st.plotly_chart(fig)
            elif visual_display=='Tabular':
              
                st.dataframe(result,use_container_width=True)
    with tab5:
        #graph_type1=st.radio('Graph Type',('Trend','Sales','Profit','Sales And Profit Per Market'),horizontal =True)
        #result,fig=percentage_changes(graph_type1)
        #st.plotly_chart(fig)
        pass


with st.expander("Average Shipping Cost Per Region"):      
    result,fig=average_shipping_cost_per_region()
    st.plotly_chart(fig)


with st.expander("Product Categories to be targetted to the different markets'"):  
    result,fig=products_market_target()
    st.plotly_chart(fig)
