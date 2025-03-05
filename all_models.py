"""
File contains different function for executing ai response based on inputs
"""

import google.generativeai as genai
from groq import Groq

def getAI(ai_model, api_key, prompt):
    
    if ai_model == "Gemini":
        gemini_api_key = api_key 

        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel(model_name = "gemini-2.0-flash-001")
        model_resp = model.generate_content(prompt)

        return model_resp.text

    if ai_model == "Gorq":
        gorq_api_key = api_key
        client = Groq(api_key=gorq_api_key)

        gorq_resp = client.chat.completions.create(
            messages=[prompt],
            model="llama-3.3-70b-versatile")
        
        return gorq_resp.choices[0].message.content
    
    return "gen AI key or some other issues"

# {
#                     "role": "system",
#                     "content": "you are Cover letter creator expert"
#                 },
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }