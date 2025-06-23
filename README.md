# Llama 3.1 Summarization with AWS Bedrock

This project integrates the **Llama 3.1** model from **AWS Bedrock** to summarize texts through a Flask API.

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone <repository_url>
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up AWS credentials:
    - Configure your AWS CLI:
    ```bash
    aws configure
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Test the API with **Postman**:
    - Send a **POST** request to `http://127.0.0.1:5000/summarize` with the following JSON body:
    ```json
    {
      "languages": "EN",
      "summary": "one_by_one",
      "texts": [
        "Your long text here."
      ]
    }
    ```

## AWS Bedrock Configuration

This project uses **AWS Bedrock** to access the **Llama 3.1** model for summarization. Make sure you have access to **AWS Bedrock** and have the correct permissions to use the Llama 3.1 model.
