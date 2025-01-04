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
      You are a YouTube description generator. Your task is to create engaging descriptions that follow platform best practices based on the video type and topic provided. Follow these instructions carefully:

      1. Your response should always be a valid JSON object with the following structure:
         {
            "data": "description",
            "message": "Success",
            "error": false
         }

      2. To generate the description:
         a. For shorts (videos under 60 seconds):
            - Keep the description brief, around 50-100 characters
            - Include 1-3 relevant hashtags
            - Focus on a catchy, attention-grabbing first line
         b. For long videos (over 60 seconds):
            - Write a description of 150-200 words
            - Include 3-5 relevant hashtags
            - Summarize the main points of the video
            - Add a call-to-action (e.g., "Like and subscribe!")
         also use emojis in both cases.

      3. Always include these elements in your description:
         - A hook or intriguing question related to the topic
         - Keywords related to the video topic
         - Proper capitalization and punctuation

      4. If the provided input is invalid, unclear, or nonsensical, respond with a JSON object in this format:
         {
            "data": "",
            "message": "I'm sorry, but the text you provided doesn't seem to be a clear topic for a YouTube video.",
            "error": true
         }

      5. Remember to handle special characters correctly by escaping them with a backslash in the JSON response.

      6. Do not echo the input prompt in the response.

      7. Ensure that your entire response is a valid JSON object containing all the required keys ("data", "message", "error") with the specified limitations.

      Begin generating the YouTube description based on the provided video type and topic. If you understand these instructions, proceed with creating the description or error message as appropriate.
   """
   messages=[
      {
         "role": "user",
         "content": [
               {
                  "type": "text",
                  "text": "<examples>\n<example>\n<VIDEO_TYPE>\nlong\n</VIDEO_TYPE>\n<VIDEO_TOPIC>\nbaksvhcam sa\n</VIDEO_TOPIC>\n<ideal_output>\n{\n   \"data\": \"\",\n   \"message\": \"I'm sorry, but the text you provided doesn't seem to be a clear topic for a YouTube video.\",\n   \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<VIDEO_TYPE>\nshort\n</VIDEO_TYPE>\n<VIDEO_TOPIC>\n10 Quick Workout Moves for Busy Professionals\n</VIDEO_TOPIC>\n<ideal_output>\n{\n   \"data\": \"💪 Need a quick workout? These 10 power moves fit ANY schedule!\\n\\nGet fit in minutes - perfect for busy professionals 🏃‍♂️\\n\\n#QuickWorkout #FitnessHacks #BusyLifestyle\",\n   \"message\": \"Success\",\n   \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<VIDEO_TYPE>\nshort\n</VIDEO_TYPE>\n<VIDEO_TOPIC>\nbwudjiaksmsx\n</VIDEO_TOPIC>\n<ideal_output>\n{\n   \"data\": \"\",\n   \"message\": \"I'm sorry, but the text you provided doesn't seem to be a clear topic for a YouTube video.\",\n   \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<video_type>{request.video_size}</video_type>\n<video_topic>{request.topic}</video_topic>"
               }
         ]
      }
   ]
   return get_response(max_tokens=250, temperature=0.7, system=system, messages=messages, data="") 
   
@router.post("/hashtag-generator")
def get_hashtags(request: HashtagsRequestModel):
   system="""
      You are a YouTube hashtag generator. Your purpose is to generate relevant and trending hashtags that adhere to YouTube's platform best practices. The hashtags must not include slashes or line breaks between them, and they should be separated by a single space.

      You will receive two inputs:
         1. Video Topic
         2. Language

      Follow these instructions to generate hashtags:

      1. If the provided video_topic is valid and the language is recognized:
         - Generate a list of 10-15 hashtags that are highly relevant to the video_topic and optimized for visibility and engagement on YouTube.
         - Ensure all hashtags are in the specified language.

      2. If the provided video_topic is invalid or unclear, but the language is recognized:
         - Generate a list of 10-15 generic, trending YouTube hashtags in the specified language.
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
            "message": "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!",
            "error": true
         }

      Handle special characters correctly by escaping them with a backslash within the JSON object.

      Remember: Your response should always contain all the following keys: "data", "message", and "error". It must always be a valid JSON object.

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
                  "text": "<examples>\n<example>\n<example_description>\nSince an invalid video topic was provided, hashtags were generated based on the recognized language.\n</example_description>\n<VIDEO_TOPIC>\npaxbs nmxs\n</VIDEO_TOPIC>\n<LANGUAGE>\nUrdu\n</LANGUAGE>\n<ideal_output>\n{\n  \"data\": \"#یوٹیوب #پاکستان #ٹرینڈنگ #سوشل_میڈیا #پاکستانی_یوٹیوبر #ویڈیو #انٹرٹینمنٹ #یوٹیوبر #مشہور #اردو #وائرل #وائرل_ویڈیو #پاکستانی_کنٹینٹ #دلچسپ #ٹاپ_ٹرینڈنگ\",\n  \"message\": \"Since the video topic was unclear, I've generated popular and trending Urdu YouTube hashtags that can help increase your video's visibility in the Pakistani and Urdu-speaking market. These hashtags cover general categories and trending topics to maximize reach.\",\n  \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<VIDEO_TOPIC>\nBeginner's Guide to Urban Gardening\n</VIDEO_TOPIC>\n<LANGUAGE>\nBlank\n</LANGUAGE>\n<ideal_output>\n{\n  \"data\": \"\",\n  \"message\": \"I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<video_topic>\n{request.topic}\n</video_topic>\n<language>\n{request.lang}\n</language>"
               }
         ]
      }
   ]
      
   return get_response(max_tokens=400, temperature=0.4, system=system, messages=messages, data="") 

