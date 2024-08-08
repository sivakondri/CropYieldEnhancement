<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crop Yield Enhancement</title>
</head>
<body>
    <h1>Crop Yield Enhancement</h1>

    <h2>Project Overview</h2>
    <p>The "Crop Yield Enhancement" project helps farmers maximize crop yields by recommending the best crops to plant based on soil and environmental conditions. The model, built using decision trees, suggests optimal crops and provides planting strategies to enhance productivity.</p>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Languages:</strong> Python</li>
        <li><strong>Framework:</strong> Flask</li>
        <li><strong>Libraries:</strong> scikit-learn, pandas, numpy</li>
        <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
    </ul>

    <h2>Model Development</h2>
    <h3>Algorithms Used</h3>
    <ul>
        <li>Logistic Regression</li>
        <li>K-Nearest Neighbors (KNN)</li>
        <li>Random Forest</li>
        <li>Decision Trees</li>
    </ul>

    <h3>Parameters</h3>
    <ul>
        <li>Nitrogen (N)</li>
        <li>Phosphorus (P)</li>
        <li>Potassium (K)</li>
        <li>Temperature</li>
        <li>Humidity</li>
        <li>Rainfall</li>
        <li>Soil pH</li>
    </ul>

    <h3>Model Selection</h3>
    <p>Decision Trees were chosen for their high accuracy.</p>

    <h2>Planting Strategies</h2>
    <p>For each recommended crop, we provide strategies on:</p>
    <ul>
        <li>Seed spacing</li>
    </ul>

    <h2>Flask Deployment</h2>
    <p>A Flask web application allows users to input soil and environmental data to get crop recommendations and planting strategies.</p>
    <p>Deployment: <a href="https://sivamsiva.pythonanywhere.com/" target="_blank">https://sivamsiva.pythonanywhere.com/</a></p>

    <h2>Installation and Setup</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/your-username/crop-yield-enhancement.git
cd crop-yield-enhancement</code></pre>
        </li>
        <li><strong>Install dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Set up the database (if using SQLite):</strong>
            <pre><code>python setup_db.py</code></pre>
        </li>
        <li><strong>Run the Flask application:</strong>
            <pre><code>python app.py</code></pre>
        </li>
        <li><strong>Access the application:</strong>
            <p>Open your browser and go to <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>.</p>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Navigate to the home page.</li>
        <li>Enter soil and environmental parameters.</li>
        <li>Submit to get crop recommendations and planting strategies.</li>
    </ol>

    <h2>Contributing</h2>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch:
            <pre><code>git checkout -b feature-name</code></pre>
        </li>
        <li>Commit changes:
            <pre><code>git commit -m 'Add feature'</code></pre>
        </li>
        <li>Push to the branch:
            <pre><code>git push origin feature-name</code></pre>
        </li>
        <li>Open a pull request.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>

</body>
</html>
