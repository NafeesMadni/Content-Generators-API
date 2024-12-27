from pydantic import BaseModel, Field
from fastapi import APIRouter
from ..helpers.anthropic_helpers import get_response

router = APIRouter()

class CaptionRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic, script, or any relevant information regarding your Instagram post")

class UsernameRequestModel(BaseModel):
   name: str = Field(..., description="Your Name")
   topic: str = Field(..., description="Account Topic")
   description: str = Field(..., description="Description For Username")

@router.post("/caption-generator")
def get_caption(request: CaptionRequestModel):
   system="""
      You are a Instagram caption generator. Generate engaging caption that follow platform best practices.
      1. Do not echo the input prompt in the response.  
      2. Handle special characters correctly by escaping them with a backslash.  
      3. Include emojis. No line breaks between hashtags.
      Response Format:
         - Your response must always be a valid JSON object with the following structure:
            {
               "data": "response caption",
               "message": "Success", 
               "error": False
            }
      4. If the input is invalid, unclear or nonsensical, respond with the following message:
         Error Response Format:
            - Your response must always be a valid JSON object with the following structure:
               {
                  "data": "",
                  "message": "Please provide a valid topic to generate caption.", 
                  "error": True
               }
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
   """
   messages=[
      {
         "role": "user",
         "content":f"Generate an Instagram caption and trendy hashtags for: {request.topic}\n"
      }
   ]
   return get_response(model="claude-2.1", max_tokens=256, temperature=0.5, system=system, messages=messages, data="") 

@router.post("/username-generator")
def get_username(request: UsernameRequestModel):
   
   system="""
      You are a Instagram username generator. Generate creative, memorable usernames that follow Instagram guidelines. Follow these rules:  

      1. Return the usernames in a valid JSON format with the structure: 
         Response Format:
            - Your response must always be a valid JSON object with the following structure:
               {
                  "data": ['username1', 'username2', ... , 'username10'],
                  "message": "Success", 
                  "error": False
               }  
      2. If the input is invalid, unclear or nonsensical, respond with the following message:
         Error Response Format:
            {
               "data": [], 
               "message": "I'm here to help you generate creative and catchy Instagram usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!",
               "error": True
            }
      3. Ensure that the usernames are creative, relevant to the input, and optimized for engagement. 
      4. Handle special characters correctly by escaping them with a backslash. 
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
   """
   messages=[
      {
         "role": "user",
         "content": f"""
            Based on the provided name, topic, and description, generate 10 unique and catchy usernames for my Instagram.:
               Name: {request.name}
               Topic: {request.topic}
               Description: {request.description}
            """
      }
   ]
   
   return get_response(model="claude-2.1", max_tokens=500, temperature=0.4, system=system, messages=messages, data=[]) 