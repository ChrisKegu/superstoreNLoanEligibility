import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import os
#import a list of colours from util class
from classes.util import colour_list

pd.options.display.float_format = '{:,.2f}'.format

#reading csv file
path=os.path.join('classes','processed_super_store.csv')
#print(os.listdir())
#print(path)
#print('%%%%%%%%%%%%%%% preparing to read %%%%%%%%%%%%%%%%')
data = pd.read_csv(path,encoding = 'latin1')

#What is the sales and profit per market?
def sales_and_profit_per_market():

    result = data[['Market','Sales','Profit']].pivot_table(index=['Market'], \
                         aggfunc='sum').sort_values(by='Sales',ascending=True)
    result=result.reset_index()
    fig = go.Figure(data=[
    go.Bar(name='Sales', x=result['Market'], y=result['Sales'],
          # text=round(pivot['Sales'],2)
          )
    ,
    go.Bar(name='Profit', x=result['Market'], y=result['Profit'],
           #text=round(pivot['Profit'],2)
          )
    ])
    fig.update_layout(barmode='group',
                  title="Sales And Profit Per Market")

    return fig


#What is the most and least profitable market?
def monthly_sales_performance():

    result = data.pivot_table(index=['Order_Month'], \
                         values=['Sales'],\
                         aggfunc='sum')

    result=result.reset_index().sort_values(by='Sales',ascending=False)

    fig = px.pie(result, values='Sales', names='Order_Month',
             title='Monthly Sales Performances',
             hover_data=['Sales'], 
             labels={'Order_Month':'Month','Sales':'Sales'},hole=.4)
    fig.update_traces(textposition='inside', textinfo='percent+label',
                 )
    fig.update_layout(showlegend=False)
    return fig
#method to return dominant product category in each market
#and a plotly graph object
def dominant_product_category_in_each_market():
    result = data.pivot_table(index=['Category','Market'], \
                         values=['Count'],\
                         aggfunc='count')

    result=result.reset_index().sort_values(by='Count', ascending=False)
    fig = px.line(result, x="Category", y="Count", 
              title='Dominant Product Category in Each Market',
              color='Market',
              markers=True,
              labels={'Count':'Quantity Sold'},
              #text='Count'
             )
    #fig.update_layout(showlegend=False)
    return result,fig

def products_making_losses(n):
    result=data[['Product_Name','Profit']][data['Profit']<0]
    result=result.sort_values(by='Profit',ascending=True).head(n)
    fig = go.Figure(data=[
    go.Bar(name='Products making loss', 
           x=result['Product_Name'], y=result['Profit'],
           #text=round(loss['Profit'],2)
          )
        ])
    fig.update_layout(barmode='group',
                  title=f"Top {n} Products Making Losses")
    
    
    return result, fig

def profit_by_segment():
    result = data.pivot_table(index=['Segment'], \
                         values=['Profit_Margin','Profit'],\
                         aggfunc='sum')

    result=result.reset_index().sort_values(by='Profit_Margin', 
    ascending=False)
    fig = go.Figure(data=[
    go.Bar(name='Profit', x=result['Segment'], y=result['Profit'],
           #text=round(pivot['Profit'],2)
          ),
   
    go.Bar(name='Profit Margin', x=result['Segment'], y=result['Profit_Margin'],
           #text=round(pivot['Profit_Margin'],2)
          )
    ])
    # Change the bar mode
    fig.update_layout(barmode='group',
                  title="Profit And Profit Margin By Segments")
    return result, fig

def sales_by_order_priority():
    result = data.pivot_table(index=['Order_Priority'], \
                         values=['Sales'],\
                         aggfunc='sum')

    result=result.reset_index().sort_values(by='Sales', ascending=False)
    fig = go.Figure(data=[
    go.Bar(name='Profit', x=result['Order_Priority'], y=result['Sales'],
           #text=round(pivot['Sales'],2)
          )
    ])

    fig.update_layout(barmode='group',title="Sales By Order Priority"
    )
    fig
    return result, fig

