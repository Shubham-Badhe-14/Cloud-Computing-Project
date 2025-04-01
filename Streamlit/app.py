import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.title("Data Engineering & Analytics Insights App")
st.markdown("By Shubham Badhe (2026)")


# File Upload Section
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Load Data with Encoding Handling
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        except UnicodeDecodeError:
            df = pd.read_csv(uploaded_file, encoding="latin1")
    
    st.success("CSV file loaded successfully!")
    
    # Display Dataset Preview and Basic Info
    st.subheader("Dataset Preview")
    st.write(df.head())
    
    st.subheader("Basic Data Information")
    st.write(df.describe(include='all'))
    
    missing_values = df.isnull().sum()
    st.subheader("Missing Values in Dataset")
    st.write(missing_values[missing_values > 0])
    
    # Attempt to convert any column named 'date' to datetime
    if 'date' in df.columns:
        try:
            df['date'] = pd.to_datetime(df['date'])
        except Exception as e:
            st.error("Error converting 'date' column: " + str(e))
    
    # Visualization Options Dropdown
    st.subheader("Choose a Visualization")
    viz_options = [
        "Sales Trend Over Time (Line Chart)",
        "Best-Selling Products (Bar Chart)",
        "Price Distribution (Histogram)",
        "Regional Sales Performance (Bar Chart)",
        "Correlation Heatmap",
        "Custom: Histogram (Numeric Column)",
        "Custom: Scatter Plot (Numeric Columns)",
        "Custom: Categorical Distribution (Bar Chart)"
    ]
    viz_choice = st.selectbox("Select Visualization Type", viz_options)
    
    # Render visualization based on selection
    if viz_choice == "Sales Trend Over Time (Line Chart)":
        # Let user choose x-axis (date) and y-axis (sales)
        date_cols = [col for col in df.columns if "date" in col.lower() or pd.api.types.is_datetime64_any_dtype(df[col])]
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if not date_cols:
            st.info("No date columns found. Please select a column to convert to datetime.")
            date_cols = list(df.columns)
        if not num_cols:
            st.error("No numeric columns found for sales data.")
        else:
            x_axis = st.selectbox("Select X-axis (Date)", date_cols)
            y_axis = st.selectbox("Select Y-axis (Sales)", num_cols)
            try:
                df[x_axis] = pd.to_datetime(df[x_axis])
            except Exception as e:
                st.error(f"Could not convert {x_axis} to datetime. {e}")
            st.subheader("Sales Trend Over Time (Line Chart)")
            fig = px.line(df, x=x_axis, y=y_axis, title="Sales Trend Over Time")
            st.plotly_chart(fig)
    
    elif viz_choice == "Best-Selling Products (Bar Chart)":
        # Let user choose a categorical column (product) and numeric (sales)
        cat_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col])]
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if not cat_cols:
            st.error("No categorical columns found for product names.")
        elif not num_cols:
            st.error("No numeric columns found for sales data.")
        else:
            cat_choice = st.selectbox("Select Product Column", cat_cols)
            num_choice = st.selectbox("Select Sales Column", num_cols)
            st.subheader("Best-Selling Products (Bar Chart)")
            top_products = df.groupby(cat_choice)[num_choice].sum().nlargest(10)
            fig = px.bar(x=top_products.index, y=top_products.values, title="Top 10 Best-Selling Products")
            st.plotly_chart(fig)
    
    elif viz_choice == "Price Distribution (Histogram)":
        # Let user choose a numeric column for histogram
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if not num_cols:
            st.error("No numeric columns available for histogram.")
        else:
            col_choice = st.selectbox("Select Numeric Column", num_cols)
            st.subheader("Price Distribution (Histogram)")
            fig, ax = plt.subplots()
            sns.histplot(df[col_choice], bins=20, kde=True, ax=ax)
            st.pyplot(fig)
    
    elif viz_choice == "Regional Sales Performance (Bar Chart)":
        # Let user choose categorical (region) and numeric (sales)
        cat_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col])]
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if not cat_cols:
            st.error("No categorical columns available for regions.")
        elif not num_cols:
            st.error("No numeric columns available for sales data.")
        else:
            region_choice = st.selectbox("Select Region Column", cat_cols)
            sales_choice = st.selectbox("Select Sales Column", num_cols)
            st.subheader("Regional Sales Performance (Bar Chart)")
            region_sales = df.groupby(region_choice)[sales_choice].sum().reset_index()
            fig = px.bar(region_sales, x=region_choice, y=sales_choice, title="Regional Sales Performance")
            st.plotly_chart(fig)
    
    elif viz_choice == "Correlation Heatmap":
        # Only if at least 3 numeric columns
        numeric_cols = df.select_dtypes(include=['number'])
        if len(numeric_cols.columns) < 3:
            st.error("Not enough numeric columns for a meaningful correlation heatmap (requires at least 3).")
        else:
            st.subheader("Correlation Heatmap")
            fig, ax = plt.subplots()
            sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
    
    elif viz_choice == "Custom: Histogram (Numeric Column)":
        # Let user choose any numeric column for a histogram
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if not num_cols:
            st.error("No numeric columns available for histogram.")
        else:
            col_choice = st.selectbox("Select Numeric Column for Histogram", num_cols)
            st.subheader(f"Histogram for {col_choice}")
            fig, ax = plt.subplots()
            sns.histplot(df[col_choice], bins=20, kde=True, ax=ax)
            st.pyplot(fig)
    
    elif viz_choice == "Custom: Scatter Plot (Numeric Columns)":
        # Let user choose two numeric columns for a scatter plot
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        if len(num_cols) < 2:
            st.error("Need at least two numeric columns for a scatter plot.")
        else:
            x_col = st.selectbox("Select X-axis Column for Scatter Plot", num_cols, key="scatter_x")
            y_col = st.selectbox("Select Y-axis Column for Scatter Plot", num_cols, key="scatter_y")
            st.subheader(f"Scatter Plot: {x_col} vs {y_col}")
            fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot: {x_col} vs {y_col}")
            st.plotly_chart(fig)
    
    elif viz_choice == "Custom: Categorical Distribution (Bar Chart)":
        # Let user choose a categorical column for a bar chart of value counts
        cat_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col])]
        if not cat_cols:
            st.error("No categorical columns available for bar chart.")
        else:
            cat_choice = st.selectbox("Select Categorical Column", cat_cols)
            st.subheader(f"Distribution of {cat_choice}")
            count_data = df[cat_choice].value_counts().reset_index()
            count_data.columns = [cat_choice, "Count"]
            fig = px.bar(count_data, x=cat_choice, y="Count", title=f"Distribution of {cat_choice}")
            st.plotly_chart(fig)
else:
    st.warning("Please upload a CSV file to begin analysis.")
