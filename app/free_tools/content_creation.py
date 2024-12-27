import os, json, anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from ..helpers.exception_helper import get_exception_response
from ..helpers.anthropic_helpers import get_response
from constants import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, FAIL_RESPONSE

load_dotenv()
router = APIRouter()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class HooksRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic of your video, and even your script if you want.")
   target_audience: str = Field(..., description="Target Audience")
   context: str = Field(..., description="Video Context")   

class ScriptRequestModel(BaseModel):
   topic: str = Field(..., description="Provide the topic of your Video and we'll generate the best script.")

class IdeasRequestModel(BaseModel):
   keyword: str = Field(..., description="Please enter keywords related to your YouTube video below, and we'll generate YouTube Video Ideas.")

@router.post("/video-hook-generator")
def get_video_hooks(request: HooksRequestModel):
   system="""
      You are a video hooks generator. Generate engaging hooks that follow platform best practices.
      Follow these rules:  
      1. Always format the response as a valid JSON object with numeric keys (1-10), e.g.,  
      2. Do not echo the input prompt in the response.
      3. Handle special characters correctly by escaping them with a backslash.
      4. Each hook should be designed to immediately grab attention, provoke curiosity, and fit the tone and fast-paced nature of video.
         {
            "data": ['hook1', 'hook2', ... , 'hook10'],
            "message": "Success", 
            "error": False
         }  
      5. If the provided inputs is unclear or nonsensical, respond with a JSON object like this:
         {
            "data": [], 
            "message": "I'm sorry, but the input you provided doesn't seem to be clear for a hook video. Could you please provide valid video topic, target_audience, or context?",
            "error": True
         }
      6. Your response must always be a valid JSON object with 10 unique hooks.
      7. Ensure your hooks align with the given topic, target audience, and context, maintaining relevance and appeal.
      8. Avoid generic hooks; each should be distinctive and tailored to the provided attributes.
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
   """
   messages=[
      {
         "role": "user",
         "content": f"""
            Based on the following information, generate 10 catchy, creative, and highly engaging video hooks that will grab the attention of the target audience and fit the video context:
               Topic: {request.topic}
               Target Audience: {request.target_audience}
               Context: {request.context}
            """
      }
   ]
   
   return get_response(model="claude-2.1", max_tokens=1000, temperature=0.3, system=system, messages=messages, data=[]) 

@router.post("/video-script-generator")
def get_video_script(request: ScriptRequestModel):
   try:
      response = client.messages.create(
         model="claude-2.1",
         temperature=0.5,
         max_tokens=1500,
         system="""
            You are a video script generator. Generate a detailed and engaging video script based on the given topic.  Follow these rules:  
               1. Write Perfect Video Scripts with Minimal Effort.
               2. Ensure the script is well-structured, engaging, and suitable for a video.
               3. Do not echo the input prompt in the response.  
               4. Your response should be in markdown like user # for h1, ## h2,... bold letter will be under **bold**.
               5. Handle special characters correctly by escaping them with a backslash.  
               6. If the provided input is invalid, unclear or nonsensical, respond with a trending topic on topic. 
            """,
         messages=[
            {
               "role": "user",
               "content": f"Generate video script based on this Topic: {request.topic}."
            }
         ]
      )
      try:
         res = {
            "data": response.content[0].text,
            "message": "Success",
            "error": False
         }
         return JSONResponse(content=res, status_code=HTTP_200_OK)
      except json.JSONDecodeError:
         return get_exception_response(data="", message=FAIL_RESPONSE, status_code=HTTP_400_BAD_REQUEST)
         
   except Exception as e:
      return get_exception_response(data="", message=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/ai-video-idea-generator")
def get_video_ideas(request: IdeasRequestModel):
   system="""
      You are a YouTube video idea generator. Your task is to create engaging and catchy ideas for YouTube videos based on provided details. Follow these rules:  
      1. Always format the response as a valid JSON object with numeric keys, e.g., 
      2. Do not echo the input prompt in the response.  
      3. Handle special characters correctly by escaping them with a backslash.  
      Response Format:
         - Your response must always be a valid JSON object with the following structure:
         
         {
            "data": ["idea1", "idea2", ... , "idea10"],
            "message": "Success", 
            "error": False
         }
         
      4. If the provided input is unclear or nonsensical, respond with a JSON object in the following format:  
      Error Response Format:  
         - Your Error response must always be a valid JSON object with the following structure: 
         {
            "data": [], 
            "data": "The text you provided isn't a clear keyword for a YouTube video. Could you please provide a more specific keyword to generate an idea for a YouTube video?",
            "error": True
         }
      5. Handle special characters correctly by escaping them with a backslash.
      Note: KEEP IN MIND THAT YOUR RESPONSE SHOULD ALWAYS CONTAINS ALL THE FOLLOWING KEYS WITH ALL THE LIMITATIONS MENTIONED AND IT SHOULD ALWAYS BE A VALID JSON OBJECT.
   """
   messages=[
      {
         "role": "user",
         "content": f"Generate 10 catchy YouTube video ideas based on the following Keywords: {request.keyword}"
      }
   ]
   return get_response(model="claude-2.1", max_tokens=500, temperature=0.7, system=system, messages=messages, data=[])   
