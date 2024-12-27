from pydantic import BaseModel, Field
from fastapi import APIRouter
from ..helpers.anthropic_helpers import get_response

router = APIRouter()

# Request Models
class CpationRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic or script of your TikTok Video.")  

class HashtagsRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic of your TikTok") 
   lang: str = Field(..., description="Hashtags language, e.g., eng, urdu, hindi.") 

@router.post("/caption-generator")
def get_caption(request: CpationRequestModel):
   system="""
      You are a Tiktok caption generator. Generate engaging caption that follow platform best practices.
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
         "content": f"Generate an Tiktok caption and trendy hashtags for: {request.topic}. "
      }
   ]
   return get_response(model="claude-2.1", max_tokens=300, temperature=0.5, system=system, messages=messages, data="")   

@router.post("/hashtag-generator")
def get_hashtags(request: HashtagsRequestModel):
   system="""
      You are a Tiktok hashtag generator. Your purpose is to generate relevant and trending hashtags that adhere to Tiktok's platform best practices. The hashtags must not include slashes or line breaks between them, and they should be separated by a single space.
      Requirements:
      1. If the provided topic is valid, generate a list of hashtags that are highly relevant and optimized for visibility and engagement on Tiktok.
      2. If the provided topic is invalid or unclear, generate a generic list of trending Tiktok hashtags and include a brief explanation of how they can boost visibility and engagement.
         Response Format:
            - Your response must always be a valid JSON object with the following structure:
               {
                  "data": "hashtags"
                  "message": "Success", 
                  "error": False
               }
      3. If the provided language is invalid or unrecognized, respond with the following message JSON Format.
         Error Response Format: For Unrecognized Languages
            - Your response must always be a valid JSON object with the following structure:
               {
                  "data": "",
                  "message": "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!",
                  "error": True
               }
      4. Handle special characters correctly by escaping them with a backslash.
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
      """
      
   messages=[
      {
         "role": "user",
         "content": f"Generate TikTok 10 trending hashtags for topic: {request.topic} in {request.lang} language."
      }
   ]
   return get_response(model="claude-2.1", max_tokens=256, temperature=0.4, system=system, messages=messages, data="")   