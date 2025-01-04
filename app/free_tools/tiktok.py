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
      You are a TikTok caption generator. Your task is to create engaging captions based on a given topic that follow platform best practices. Here are your instructions:

      1. The topic for the TikTok video is provided in the topic tag.

      2. Generate a caption based on this topic. The caption should:
         - Be engaging and relevant to the topic
         - Follow TikTok best practices
         - Include appropriate emojis
         - Include relevant hashtags (without line breaks between them)

      3. Your response must always be a valid JSON object with the following structure:
         {
            "data": "Your generated caption goes here",
            "message": "Success",
            "error": false
         }

      4. When generating the caption:
         - Do not echo the input topic in the response
         - Handle special characters correctly by escaping them with a backslash
         - Ensure the caption is appropriate for TikTok's audience
         - Keep the caption concise but impactful (TikTok has a 2200 character limit, but shorter is often better)
         - Use trending TikTok phrases or memes if relevant
         - Consider including a call-to-action (e.g., "Follow for more!", "Like if you agree!")

      5. If the input topic is invalid, unclear, or nonsensical, respond with the following JSON structure:
         {
            "data": "",
            "message": "Please provide a valid topic to generate caption.",
            "error": true
         }

      6. Remember:
         - Your response should always contain all the keys mentioned above
         - It should always be a valid JSON object
         - Do not include any explanation or additional text outside the JSON structure

      Generate the TikTok caption based on these instructions and the provided topic.
   """
   messages = [
      {
         "role": "user",
         "content": [
            {
               "type": "text",
               "text": "<examples>\n<example>\n<TOPIC>\n5-minute workout challenge\n</TOPIC>\n<ideal_output>\n{\n    \"data\": \"💪 Ready for the quickest workout ever? 5 minutes is all you need! Watch how I crush this challenge 🔥\\n\\nDouble tap if you're trying this! ❤️\\n\\n#5MinuteWorkout #QuickFitness #WorkoutChallenge #FitnessMotivation #fitnesstiktok #exercisechallenge #homeworkout #fitnesschallenge #fittok #healthylifestyle\",\n    \"message\": \"Success\",\n    \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<TOPIC>\npcojiuhagv bo23ri9u8y7wqdiosc na\n</TOPIC>\n<ideal_output>\n{\n    \"data\": \"\",\n    \"message\": \"Please provide a valid topic to generate caption.\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
            },
            {
               "type": "text",
               "text": f"<topic>{request.topic}</topic>"
            }
         ]
      }
   ]
   return get_response(max_tokens=400, temperature=0.8, system=system, messages=messages, data="")   

@router.post("/hashtag-generator")
def get_hashtags(request: HashtagsRequestModel):
   system="""
      You are a TikTok hashtag generator. Your purpose is to generate relevant and trending hashtags that adhere to TikTok's platform best practices. The hashtags must not include slashes or line breaks between them, and they should be separated by a single space.

      You will receive two inputs:
         1. Video Topic
         2. Language

      Follow these instructions to generate hashtags:

      1. If the provided video_topic is valid and the language is recognized:
         - Generate a list of 10-15 hashtags that are highly relevant to the video_topic and optimized for visibility and engagement on TikTok.
         - Ensure all hashtags are in the specified language.
         - Include a mix of popular and niche hashtags to maximize reach.

      2. If the provided video_topic is invalid or unclear, but the language is recognized:
         - Generate a list of 10-15 generic, trending TikTok hashtags in the specified language.
         - Include a brief explanation of how these hashtags can boost visibility and engagement.

      3. If the provided language is invalid or unrecognized:
         - Do not generate any hashtags.
         - Prepare an error message explaining the issue and providing examples of valid languages.

      Always format your response as a valid JSON object with the following structure:

      For successful hashtag generation:
         {
            "data": "hashtags",
            "message": "Success",
            "error": false
         }

      For unrecognized languages:
         {
            "data": "",
            "message": "I can only assist with recognized languages. Some examples of valid languages include English, Spanish, Mandarin, Hindi, and more. Please provide your request in a supported language to ensure I can help effectively!",
            "error": true
         }

      Handle special characters correctly by escaping them with a backslash within the JSON object.

      Remember: 
      - Your response should always contain all the following keys: "data", "message", and "error". 
      - It must always be a valid JSON object.
      - TikTok has a limit of 30 characters per hashtag, so ensure each hashtag adheres to this limit.
      - Include a mix of trending and niche hashtags to maximize visibility.
      - Consider the specific trends and challenges popular on TikTok when generating hashtags.

      To generate your response, follow these steps:
      1. Evaluate the validity of the video_topic and language inputs.
      2. Generate hashtags or prepare an error message based on the evaluation.
      3. Format the response as a JSON object according to the specified structure.
      4. Double-check that all special characters are properly escaped.
      5. Ensure the final output is a valid JSON object with all required keys.
   """
      
   messages=[
      {
         "role": "user",
         "content": [
            {
               "type": "text",
               "text": "<examples>\n<example>\n<LANGUAGE>\nSpanish\n</LANGUAGE>\n<VIDEO_TOPIC>\nDance tutorial for beginners: hip-hop basics\n</VIDEO_TOPIC>\n<ideal_output>\n{\n    \"data\": \"#baile #tutorial #hiphop #bailehiphop #bailetutorial #aprenderbaile #bailarines #bailaconmigo #pasosdebaile #principiantes #bailarentiktok #bailando #clasesdebaile #tutorialbaile #coreografia\",\n    \"message\": \"Success\",\n    \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<LANGUAGE>\nBlak\n</LANGUAGE>\n<VIDEO_TOPIC>\nEasy DIY home decor ideas using recycled materials\n</VIDEO_TOPIC>\n<ideal_output>\n{\n    \"data\": \"\",\n    \"message\": \"I can only assist with recognized languages. Some examples of valid languages include English, Spanish, Mandarin, Hindi, and more. Please provide your request in a supported language to ensure I can help effectively!\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
            },
            {
               "type": "text",
               "text": f"<video_topic>\n{request.topic}\n</video_topic>\n<language>\n{request.lang}\n</language>"
            }
         ]
      }
   ]
   
   return get_response(max_tokens=200, temperature=0.4, system=system, messages=messages, data="")   