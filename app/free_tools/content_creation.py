import os, anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from ..helpers.anthropic_helpers import get_response

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
      You are a video hook generator AI. Your task is to create engaging hooks for videos based on the given topic, target audience, and context. Follow these instructions carefully to generate appropriate video hooks.
      
      To generate the video hooks:
      
      1. Carefully analyze the provided topic, target audience, and context.
      2. Create 10 unique, engaging hooks that are tailored to the given information.
      3. Ensure each hook is attention-grabbing, provokes curiosity, and fits the fast-paced nature of video content.
      4. Make sure the hooks align with the topic, appeal to the target audience, and consider the given context.
      5. Avoid generic statements; each hook should be distinctive and specific to the provided attributes.

      If any of the inputs are unclear or nonsensical, respond with the error JSON object as specified in rule 5 of the system prompt.

      Format your response as a valid JSON object, following this structure:
         {
            "data": ['hook1', 'hook2', ... , 'hook10'],
            "message": "Success", 
            "error": False
         }

      Remember to escape any special characters with a backslash to ensure the JSON is valid.

      Always provide exactly 10 hooks in your response. Do not include any additional commentary or explanations outside of the JSON object.

      Adhere strictly to all rules and limitations mentioned in the system prompt. Your entire response should be a single, valid JSON object containing all the required keys and following all specified guidelines.
   """
   messages=[
      {
         "role": "user",
         "content": [
            {
               "type": "text",
               "text": "<examples>\n<example>\n<example_description>\nIf the user provides all invalid inputs then follow this ideal output. \n</example_description>\n<TOPIC>\nThepsoaii93uwq\n</TOPIC>\n<CONTEXT>\npcsoiuhse8w\n</CONTEXT>\n<TARGET_AUDIENCE>\noiajkhnb9287tygbn\n</TARGET_AUDIENCE>\n<ideal_output>\n{\n    \"data\": [],\n    \"message\": \"Error: Invalid or unclear inputs provided. Please provide a valid topic, target audience, and context.\",\n    \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nif the user provide invalid context then you output should be like this example idea output.\n</example_description>\n<TOPIC>\nThe future of space tourism and its potential impact on the travel industry\n</TOPIC>\n<CONTEXT>\nposasjnm\n</CONTEXT>\n<TARGET_AUDIENCE>\nAdventure-seeking young professionals and tech enthusiasts aged 25-40 with disposable income, interested in space, technology, and unique travel experiences\n</TARGET_AUDIENCE>\n<ideal_output>\n{\n    \"error\": true,\n    \"message\": \"Invalid context provided. The context 'posasjnm' appears to be nonsensical or unclear. Please provide a clear and relevant context for generating video hooks.\",\n    \"data\": []\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIf the user provides invalid target_audience then your response should follow this example's ideal output. \n</example_description>\n<TOPIC>\nThe role of blockchain technology in revolutionizing supply chain management\n</TOPIC>\n<CONTEXT>\nCreating a series of 5-minute YouTube videos to explain the practical applications of blockchain in supply chain management, showcasing real-world case studies and potential benefits for businesses\n</CONTEXT>\n<TARGET_AUDIENCE>\npxasj23093 cnjscklq548wd2\n</TARGET_AUDIENCE>\n<ideal_output>\n{\n    \"error\": true,\n    \"message\": \"Invalid target audience provided. The target audience contains unrecognizable characters or nonsensical text: 'pxasj23093 cnjscklq548wd2'\",\n    \"data\": []\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIf the user provide invalid video topic then your response should follow this example's ideal output. \n</example_description>\n<TOPIC>\noasc39 xsap002\n</TOPIC>\n<CONTEXT>\nCreating a series of 3-5 minute Instagram Reels to raise awareness about microplastics, their sources, and potential solutions, while encouraging viewers to take action in their daily lives to reduce plastic pollution\n</CONTEXT>\n<TARGET_AUDIENCE>\nEnvironmentally conscious adults aged 25-45, including parents, educators, and health-conscious consumers interested in sustainability and environmental protection\n</TARGET_AUDIENCE>\n<ideal_output>\n{\n    \"error\": true,\n    \"message\": \"Invalid topic provided. Topic 'oasc39 xsap002' appears to be a code or placeholder and does not provide meaningful content to generate video hooks.\",\n    \"data\": []\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIf the user provides valid inputs then follow this example's ideal output. \n</example_description>\n<TOPIC>\nThe impact of vertical farming on urban food sustainability\n</TOPIC>\n<TARGET_AUDIENCE>\nUrban dwellers aged 30-50, including young professionals and families, interested in sustainable living, local food production, and innovative agricultural technologies\n</TARGET_AUDIENCE>\n<CONTEXT>\nCreating a series of 3-4 minute YouTube videos to showcase the benefits and challenges of vertical farming in cities, highlighting real-world examples and discussing how viewers can support or implement small-scale vertical gardening in their own homes\n</CONTEXT>\n<ideal_output>\n{\n    \"data\": [\n        \"What if your next salad came from the 47th floor? The urban farming revolution is here\",\n        \"They said farming couldn't work in skyscrapers - until this happened...\",\n        \"This 'crazy' farming method could feed 10,000 people in a single building\",\n        \"The secret garden hidden inside your city's abandoned warehouse\",\n        \"Why traditional farmers are switching to this controversial growing method\",\n        \"I grew 500 lettuce heads in my tiny apartment - here's how\",\n        \"The shocking truth about where your city's food could come from in 2030\",\n        \"This revolutionary farming technique uses 95% less water (and it's happening above your head)\",\n        \"Your grocery store is about to change forever - vertical farms are taking over\",\n        \"How a single indoor farm is feeding an entire neighborhood (and why it matters)\"\n    ],\n    \"message\": \"Success\",\n    \"error\": false\n}\n</ideal_output>\n</example>\n</examples>\n\n"
            },
            {
               "type": "text",
               "text": f"<topic>\n{request.topic}\n</topic>\n<target_audience>\n{request.target_audience}\n</target_audience>\n<context>\n{request.context}\n</context>"
            }
         ]
      }
   ]
   
   return get_response(max_tokens=400, temperature=0.8, system=system, messages=messages, data=[]) 

@router.post("/video-script-generator")
def get_video_script(request: ScriptRequestModel):
   
   system="""
      You are an AI video script generator. Your task is to create a detailed and engaging video script based on the given topic. Follow these instructions carefully:

      1. Generate a well-structured and engaging video script suitable for the given topic. The script should be detailed and appropriate for video presentation.

      2. Structure your response in markdown format:
         - Use # for h1 headings
         - Use ## for h2 headings
         - Use ### for h3 headings, and so on
         - Use **bold** for emphasis
         - Handle special characters correctly by escaping them with a backslash in the JSON response
         - Use "\n" for line breaks
         - Use proper markdown syntax for lists, quotes, and other formatting as needed

      3. Do not repeat or echo the input prompt in your response.

      4. Handle special characters correctly by escaping them with a backslash.

      5. Your output should be formatted as a JSON object with the following structure:
          {
            "data": "Your markdown content goes here",
            "message": "Success or error message",
            "error": boolean value (true if input is invalid, false otherwise)
         }
      6. If the provided video topic is valid and clear:
         - Generate the script and place it in the "data" field
         - Set the "message" field to "Success"
         - Set the "error" field to false

      7. If the provided video topic is invalid, unclear, or nonsensical:
         - Generate a script for a trending topic of your choice
         - Place this script in the "data" field
         - Set the "message" field to "Your input was invalid. As a result, we've created a script based on a trending topic that is more relevant and engaging"
         - Set the "error" field to true

      Begin generating the video script now.
   """
   
   messages=[
      {
         "role": "user",
         "content": [
             {
               "type": "text",
               "text": "<examples>\n<example>\n<example_description>\nIf the user provides a invalid video topic then your response should follow this example's ideal output.\n</example_description>\n<VIDEO_TOPIC>\nscnm s masc\n</VIDEO_TOPIC>\n<ideal_output>\n{\n  \"data\": \"# The Rise of Artificial Intelligence in Daily Life\\n\\n## Introduction\\n\\nWelcome viewers! Today we're diving into one of the most fascinating and transformative technologies of our time - Artificial Intelligence, or AI.\\n\\n## What is AI?\\n\\n**Artificial Intelligence** is all around us, quietly revolutionizing how we live, work, and interact. From the moment you wake up to when you go to bed, AI is there, making your life easier in ways you might not even realize.\\n\\n### Common AI Applications\\n\\n1. **Smart Assistants**\\n   - Siri, Alexa, and Google Assistant\\n   - Voice-controlled home automation\\n   - Personalized recommendations\\n\\n2. **Social Media**\\n   - Content curation\\n   - Face recognition\\n   - Targeted advertising\\n\\n## Impact on Different Industries\\n\\n### Healthcare\\n- Disease diagnosis\\n- Drug discovery\\n- Patient care optimization\\n\\n### Transportation\\n- Self-driving cars\\n- Traffic management\\n- Route optimization\\n\\n### Entertainment\\n- Streaming recommendations\\n- Gaming experiences\\n- Content creation\\n\\n## The Future of AI\\n\\n**What's next for AI?**\\n- More personalized experiences\\n- Enhanced automation\\n- Breakthrough innovations\\n\\n## Conclusion\\n\\nAI isn't just a glimpse of the future - it's already here, shaping our world in remarkable ways. As we continue to advance, the possibilities are endless.\\n\\n**Call to Action**\\nShare your thoughts on AI in the comments below, and don't forget to subscribe for more fascinating tech insights!\\n\\n*[End of Script]*\",\n  \"message\": \"Your input was invalid. As a result, we've created a script based on a trending topic that is more relevant and engaging\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIf the user provides a invalid video topic then your response should follow this example's ideal output.\n</example_description>\n<VIDEO_TOPIC>\niuhas c\n</VIDEO_TOPIC>\n<ideal_output>\n{\n  \"data\": \"# The Rise of Artificial Intelligence: Shaping Our Future\\n\\n## Introduction\\n\\nWelcome to this fascinating exploration of artificial intelligence and its impact on our daily lives. Today, we'll dive deep into how AI is revolutionizing everything from smartphone technology to healthcare.\\n\\n## The AI Revolution\\n\\n### What is Artificial Intelligence?\\n**Artificial Intelligence** is the simulation of human intelligence by machines, enabling them to:\\n- Learn from experience\\n- Adjust to new inputs\\n- Perform human-like tasks\\n\\n### Current Applications\\nLet's look at where AI is already making waves:\\n1. Virtual assistants (Siri, Alexa)\\n2. Healthcare diagnostics\\n3. Autonomous vehicles\\n4. Smart home technology\\n\\n## Impact on Society\\n\\n### Benefits\\n- **Increased Efficiency**: AI automates repetitive tasks\\n- **Enhanced Decision Making**: Data-driven insights\\n- **Improved Safety**: Reduced human error\\n\\n### Challenges\\n- Privacy concerns\\n- Job displacement\\n- Ethical considerations\\n\\n## The Future of AI\\n\\n### Emerging Trends\\n- **Quantum Computing Integration**\\n- **Enhanced Natural Language Processing**\\n- **Advanced Robotics**\\n\\n## Closing Thoughts\\n\\nAs we conclude, remember that AI isn't just about technology – it's about enhancing human capabilities and creating a better future for all. The question isn't whether AI will change our world, but how we'll adapt to these changes.\\n\\n### Call to Action\\nStay informed about AI developments and consider how you can leverage this technology in your own life and career.\\n\\n[End of Script]\",\n  \"message\": \"Your input was invalid. As a result, we've created a script based on a trending topic that is more relevant and engaging.\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
            },
            {
               "type": "text",
               "text": f"<video_topic>\n{request.topic}\n</video_topic>"
            }
         ]
      }
   ]
   
   return get_response(max_tokens=1500, temperature=0.7, system=system, messages=messages, data="")   

@router.post("/ai-video-idea-generator")
def get_video_ideas(request: IdeasRequestModel):
   system="""
      You are a YouTube video idea generator. Your task is to create engaging and catchy ideas for YouTube videos based on a provided keyword. Follow these instructions carefully:

      Your response must always be formatted as a valid JSON object with the following structure:

         {
            "data": ["idea1", "idea2", ... , "idea10"],
            "message": "Success",
            "error": false
         }

      Generate 10 unique and creative video ideas based on the given keyword. Each idea should be a string in the "data" array. Make sure the ideas are diverse and appealing to potential YouTube viewers. 

      If the provided keyword is unclear, nonsensical, or not suitable for generating YouTube video ideas, respond with a JSON object in this format:

         {
            "data": [],
            "message": "The text you provided isn't a clear keyword for a YouTube video. Could you please provide a more specific keyword to generate an idea for a YouTube video?",
            "error": true
         }

      Important reminders:
         1. Do not echo the input prompt in the response.
         2. Handle special characters correctly by escaping them with a backslash.
         3. Ensure your response is always a valid JSON object containing all the required keys ("data", "message", and "error").
         4. The "data" array should always contain exactly 10 ideas when successful, or be empty when there's an error.
         5. The "message" key should contain "Success" for successful responses or an error message for error responses.
         6. The "error" key should be a boolean value: false for successful responses, true for error responses.

      Generate your response now, ensuring it adheres to all the above requirements.
   """
   messages=[
      {
         "role": "user",
         "content": [
               {
                  "type": "text",
                  "text": "<examples>\n<example>\n<example_description>\nIf the user provides a valid keyword then your response should follow this example's ideal output.\n</example_description>\n<KEYWORD>\nfitness motivation\n</KEYWORD>\n<ideal_output>\n{\n  \"data\": [\n    \"10 Morning Habits That Will Transform Your Fitness Journey\",\n    \"From Couch Potato to Fitness Warrior: My 90-Day Transformation\",\n    \"The Psychology of Building Unbreakable Fitness Habits\",\n    \"5 Mindset Shifts That Changed My Fitness Journey Forever\",\n    \"How to Stay Motivated When You Feel Like Giving Up: Fitness Edition\",\n    \"Real People, Real Stories: Inspiring Fitness Transformations\",\n    \"The Science Behind Motivation: Why Some Succeed and Others Don't\",\n    \"Fitness Motivation for Busy People: Making Time for What Matters\",\n    \"Breaking Through Fitness Plateaus: Mental Strategies That Work\",\n    \"Creating Your Fitness Vision Board: Turn Dreams into Reality\"\n  ],\n  \"message\": \"Success\",\n  \"error\": false\n}\n</ideal_output>\n</example>\n<example>\n<example_description>\nIf the user provides an invalid keyword then your response should follow this example's ideal output.\n</example_description>\n<KEYWORD>\nGenerate some trending video ideas\n</KEYWORD>\n<ideal_output>\n{\n  \"data\": [],\n  \"message\": \"The text you provided isn't a clear keyword for a YouTube video. Could you please provide a more specific keyword to generate an idea for a YouTube video?\",\n  \"error\": true\n}\n</ideal_output>\n</example>\n</examples>\n\n"
               },
               {
                  "type": "text",
                  "text": f"<keyword>\n{request.keyword}\n</keyword>"
               }
         ]
      }
   ]
   
   return get_response(max_tokens=300, temperature=0.8, system=system, messages=messages, data=[])   