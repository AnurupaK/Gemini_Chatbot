from dotenv import load_dotenv
import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold,StopCandidateException
import re
from googletrans import Translator

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key for Google Generative AI is not set in the environment variables.")
   

genai.configure(api_key=api_key)

##Creating the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8000,
    "response_mime_type": "text/plain",
}


##Update safety settings
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

system_instruction = "You are a friendly and accurate information provider. Strictly avoid answering any questions that could be harmful, violent, or inappropriate."

##Model object
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings= safety_settings
)


##Create chat session
chat_session = model.start_chat(history=[])

##For resetting chat
def reset_chat_session():
    global chat_session
    chat_session = model.start_chat(history=[])
    

def translate_with_googletrans(response_from_model,language):
    translator = Translator()
    translated_response = translator.translate(response_from_model, dest=language)
    return translated_response.text

##Gemini response function    
def get_gemini_response(user_message,language):
    try:
        user_message = user_message.lower().strip()
        response = chat_session.send_message(user_message)
        text = response.text
        response = re.sub(r"\*\*Assistant\*\*|\*\*assistant\*\*", "", text)
        if(language.lower()=='english'):
             return response
        else:
            return translate_with_googletrans(response,language)
    except StopCandidateException as e:
        return "Please refrain from asking questions that are inapropriate or irrelevant 😊"



# done_yet = True
# while done_yet:
#     question = input("Ask the bot: ")
#     language = "Bengali"  # Assuming default language is English
#     response = get_gemini_response(question,language)
#     print("Bot response:", response)
#     wish = input("Do you want to continue? (yes/no): ")
#     done_yet = wish.lower() == "yes"

    
    
