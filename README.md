<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Startup Funding Analysis</title>
</head>

<body>
    <h1>📊 Startup Funding Analysis</h1>

    <p>Welcome to the <strong>Startup Funding Analysis</strong> project! This project provides a comprehensive analysis
        of startup funding patterns in India, leveraging data visualization techniques to uncover insights about
        investment trends, top investors, funding stages, and more. The analysis is built using <strong>Streamlit</strong>
        and <strong>Plotly</strong>, making it interactive and user-friendly.</p>

    <h2>🚀 Overview</h2>

    <p>This project is designed to help users understand various aspects of startup funding in India, including:</p>
    <ul>
        <li><strong>Funding Amounts by Month/Year</strong>: Visualizing the total and count of funding amounts over time.</li>
        <li><strong>Funding Types</strong>: Analyzing the different types of funding (e.g., Seed, Series A, Series B).</li>
        <li><strong>City-wise Funding</strong>: Understanding which cities attract the most funding.</li>
        <li><strong>Top Startups and Investors</strong>: Identifying the top-funded startups and most active investors.</li>
        <li><strong>Sector Analysis</strong>: Breaking down funding by sector to see which industries are attracting the most investment.</li>
        <li><strong>Interactive Heatmaps</strong>: Visualizing funding distribution across different months and years.</li>
        <li><strong>Investor-Specific Insights</strong>: Drilling down into specific investors to see their biggest investments, sectors of interest, and year-on-year funding trends.</li>
        <li><strong>Similar Companies</strong>: Displaying startups that are similar in terms of industry or investment.</li>
    </ul>

    <h2>🔍 Exploratory Data Analysis (EDA) and Feature Engineering</h2>

    <p>Before diving into the visualizations, we performed <strong>Exploratory Data Analysis (EDA)</strong> and
        <strong>Feature Engineering</strong> on the dataset. This process included:</p>
    <ul>
        <li>Cleaning and preprocessing the data.</li>
        <li>Handling missing values.</li>
        <li>Extracting key features like funding type, city, and investor information.</li>
        <li>Creating new features for enhanced analysis.</li>
    </ul>

    <h2>📈 Visualizations</h2>

    <p>The project utilizes <strong>Plotly</strong> for dynamic and interactive visualizations, providing a more engaging
        experience for users. Some of the key visualizations include:</p>
    <ul>
        <li><strong>Line Charts</strong>: For month-on-month and year-on-year analysis of funding amounts.</li>
        <li><strong>Bar Charts</strong>: For city-wise funding distribution and top startups/investors.</li>
        <li><strong>Pie Charts</strong>: For sector-wise investment breakdown and funding stage analysis.</li>
        <li><strong>Heatmaps</strong>: To visualize funding intensity over time.</li>
    </ul>

    <h2>🌟 Features</h2>

    <ul>
        <li><strong>Interactive User Interface</strong>: Built using <strong>Streamlit</strong>, making the analysis easy to use and navigate.</li>
        <li><strong>Filter Options</strong>: Allow users to filter data by various parameters, such as funding type, investor, city, and stage.</li>
        <li><strong>Detailed Insights</strong>: Provides a deep dive into each investor's portfolio, including sectors invested in, biggest investments, and more.</li>
        <li><strong>Similar Companies Analysis</strong>: Displays companies that are similar to a selected startup based on industry and funding characteristics.</li>
    </ul>

    <h2>🛠️ How to Use</h2>

    <ol>
        <li>
            <strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/your-username/startup-funding-analysis.git<br>cd startup-funding-analysis</code></pre>
        </li>
        <li>
            <strong>Install the Required Packages:</strong>
            <p>Ensure you have Python installed. Install the necessary packages using pip:</p>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>
            <strong>Run the Streamlit App:</strong>
            <pre><code>streamlit run app.py</code></pre>
        </li>
        <li>
            <strong>Explore the Dashboard:</strong>
            <p>Open the provided URL in your browser to explore the interactive dashboard and gain valuable insights into startup funding trends.</p>
        </li>
    </ol>

    <h2>📊 Sample Visuals</h2>

    <p>Here are some sample visuals from the app:</p>
    <ul>
        <li><strong>Month-on-Month Analysis:</strong> <img src="images/mom_analysis.png" alt="MoM Analysis"></li>
        <li><strong>Funding Heatmap:</strong> <img src="images/funding_heatmap.png" alt="Funding Heatmap"></li>
        <li><strong>Top Startups:</strong> <img src="images/top_startups.png" alt="Top Startups"></li>
        <li><strong>Sector Analysis:</strong> <img src="images/sector_analysis.png" alt="Sector Analysis"></li>
    </ul>

    <p><em>(Make sure to include sample images in the <code>/images</code> directory for visualization in your README.)</em></p>

    <h2>🌐 Deployed Version</h2>

    <p>The app is deployed on <strong>Streamlit</strong>! You can check out the live version and explore the analysis on
        your own: <a href="https://your-streamlit-app-link">Streamlit App</a>.</p>

    <h2>📚 Resources</h2>

    <ul>
        <li><strong>Kaggle Notebook</strong>: For a more in-depth look at the data analysis, check out the <a href="https://www.kaggle.com/your-kaggle-notebook-link">Kaggle Notebook</a>.</li>
        <li><strong>GitHub Repository</strong>: Visit the <a href="https://github.com/your-github-repo-link">GitHub Repository</a> for the complete codebase.</li>
    </ul>

    <h2>🤝 Contributing</h2>

    <p>We welcome contributions! If you have any suggestions, bug reports, or feature requests, please open an issue or
        submit a pull request.</p>

    <h2>📄 License</h2>

    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

    <h2>🙏 Acknowledgments</h2>

    <p>A big thank you to the data science community for their support and resources. Special thanks to the providers of
        the dataset and all contributors who helped make this project a reality.</p>

    <hr>

    <p><strong>Happy Learning! 😊</strong></p>
</body>

</html>
