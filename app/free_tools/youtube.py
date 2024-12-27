from fastapi import APIRouter
from pydantic import BaseModel, Field
from ..helpers.anthropic_helpers import get_response

router = APIRouter()

# Request Models
class DescriptionRequestModel(BaseModel):
   video_size: str = Field(..., description="The size of the video: '1. Long-Form Video' or '2. Short-Form Video'")
   topic: str = Field(..., description="The topic or script of the video")
   
class HashtagsRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic of your YouTube Video/Short")
   lang: str = Field(..., description="Specify the language for the hashtags generation")
   
class TitlesRequestModel(BaseModel):
   details: str = Field(..., description="Provide details about your video")

class UsernamesRequestModel(BaseModel):
   name: str = Field(..., description="Your full name")
   topic: str = Field(..., description="The theme or topic of your account")
   description: str = Field(..., description="Brief description of desired username style")
   
@router.post("/description-generator")
def get_description(request: DescriptionRequestModel):
   system="""
      You are a YouTube description generator. Generate engaging descriptions that follow platform best practices.
      1. Do not echo the input prompt in the response.  
      2. Handle special characters correctly by escaping them with a backslash.
         Response Format:
            {
               "data": "description",
               "message": "Success", 
               "error": False
            }
            
      3. If the provided input is invalid, unclear or nonsensical, respond with a JSON object in the following format:  
         Response Format:                 
            {
               "data": "", 
               "message": "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video.",
               "error": True
            }
                
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
   """
   messages=[
      {
         "role": "user",
         "content": f"Generate a description including trending tags relevant to the topic for YouTube video based on video size: {request.video_size} and topic/Script of that video is: {request.topic}."
      }
   ]
   
   return get_response(model="claude-2.1", max_tokens=700, temperature=0.4, system=system, messages=messages, data="") 
   

@router.post("/hashtag-generator")
def get_hashtags(request: HashtagsRequestModel):
   system="""
      You are a YouTube hashtag generator. Your purpose is to generate relevant and trending hashtags that adhere to YouTube's platform best practices. The hashtags must not include slashes or line breaks between them, and they should be separated by a single space.
      Requirements:
      1. If the provided topic is valid, generate a list of hashtags that are highly relevant and optimized for visibility and engagement on YouTube.
      2. If the provided topic is invalid or unclear, generate a generic list of trending YouTube hashtags and include a brief explanation of how they can boost visibility and engagement.
      3. If the provided language is invalid or unrecognized, respond with a message explaining the issue and provide examples of valid languages such as English, Urdu, Hindi, etc.
      Response Format:
         - Your response must always be a valid JSON object with the following structure:
            {
               "data": "hashtags",
               "message": "Success",
               "error": False
            }
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
         "content": f"Generate 10 YouTube hashtags related to this topic: '{request.topic}' in {request.lang} language."
      }
   ]
      
   return get_response(model="claude-2.1", max_tokens=500, temperature=0.5, system=system, messages=messages, data="") 

@router.post("/title-generator")
def get_titles(request: TitlesRequestModel):
   system="""
      You are a YouTube video title generator. Your task is to create engaging and catchy titles for YouTube videos based on provided details. Follow these rules:  
      1. Always format the response as a valid JSON object with numeric keys, e.g., 
      2. Do not echo the input prompt in the response.  
      3. Handle special characters correctly by escaping them with a backslash.  
      Response Format:
         - Your response must always be a valid JSON object with the following structure:
         
         {
            "data": ['title1', 'title2', ... , 'title10']
            "message": "Success", 
            "error": False
         }  
         
      4. If the provided input is invalid, unclear or nonsensical, respond with a JSON object in the following format:  
      Error Response Format:  
         - Your Error response must always be a valid JSON object with the following structure: 
         {
            "data": [],
            "message": "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video. Could you please provide a more specific topic or script idea?"
            "error": True
         }
         
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT. DON'T FALL BACK TO EXCEPTION ON INVALID INPUT
      """
   messages=[
      {
         "role": "user",
         "content": f"Generate 10 catchy YouTube video titles based on the following details: {request.details}"
      }
   ]
      
   return get_response(model="claude-2.1", max_tokens=600, temperature=0.3, system=system, messages=messages, data=[]) 
      
@router.post("/username-generator")
def get_usernames(request: UsernamesRequestModel):
   system="""
      You are a YouTube username generator. Generate creative, memorable usernames that follow Youtube guidelines. Follow these rules:  

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
               "message": "I'm here to help you generate creative and catchy YouTube usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!",
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
               Based on the provided name, topic, and description, generate 10 unique and catchy usernames for my YouTube channel.:
               Name: {request.name}
               Topic: {request.topic}
               Description: {request.description}
            """
      }
   ]
      
   return get_response(model="claude-2.1", max_tokens=500, temperature=0.4, system=system, messages=messages, data=[]) 