def average_shipping_cost_per_region():
    result=data[['Region','Shipping_Cost']].groupby('Region')\
    .mean().sort_values(by='Shipping_Cost',ascending=False)
    result.reset_index(inplace=True)

    colour_list=["orange", "green",'Maroon', "blue", "purple",'Salmon',
             'indigo','Olive','Turquoise', "red",'thistle',
             'springgreen','yellow']

    fig = px.bar(result, x='Region', y='Shipping_Cost',
             hover_data=['Region', 'Shipping_Cost'], 
             color='Region',
             labels={'Shipping_Cost':'Average Shipping Cost'}, 
             height=400,
             #text_auto='.4s',
              color_discrete_sequence=colour_list,
             #title='Average Shipping Cost Per Region'
             )#text_auto=True)

    fig.update_layout(showlegend=False)
    return result,fig

def products_market_target():
    result=data.pivot_table(data[['Count']],\
                            index=['Market','Category'], aggfunc='count')
    result=result.reset_index().head(10)
    result=result.sort_values(by='Count',ascending=False)
    fig = px.line(result, x="Category", y="Count", 
              #title='Product Categories to be targetted to the different markets',
              color='Market',markers=True,
              labels={'Count':'Quantity Sold'},
              #text='Count'
             )
    return result, fig

def annual_sales_performance_by_categories():       
#Annual sales performance by categories
    result=data[['Order_Year','Category','Sales']].groupby(['Order_Year','Category']).sum()\
.sort_values(by='Sales',ascending=False).head(10) 
    result=result.reset_index()
    fig = px.line(result, x="Category", y="Sales",
              #title='Annual Product Sales Per Category',
              color='Order_Year',
              markers=True,
              labels={'Sales':'Sales Made in Millions',
                      'Order_Year':'Order Year'})
    return result,fig
def most_profitable_products_per_region(n):


    result=data[['Product_Name','Region','Profit_Margin','Profit']].groupby(['Region','Product_Name']).sum()\
    .sort_values(by=['Profit_Margin'],ascending=False)
    result.reset_index(inplace=True) 
    #result=result.head(n)
    fig = px.bar(result.head(n), x='Product_Name', y='Profit_Margin',
             hover_data=['Product_Name', 'Profit_Margin'],color='Region', 
             
             #height=400,
             #text_auto='.4s',
             labels={'Product_Name':'Product','Profit_Margin':'Profit Margin'},
             title=f'Top {n} Most Profitable Products vr Region')
    fig.update_xaxes(tickangle=90,tickfont=dict(family='Rockwell', 
                                            #color='grey', 
                                            size=14))

    result,fig

#quarterly sales performance
def quarterly_sales_performance(graph_type):

    result=data[['Order_Year','Sales','Quarter_Ordered']]\
    .groupby(['Order_Year','Quarter_Ordered']).sum()\
    .sort_values(by=['Order_Year'],ascending=True)
    result.reset_index(inplace=True)
    if graph_type=='Bar':
        fig = px.bar(result, x='Quarter_Ordered', y='Sales',
             hover_data=['Order_Year', 'Quarter_Ordered'], 
             color='Order_Year',
             labels={'Order_Year':'Year','Quarter_Ordered':'Quarter'}, 
             height=400,#text_auto='.4s',
             title='Qurterly Sales Performance')
        return fig
            
    elif graph_type=='Line':
        fig = px.line(result, x="Quarter_Ordered", y="Sales", title='Quarterly Sales Performance',
              color='Order_Year',markers=True,
              labels={'Quarter_Ordered':'Quarter'})
        return fig
    elif graph_type=='Tabular':
        return result
    #return result,fig

