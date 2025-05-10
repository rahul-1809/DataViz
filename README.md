# 📊 Sales Data Dashboard

An interactive Streamlit dashboard for visualizing sales, profit, and ratings data across countries, regions, and time periods using `Plotly Express`.

## 🔍 Overview

This dashboard helps in understanding key business metrics like:

* **Sales trends over time and geography**
* **Yearly profit distribution**
* **Average ratings per country**
* **Customizable scatter plots and 3D plots**
* **Region-wise performance**

Built using:

* **Streamlit**
* **Plotly Express**
* **Pandas**

## 📁 Dataset

The app uses a preprocessed CSV file named `preprocessed_dataset1.csv`. It should include (but is not limited to) columns like:

* `Country`
* `Year`
* `Sales`
* `Profit`
* `ratings`
* `Region`
* Other numerical/ categorical fields for user-selectable visualizations

## 📸 Visualizations

* **Choropleth Map**: Animated map showing sales across countries over time
* **Pie Chart**: Year-wise profit distribution
* **Bar Chart**: Average ratings by country
* **Scatter Plot**: Customizable XY plot
* **3D Plot**: Selectable 3D scatter plot
* **Box Plot**: Distribution of values across categories
* **Region Bar Plot**: Sales by region
* **Product Rating Bar**: Rating distribution for selected product column

## 🚀 Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/rahul-1809/DataViz.git
   cd DataViz
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your `preprocessed_dataset1.csv` in the root directory.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## 📦 Requirements

Create a `requirements.txt` using:

```txt
streamlit
pandas
plotly
```
