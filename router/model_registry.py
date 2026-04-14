import os
import sys
from dotenv import load_dotenv
from groq import Groq
from google import genai



class Models:

    load_dotenv()
    groq_client = Groq(api_key=str(os.getenv('GROK_API_KEY')))
    genai_client = genai.Client(api_key=str(os.getenv('GENAI_API_KEY')))



    def __init__(self, category, prompt):
        self.category = category
        self.prompt = prompt

    
    def _getGroq(self):
        try:
            response = self.groq_client.chat.completions.create(
                messages= [
                    {
                        "role": "user",
                        "content": self.prompt,
                    }
                ],

                model="qwen/qwen3-32b",
            
                

            )
            
            return response.choices[0].message.content
        except Exception as e:
           sys.exit(f'Error: {e}')

    #Google's Gemini
    def _getGenai(self):
        try:
        
            response = self.genai_client.models.generate_content(
                model = "gemini-3-flash-preview",
                contents = self.prompt
            )

            return response.text
        
        except Exception as e:
           sys.exit(f'Error: {e}')
        
    def _getLama(self):
        try:
            response = self.groq_client.chat.completions.create(
                messages= [
                    {
                        "role": "user",
                        "content": self.prompt,
                    }
                ],

                model="llama-3.1-8b-instant",
            
                

            )
            
            return response.choices[0].message.content
        except Exception as e:
           sys.exit(f'Error: {e}')

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
