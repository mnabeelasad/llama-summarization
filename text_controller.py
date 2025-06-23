import boto3
import os

# Initialize AWS SDK (Boto3 client for AWS Bedrock)
client = boto3.client('bedrock', region_name=os.getenv("AWS_REGION", "us-west-2"))  # Ensure region is correct

def summarize_using_llama(text):
    """
    Function to interact with AWS Bedrock using Llama 3.1 for summarization.
    """
    model_id = 'llama-3.1'  # Specify Llama 3.1 model ID

    # Construct the prompt as per the required format
    prompt = f"""
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    Cutting Knowledge Date: December 2023
    Today Date: 23 July 2024
    You are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>
    {text}
    <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """

    # Make the API request to AWS Bedrock to summarize the text
    response = client.invoke_model(
        modelId=model_id,
        body=prompt,  # Pass the constructed prompt
        contentType="text/plain",  # Content type as plain text
        accept="application/json"  # Accepting JSON response
    )

    # Parse the response and extract the summary
    summary = response['body'].read().decode('utf-8')
    return summary
