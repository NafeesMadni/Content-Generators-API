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
      You are an Instagram caption generator. Your task is to create engaging captions based on the given topic that follow platform best practices. Here are your instructions:

      1. The topic for the video is provided in the topic tag:

      2. Generate a caption based on this topic. The caption should:
         - Be engaging and relevant to the topic
         - Follow Instagram best practices
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
         - Ensure the caption is appropriate for Instagram's audience
         - Keep the caption concise but impactful

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

      Generate the Instagram caption based on these instructions and the provided topic.   
   """
   messages=[
      {
            "role": "user",
            "content": [
               {
                  "type": "text",
                  "text": "<examples>\n<example>\n<TOPIC>\nTrying out a new home workout routine with resistance bands\n</TOPIC>\n<ideal_output>\n{\n    \"data\": \"Getting those gains from home! 💪 Loving this new resistance band workout - proving you don't need fancy equipment for amazing results! 🎯\\n\\nFeeling the burn and loving every minute of it! Who else is on their fitness journey? Drop a 💪 below!\\n\\n#HomeWorkout #FitnessMotivation #ResistanceBands #FitnessJourney #WorkoutFromHome #FitLife #HealthyLifestyle #NoGymNeeded #FitnessGoals #WorkoutMotivation #FitnessCommunity #StrengthTraining #HomeGym #WorkoutRoutine #FitFam\",\n    \"message\": \"Success\",\n    \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIdea output example if the provided topic input is invalid. \n</example_description>\n<TOPIC>\npxoasjcnh \n</TOPIC>\n<ideal_output>\n{\n    \"data\": \"\",\n    \"message\": \"Please provide a valid topic to generate caption.\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<topic>{request.topic}</topic>"
               }
            ]
      }
   ]
   return get_response(max_tokens=400, temperature=0.8, system=system, messages=messages, data="") 

@router.post("/username-generator")
def get_username(request: UsernameRequestModel):
   
   system="""
      You are an Instagram username generator. Your task is to generate creative, memorable usernames that follow Instagram guidelines based on the user's input. Follow these instructions carefully:

      1. You will receive the following inputs:
         a. full_name
         b. account_topic
         c. description

      2. Generate 10 short unique usernames based on the provided inputs. Ensure that the usernames are:
         - Creative and catchy
         - Relevant to the account topic and description
         - Optimized for engagement
         - Compliant with Instagram guidelines (e.g., no profanity, no impersonation)
         - 20 characters or less
         - Can only use letters, numbers, periods, and underscores
         - Don't use more than one periods or underscores in a single username

      3. Your response must always be a valid JSON object with the following structure:
         {
            "data": ["username1", "username2", ... , "username10"],
            "message": "Success",
            "error": false
         }

      4. If any input is invalid or insufficient, return an error message in JSON format. Be specific about which input needs correction. For example:
         {
            "data": [],
            "message": "Please provide a valid [input_type]. [Specific guidance on what's expected]",
            "error": true
         }

         Replace [input_type] with "full name", "account topic", or "description" as appropriate, and provide specific guidance.

      5. Handle special characters correctly by escaping them with a backslash in the JSON output.

      6. Remember:
         - Always return a valid JSON object
         - Include all required keys: "data", "message", and "error"
         - Generate exactly 10 usernames when inputs are valid
         - Do not include any explanation or additional text outside the JSON structure
         - Instagram usernames are not case-sensitive, so you can use a mix of uppercase and lowercase letters for readability, but avoid relying on case for uniqueness

      Now, based on the provided inputs, generate the Instagram usernames and format your response as instructed.
   """
   
   messages=[
      {
         "role": "user",
         "content": [
            {
               "type": "text",
               "text": "<examples>\n<example>\n<FULL_NAME>\nAlexander James Martinez\n</FULL_NAME>\n<DESCRIPTION>\nCapturing the pulse of city life through my lens. I explore hidden corners, street art, and architectural marvels to showcase the beauty and grit of urban landscapes worldwide.\n</DESCRIPTION>\n<ACCOUNT_TOPIC>\nUrban Photography\n</ACCOUNT_TOPIC>\n<ideal_output>\n{\n    \"data\": [\n        \"urban.alex.lens\",\n        \"city.snaps.ajm\",\n        \"alex_urban_eye\",\n        \"martinez_frames\",\n        \"street_alex_m\",\n        \"urbanist.ajm\",\n        \"alexcityvibes\",\n        \"citylens.ajm\",\n        \"alex.urban.pulse\",\n        \"urban.amartinez\"\n    ],\n    \"message\": \"Success\",\n    \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<FULL_NAME>\naspcajc\n</FULL_NAME>\n<ACCOUNT_TOPIC>\nVegan Baking\n</ACCOUNT_TOPIC>\n<DESCRIPTION>\nWhipping up delicious plant-based treats and sharing easy-to-follow recipes. My mission is to prove that vegan desserts can be just as indulgent and satisfying as traditional ones, all while promoting a cruelty-free lifestyle.\n</DESCRIPTION>\n<ideal_output>\n{\n   \"data\": [\n      \"veganbakes_aspcajc\",\n      \"plantbased_baker\",\n      \"cruelty_freebakes\",\n      \"vegansweets.co\",\n      \"greenpatissier\",\n      \"aspcajc.bakes\",\n      \"plantpowered_chef\",\n      \"vegandessertpro\",\n      \"kindbakerclub\",\n      \"vegantreatmaker\"\n   ],\n   \"message\": \"Success\",\n   \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<FULL_NAME>\nSophia Lin Chen\n</FULL_NAME>\n<ACCOUNT_TOPIC>\napaskjncas\n</ACCOUNT_TOPIC>\n<DESCRIPTION>\nExploring the world with intention and respect. I share sustainable travel tips, cultural insights, and hidden gems that promote responsible tourism. Join me on a journey to discover the beauty of our planet while minimizing our environmental impact.\n</DESCRIPTION>\n<ideal_output>\n{\n   \"data\": [],\n   \"message\": \"Please provide a valid account topic. The topic should clearly describe the main focus of your Instagram account (e.g., travel, photography, food, etc.). The current input 'apaskjncas' appears to be random characters.\",\n   \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
            },
            {
               "type": "text",
               "text": f"<full_name>\n{request.name}\n</full_name>\n\n<account_topic>\n{request.topic}\n</account_topic>\n\n<description>\n{request.description}\n</description>"
            }
         ]
      }
   ]
   
   return get_response(max_tokens=200, temperature=0.7, system=system, messages=messages, data=[]) 