import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("preprocessed_dataset1.csv")

df_sample = df.sample(frac=0.2)

fig_choropleth = px.choropleth(
    df_sample,
    locations='Country',
    locationmode='country names',
    color='Sales',
    hover_name='Country',
    color_continuous_scale='Viridis',
    title='Sales by Country',
    animation_frame='Year'
)

fig_choropleth.update_layout(
    geo=dict(
        showcoastlines=True,
        projection_scale=20,
        visible=False
    ),
    height=600,
    width=800
)

yearly_profit = df.groupby('Year')['Profit'].sum().reset_index()

fig_pie = px.pie(
    yearly_profit,
    values='Profit',
    names='Year',
    title='Yearly Profit Distribution'
)

avg1, avg2 =  st.columns(2)
with avg1:
         average_value = df["Sales"].mean()
         st.subheader(f"Average sales")
         st.markdown(f"<div style='font-size:35px; background-color: pink; padding: 20px;  display:inline-block; color:black; font-weight: bold;  border-radius: 10px;'>{average_value:.2f}</div>", unsafe_allow_html=True)

with avg2:
         average_value = df["Profit"].mean()
         st.subheader(f"Average sales")
         st.markdown(f"<div style='font-size:35px; background-color: pink; padding: 20px;  display:inline-block; color:black; font-weight: bold;  border-radius: 10px;'>{average_value:.2f}</div>", unsafe_allow_html=True)

average_rating_by_country = df.groupby("Country")["ratings"].mean().reset_index()

st.title("Average Ratings by Country")

fig = px.bar(average_rating_by_country, x="Country", y="ratings", title="Average Ratings by Country", labels={"Rating": "Average Rating"})
fig.update_layout(width=1500)
st.plotly_chart(fig)


     
col1, col2  = st.columns(2)

with col1:
    st.subheader("Choropleth Map: Sales by Country Over Time")
    st.plotly_chart(fig_choropleth)

with col2:
    st.subheader("Pie Chart: Yearly Profit Distribution")
    st.plotly_chart(fig_pie)

col3, col4=st.columns(2)

with col3:
    st.subheader("Scatter Plot: Relationship between X and Y")
    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column = st.selectbox("Select Y-axis column", df.columns)
    fig_scatter = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"Scatter Plot: {x_column} vs {y_column}",
        labels={'x': x_column, 'y': y_column}
    )
    st.plotly_chart(fig_scatter)

with col4:
    st.subheader("Bar Plot: Regions and Sales")
    fig_bar = px.bar(df, x='Region', y='Sales', title='Bar Plot for Regions and Sales')
    st.plotly_chart(fig_bar)

st.subheader("3D Surface Plot: X, Y, Z")
x_surface_column = st.selectbox("Select X-axis column for Surface Plot", df.columns)
y_surface_column = st.selectbox("Select Y-axis column for Surface Plot", df.columns)
z_surface_column = st.selectbox("Select Z-axis column for Surface Plot", df.columns)
fig_surface = px.scatter_3d(
    df,
    x=x_surface_column,
    y=y_surface_column,
    z=z_surface_column,
    title=f"3D Surface Plot: {x_surface_column}, {y_surface_column}, {z_surface_column}",
    labels={'x': x_surface_column, 'y': y_surface_column, 'z': z_surface_column}
)
st.plotly_chart(fig_surface)

st.subheader("Box Plot and Bar Graph")
x_column_box = st.selectbox("Select X-axis column for Box Plot", df.columns, key='x_column_box')
y_column_box = st.selectbox("Select Y-axis column for Box Plot", df.columns, key='y_column_box')
fig_box = px.box(df, x=x_column_box, y=y_column_box)
st.plotly_chart(fig_box)

product_column = st.selectbox("Select Product column for Bar Graph", df.columns, key='product_column')
rating_column = st.selectbox("Select Rating column for Bar Graph", df.columns, key='rating_column')
fig_bar_product = px.bar(df, x=product_column, y=rating_column, title="Product Ratings Bar Graph")
st.plotly_chart(fig_bar_product)
