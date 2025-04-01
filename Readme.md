# Cloud Computing Course Project - 6th Semester Engineering

This repository contains two separate projects developed as part of the Cloud Computing course in my 6th Semester of Engineering:

### Frontend: Pomodoro Tracker (Next.js application)
A productivity timer application implementing the Pomodoro Technique with customizable work/break sessions.

#### Key Features:
- Interactive countdown timer with circular progress visualization
- Start/Pause/Reset functionality
- Customizable session durations
- Responsive design with Tailwind CSS

### Streamlit: Data Insights App (Streamlit application)
A data visualization application built with Streamlit to analyze datasets, providing various insights and visualizations.

#### Key Features:
- Upload CSV files and visualize data with multiple graph options
- Sales Trend Over Time (Line Chart)
- Best-Selling Products (Bar Chart)
- Price Distribution (Histogram)
- Regional Sales Performance (Bar Chart)
- Correlation Heatmap
- Custom Visualizations (Histogram, Scatter Plot, and more)

---

## Project Structure

```
cloud-computing-project/
├── streamlit/
│   ├── app.py
│   └── datasets/
│       ├── sales_data.csv
│       └── products_data.csv
│
├── frontend/
│   ├── .next
│   ├── app
│   │   ├── components
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.js
│   ├── node_modules
│   ├── public
│   ├── .gitignore
│   ├── next-env.d.ts
│   ├── next.config.ts
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.mjs
│   └── README.md
│
└── README.md
```

---

## Technologies Used

### Frontend
- **Next.js 13+**, **React**, **Tailwind CSS**, **JavaScript**

### Streamlit
- **Streamlit**, **Python**, **Pandas**, **Plotly**, **Matplotlib**, **Seaborn**

---

## Getting Started

### Frontend Setup

1. Navigate to the `frontend` folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

4. Access the app at: [http://localhost:3000](http://localhost:3000)

### Streamlit Setup

1. Navigate to the `streamlit` folder:

   ```bash
   cd streamlit
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Access the app at: [http://localhost:8501](http://localhost:8501)

---

## Key Learnings

Through this project, I gained practical experience with:

- Building responsive frontend applications with modern frameworks
- Designing data visualization applications
- Using APIs for data handling and analysis
- Application state management and deployment

---

## Future Enhancements

Potential improvements for both projects:

- **Frontend**: Add user authentication, task tracking, cloud deployment
- **Streamlit**: Integrate more data analysis functionalities, enhance visualizations, deploy to the cloud

---

## Course Relevance

This project helped demonstrate several cloud computing concepts:

- Client-server architecture
- API design and consumption
- Data analysis and visualization
- Potential for cloud deployment
