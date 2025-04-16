import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging
import sys

# Configure logging with more detail
logging.basicConfig(
    level=logging.ERROR,  # Changed from DEBUG to ERROR
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        #logging.FileHeadler("gemini_debug.log"),  # Keep this for debugging purposes
        logging.StreamHandler(sys.stdout)  # Removed FileHandler to stop writing to gemini_debug.log
    ]
)

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API key format
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env file")

logging.debug(f"Environment loaded, API_KEY is set")

# Configure the generative AI client
try:
    genai.configure(api_key=API_KEY)
    logging.debug("Configured Gemini API client")
except Exception as e:
    logging.error(f"Failed to configure Gemini client: {str(e)}")
    raise

try:
    # List available models first
    models = genai.list_models()
    model_names = [m.name for m in models]
    logging.debug(f"Available models: {model_names}")
    
    if "models/gemini-1.5-pro" not in model_names:
        raise RuntimeError("gemini-1.5-pro model is not available. Available models: " + ", ".join(model_names))
    
    # Initialize the model
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    
    # Simple test to verify the model works
    response = model.generate_content("Hello, are you working?")
    if not response or not hasattr(response, "text"):
        raise RuntimeError("Model initialization test failed - invalid response")
        
    logging.info(f"Successfully initialized model. Test response: {response.text[:100]}")
    
except Exception as e:
    error_msg = f"Failed to initialize Gemini model: {str(e)}"
    logging.error(error_msg)
    raise RuntimeError(error_msg)

def ask_gemini(question):
    try:
        logging.debug(f"Sending question: {question}")
        response = model.generate_content(question)
        
        if not response or not hasattr(response, "text"):
            logging.error("Invalid response from Gemini API")
            return "Sorry, I couldn't process your question."
            
        return response.text
        
    except Exception as e:
        logging.error(f"Error generating response: {str(e)}")
        return "Sorry, something went wrong. Please try again later."