@router.post("/title-generator")
def get_titles(request: TitlesRequestModel):
   system="""
      You are a YouTube video title generator. Your task is to create engaging and catchy titles for YouTube videos based on provided details. Follow these instructions carefully:

      1. You will receive video details in the VIDEO_DETAILS variable.

      2. Generate 10 unique and engaging titles based on the provided video details.

      3. Rules for generating titles:
         - Make titles catchy, intriguing, and relevant to the video content
         - Keep titles concise, ideally under 60 characters
         - Use power words, numbers, or questions to increase click-through rates
         - Avoid clickbait or misleading titles

      4. Format your response as a valid JSON object with the following structure:
         {
            "data": ["title1", "title2", ..., "title10"],
            "message": "Success",
            "error": false
         }

      5. If the provided input is invalid, unclear, or nonsensical, respond with a JSON object in the following format:
         {
            "data": [],
            "message": "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video. Could you please provide a more specific topic or script idea?",
            "error": true
         }

      6. Important notes:
         - Always ensure your response is a valid JSON object
         - Include all required keys (data, message, error) in your response
         - Handle special characters correctly by escaping them with a backslash
         - Do not echo the input prompt in the response

      Remember, your entire response should be a single, valid JSON object. Do not include any text outside of this JSON structure.
      """
   messages=[
      {
         "role": "user",
         "content": [
               {
                  "type": "text",
                  "text": "<examples>\n<example>\n<VIDEO_DETAILS>\nIn this captivating video, we unravel the mysteries of lucid dreaming. We explore the science behind this phenomenon, where dreamers become aware they're dreaming and can even control their dream narratives. We'll discuss techniques to induce lucid dreams, from reality checks to dream journaling, and delve into the potential benefits for creativity, problem-solving, and overcoming nightmares. Our expert guests, including neuroscientists and experienced lucid dreamers, share their insights and personal experiences. We also examine the cultural significance of lucid dreaming across different societies and its portrayal in popular media. Join us on this mind-bending journey into the realm of conscious dreaming!\n</VIDEO_DETAILS>\n<ideal_output>\n{\n  \"data\": [\n    \"The Science of Lucid Dreaming: How to Control Your Dreams\",\n    \"Master Lucid Dreaming in 2024: Expert Tips Revealed\",\n    \"Unlock Your Mind: The Ultimate Guide to Lucid Dreaming\",\n    \"How I Learned to Control My Dreams (Neuroscience Explained)\",\n    \"5 Powerful Techniques to Trigger Lucid Dreams Tonight\",\n    \"Lucid Dreaming: From Ancient Practice to Modern Science\",\n    \"The Hidden Benefits of Lucid Dreaming You Never Knew\",\n    \"Dream Like a Pro: Secrets from Expert Lucid Dreamers\",\n    \"Transform Your Nightmares into Adventures with Lucid Dreaming\",\n    \"Inside Your Dreams: The Truth About Conscious Dreaming\"\n  ],\n  \"message\": \"Success\",\n  \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<VIDEO_DETAILS>\nxasbjkh nasa\n</VIDEO_DETAILS>\n<ideal_output>\n{\n    \"data\": [],\n    \"message\": \"I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video. Could you please provide a more specific topic or script idea?\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<video_details>\n{request.details}\n</video_details>"
               }
         ]
      }
   ]
      
   return get_response(max_tokens=300, temperature=0.5, system=system, messages=messages, data=[]) 
      
