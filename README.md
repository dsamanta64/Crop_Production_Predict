# Crop Production Prediction Using Machine Learning

## Overview

Welcome to the Crop Production Prediction project! Our objective is to deliver accurate crop production forecasts using advanced machine learning techniques.

## Dataset Overview

The dataset used for this project includes comprehensive agricultural data from various states across India, spanning from 1997 to 2020. It provides crucial features necessary for predicting crop yield, covering different crop types, cultivation years, cropping seasons, and several environmental and agricultural factors.

### Columns Description

**Input Features:**

- **Crop:** The specific type of crop being cultivated.
- **Crop_Year:** The year in which the crop was grown.
- **Season:** The cropping season during which the crop was planted, such as Kharif, Rabi, or Whole Year.
- **State:** The Indian state where the crop was cultivated.
- **Area:** The total land area (in hectares) dedicated to the cultivation of the crop.
- **Annual_Rainfall:** The total annual rainfall received in the region where the crop was grown (in millimeters).
- **Fertilizer:** The total amount of fertilizer applied to the crop (in kilograms).
- **Pesticide:** The total amount of pesticide used on the crop (in kilograms).

**Output Feature:**

- **Production:** The resulting quantity of crop production (in metric tons).

## Machine Learning Model

We use the RandomForest Regressor to predict crop production, a robust machine learning model known for its accuracy and ability to handle complex datasets. Our model has achieved an impressive R² score of 98%, reflecting its high predictive accuracy and effectiveness.

By training our model on this diverse dataset, we aim to provide reliable predictions that can help farmers, agricultural planners, and policymakers make informed decisions.

Our predictive model takes into account various factors such as crop type, cultivation area, seasonal patterns, and environmental conditions to generate accurate forecasts of crop production. We are committed to leveraging data-driven insights to support sustainable agricultural practices and enhance productivity.

## Getting Started

<li><strong>To get started with this project, follow the steps:</strong></li> 
    
<ol>
            <li> Clone the repository:<br><br> 
git clone https://github.com/dsamanta64/Crop_Production_Predict.git</li><br>
            <li> Change to the project directory:<br><br>
cd Crop_Production_Predict</li><br>
            <li> Install the required Python packages:<br><br>
pip install -r requirements.txt</li><br>
            <li> Start the development server:<br><br>
python app.py</li><br>
            <li> Access the portal in your web browser at <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li><br>
        </ol><br>

Thank you for checking out our Crop Production Prediction project! We hope you find our model and insights valuable for your agricultural needs.
