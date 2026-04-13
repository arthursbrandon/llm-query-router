import os
from dotenv import load_dotenv
from groq import Groq
from google import genai
from huggingface_hub import InferenceClient


class Models:

    load_dotenv()
    #groq_client = Groq(api_key="")
    genai_client = genai.Client(api_key=str(os.getenv('GENAI_API_KEY')))
    #lama_client = InferenceClient(token="")


    def __init__(self, category, prompt):
        self.category = category
        self.prompt = prompt

    
    def _getGroq(self):
        pass

    def _getGenai(self):

        
        response = self.genai_client.models.generate_content(
            model = "gemini-3-flash-preview",
            contents = self.prompt
        )

        return response.text
        
    def _getLama(self):
        pass

    def loadModel(self):
        match self.category:
            case 'coding':
                return self._getGroq()
            case 'reasoning':
                return self._getGenai()
            case 'creative':
                return self._getLama()
            case 'factual':
                return self._getGenai()