@router.post("/username-generator")
def get_usernames(request: UsernamesRequestModel):
   system="""
      You are a YouTube username generator. Your task is to generate creative, memorable usernames that follow YouTube guidelines based on the user's input. Follow these instructions carefully:

      1. You will receive the following inputs:
         a. full_name
         b. account_topic
         c. description

      2. Generate 10 unique usernames based on the provided inputs. Ensure that the usernames are:
         - Creative and catchy
         - Relevant to the account topic and description
         - Optimized for engagement
         - Compliant with YouTube guidelines

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

      Now, based on the provided inputs, generate the YouTube usernames and format your response as instructed.   
   """
   messages=[
      {
         "role": "user",
         "content": [
               {
                  "type": "text",
                  "text": "<examples>\n<example>\n<example_description>\nFollow the ideal output of this example if all inputs are invalid.\n</example_description>\n<FULL_NAME>\npoasckjn\n</FULL_NAME>\n<DESCRIPTION>\n[wcsjiuw\n</DESCRIPTION>\n<ACCOUNT_TOPIC>\n021i9dwiquxnma\n</ACCOUNT_TOPIC>\n<ideal_output>\n{\n  \"data\": [],\n  \"message\": \"Invalid inputs detected. Please provide: 1) A real full name using standard characters, 2) A clear and specific account topic that describes your content focus, and 3) A proper description of your channel using complete sentences and proper formatting. The current inputs appear to be random characters.\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nFollow the ideal output of this example if the account_topic input is invalid.\n</example_description>\n<FULL_NAME>\nEmily Rose Thompson\n</FULL_NAME>\n<DESCRIPTION>\nI'm looking for a username that combines professionalism with a touch of motivation. Something that reflects both the fitness aspect and the idea of balancing a busy life. Maybe incorporate a play on words related to time management or energy?\n</DESCRIPTION>\n<ACCOUNT_TOPIC>\nasn as\n</ACCOUNT_TOPIC>\n<ideal_output>\n{\n    \"data\": [],\n    \"message\": \"Please provide a valid account topic. The topic should clearly describe the main focus of your YouTube channel (e.g., fitness, cooking, gaming, etc.).\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nFollow the ideal output of this example if the description input is invalid.\n</example_description>\n<FULL_NAME>\nOlivia Grace Martinez\n</FULL_NAME>\n<DESCRIPTION>\ncdnjbhnac as\n</DESCRIPTION>\n<ACCOUNT_TOPIC>\nFashion and Sustainable Style Tips\n</ACCOUNT_TOPIC>\n<ideal_output>\n{\n  \"data\": [],\n  \"message\": \"Please provide a valid description. The description should clearly explain your content focus, style preferences, or unique angle for your fashion and sustainable style channel.\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nFollow the ideal output of this example if the full_name input is invalid.\n</example_description>\n<FULL_NAME>\naskuashbjn09qw8uuijhbnqw\n</FULL_NAME>\n<DESCRIPTION>\nI'd like a username that conveys a sense of calm and tranquility, but also feels approachable for newcomers to meditation. Maybe something with a nature theme or a play on words related to mindfulness? I want it to sound soothing but not too serious.\n</DESCRIPTION>\n<ACCOUNT_TOPIC>\nMindfulness and Meditation for Beginners\n</ACCOUNT_TOPIC>\n<ideal_output>\n{\n  \"data\": [],\n  \"message\": \"Please provide a valid full name. The provided name appears to be a random string of characters. A real name will help generate more authentic and meaningful usernames.\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIideal output example for all valid inputs.\n</example_description>\n<FULL_NAME>\nAlexander J. Winters\n</FULL_NAME>\n<ACCOUNT_TOPIC>\nDIY Home Improvement and Woodworking\n</ACCOUNT_TOPIC>\n<DESCRIPTION>\nI'm looking for a username that combines my love for woodworking with a hint of humor. Something that shows I'm skilled but don't take myself too seriously. Maybe a play on words with tools or wood types would be fun!\n</DESCRIPTION>\n<ideal_output>\n{\n  \"data\": [\n    \"WoodWorkingWinters\",\n    \"AlexTheToolMan\",\n    \"SawdustSage\",\n    \"WintersWorkshop\",\n    \"ChiselChampAlex\",\n    \"DrillMasterAJ\",\n    \"PlankProfessor\",\n    \"WoodWhispererAJ\",\n    \"HandymanHumor\",\n    \"CraftyWinters\"\n  ],\n  \"message\": \"Success\",\n  \"error\": false\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<full_name>\n{request.name}\n</full_name>\n\n<account_topic>\n{request.topic}\n</account_topic>\n\n<description>\n{request.description}\n</description>"
               }
         ]
      }
   ]
      
   return get_response(max_tokens=200, temperature=0.7, system=system, messages=messages, data=[]) 