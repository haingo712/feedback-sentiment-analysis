# feedback-sentiment-analysis
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/haingo712/feedback-sentiment-analysis)

This repository contains a sentiment analysis model trained to classify feedback messages into positive, neutral, or negative categories. The model is served via a FastAPI-based REST API.

## Features

- **Sentiment Classification**: Categorizes text into `positive`, `neutral`, or `negative` sentiments.
- **REST API**: Provides an easy-to-use API endpoint for sentiment prediction.
- **Model Training**: Includes the script and dataset to train the Logistic Regression model from scratch.
- **Text Preprocessing**: Implements text cleaning and vectorization using `TfidfVectorizer`.

## Project Structure

```
.
├── app.py                  # FastAPI application for serving the model
├── dataset.training.csv    # The training dataset
├── handle_messages.py      # Text cleaning and preprocessing functions
├── requirements.txt        # Python project dependencies
├── sentiment_service.py    # Logic for model loading and prediction
├── train_model.py          # Script to train the sentiment analysis model
└── models/
    ├── logistic_regression.joblib  # The trained logistic regression model
    ├── model_features.csv          # Feature importance from the model
    └── vectorizer.joblib           # The trained TfidfVectorizer
```

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/haingo712/feedback-sentiment-analysis.git
    cd feedback-sentiment-analysis
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

You can retrain the model by running the `train_model.py` script. This will use the `dataset.training.csv` to create and save a new model and vectorizer in the `models/` directory.

```bash
python train_model.py
```

### Running the API Server

To start the API server, run the following command in the root directory:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

### Making Predictions

You can send a `POST` request to the `/predict-sentiment` endpoint with a list of messages to get their sentiment classification.

**Example using `curl`:**

```bash
curl -X 'POST' \
  'http://localhost:8000/predict-sentiment' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": [
    "Absolutely loved my stay here, everything was perfect!",
    "The stay was fine, not too bad but not great.",
    "Horrible experience, nothing worked as expected."
  ]
}'
```

**Example Response:**

```json
[
  {
    "message": "Absolutely loved my stay here, everything was perfect!",
    "label": "positive",
    "confidence": 98.61869894283832
  },
  {
    "message": "The stay was fine, not too bad but not great.",
    "label": "neutral",
    "confidence": 88.06653194098485
  },
  {
    "message": "Horrible experience, nothing worked as expected.",
    "label": "negative",
    "confidence": 97.43638058287515
  }
]
```

## API Endpoints

### `GET /`

-   **Description**: A root endpoint to verify that the API is running.
-   **Response**:
    ```json
    {
      "message": "Sentiment Analysis API is running!"
    }
    ```

### `POST /predict-sentiment`

-   **Description**: Predicts the sentiment of a list of input messages.
-   **Request Body**:
    ```json
    {
      "message": ["string", "string", ...]
    }
    ```
-   **Response Body**: A list of objects, each containing the original message, its predicted label, and the confidence score.
    ```json
    [
      {
        "message": "string",
        "label": "string",
        "confidence": "float"
      }
    ]