def percentage_changes(graph_type):
    result=data[['Order_Year','Month_Number','Order_Month','Sales','Profit']]\
    .groupby(['Order_Year','Month_Number','Order_Month']).sum()\
    .sort_values(by=['Order_Year','Month_Number'],ascending=True)
    result.reset_index(inplace=True)

    result['%Change in Sales']=result['Sales'].pct_change()*100
    result['%Change in Profit']=result['Profit'].pct_change()*100
    result.fillna(0,inplace=True)
    if graph_type=='Trend':
        fig = px.line(result, x="Order_Month", y="%Change in Sales", 
              title='% Change in Sales ',
              color='Order_Year',
              markers=True,
              labels={'Order_Month':'Month','Order_Year':'Year'})
    elif graph_type=='Sales':
        fig = px.bar(result, x='Order_Month', y='%Change in Sales',
             hover_data=['Order_Month', '%Change in Sales'],color='Order_Year', 
             
             #height=400,
             #text_auto='.4s',
             labels={'Order_Month':'Month','Order_Year':'Year'},
             title='% Change in Sales')
        fig.update_xaxes(tickangle=90,tickfont=dict(family='Rockwell', 
                                            color='grey', size=14))
    elif graph_type=='Profit':
        fig = px.bar(result, x='Order_Month', y='%Change in Profit',
             hover_data=['Order_Month', '%Change in Profit'],
             color='Order_Year', 
             
             #height=400,
             #text_auto='.4s',
             labels={'Order_Month':'Month','Order_Year':'Year'},
             title='% Change in Profit')
        fig.update_xaxes(tickangle=90,tickfont=dict(family='Rockwell', 
                                            color='grey', size=14))
    elif graph_type=='Sales And Profit Per Market':
        fig = go.Figure(data=[
        go.Bar(name='Sales', x=result['Order_Month'], y=result['%Change in Sales'],
          # text=round(pivot['Sales'],2)
          )
        ,
        go.Bar(name='Profit', x=result['Order_Month'], y=result['%Change in Profit'],
           #text=round(pivot['Profit'],2)
          )
        ])
        fig.update_layout(barmode='group',
                  title="% Changes in  Sales And Profit Per Month")
    return result,fig
#get weekly sales performances
def weekly_performance():
    result=data[['Week','Sales','Order_Year','Order_Month','Month_Number']].\
    pivot_table(index=['Week','Order_Year','Order_Month','Month_Number'],
                                   values=['Sales'],
                                   aggfunc='sum')

    result.reset_index(inplace=True)
    result.sort_values(by=['Order_Year','Month_Number','Week'],ascending=True)

    fig = px.line(result, x="Week", y="Sales", 
              title='Weekly Sales Performance',
              color='Order_Year',
              markers=True,
              labels={'Order_Month':'Month','Order_Year':'Year'},
              hover_data={'Order_Month'},
              color_discrete_sequence=colour_list
             )
    return result,fig 

#customer distribution by country
def customer_distribution_by_country(n):

    result=data[['Country','Sales','Profit','Count']].pivot_table(index=['Country'],
                                        values=['Count','Sales','Profit'],
                                        aggfunc='sum').\
    sort_values(by='Count', ascending=False)
    result.reset_index(inplace=True)
    result=result.head(n)
    country_map = dict(type='choropleth',
           locations=result['Country'],
           locationmode='country names',
           z=result['Sales'],
           reversescale = True,
           text=result['Country'],
           colorscale='earth',
           colorbar={'title':'Number of Customers'})
    layout = dict(title='Customer Distribution over Countries',
             geo=dict(showframe=False,projection={'type':'mercator'}))
    fig = go.Figure(data = [country_map],layout = layout)
    return result,fig

def month_over_month_sales():
    #same period last month/ month over month/month on month
    result=data[['Order_Year','Month_Number','Order_Month','Sales']].groupby(['Order_Year','Month_Number','Order_Month']).sum()\
    .sort_values(by=['Order_Year','Month_Number'],ascending=True)
    result.reset_index(inplace=True)
    result['Previous_Month']=result['Sales'].shift(1)
    result['Difference']=result['Sales']-result['Previous_Month']
    result=result.fillna(0)
    

    fig = px.line(result, x="Order_Month", y="Sales", title='Year On Year Sales Performance',
              color='Order_Year',markers=True,labels={'Order_Month':'Month'})
    return result, fig



