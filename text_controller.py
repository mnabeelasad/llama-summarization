import boto3
import os

# Initialize AWS SDK (Boto3 client for AWS Bedrock)
client = boto3.client('bedrock', region_name=os.getenv("AWS_REGION", "eu-central"))  

def summarize_using_llama(text):
    """
    Function to interact with AWS Bedrock using Llama 3.1 for summarization.
    """
    model_id = 'give your model id here' 

    # Construct the prompt as per the required format
    prompt = f"""
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    Give you prompt for summarization.
    You are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>
    {text}
    <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    """

    # Make the API request to AWS Bedrock to summarize the text
    response = client.invoke_model(
        modelId=model_id,
        body=prompt,  
        contentType="text/plain",  
        accept="application/json"  
    )

    # Parse the response and extract the summary
    summary = response['body'].read().decode('utf-8')
    return summary
