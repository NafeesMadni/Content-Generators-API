import requests
# from ...helpers.testing_helper import helper_func
# from constants import HTTP_200_OK, HTTP_400_BAD_REQUEST

youtube_url = "http://127.0.0.1:8000/youtube"
instagram_url = "http://127.0.0.1:8000/instagram"
tiktok_url = "http://127.0.0.1:8000/tiktok"
content_creation_url = "http://127.0.0.1:8000/content-creation"

def helper_func(url, payload, status_code, message, error, data_type):
   response = requests.post(url, json=payload)

   assert response.status_code == status_code, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()
   
   # Assert the response structure and values
   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   
   assert response_data["message"] == message
   assert response_data["error"] is error, "Error field value mismatch"
   
   # validation for "data" should be a string 
   assert isinstance(response_data["data"], data_type), f"'data' field should be a {data_type}"

# ! Youtube

def test_valid_yt_hashtag_generator():
   url = youtube_url+"/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "urdu"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)
   
def test_inValid_yt_hashtag_generator():
   url = youtube_url+"/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "blnk"
   }
   message = "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=str)
   
def test_valid_yt_description_generator():
   url = youtube_url+"/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Saudi Arabia Built a $16BN Clock Tower"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)
   
def test_inValid_yt_description_generator():
   url = youtube_url+"/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Sodqidw01298"
   }
   message = "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video."
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=str)
   
def test_valid_yt_title_generator():
   url = youtube_url+"/title-generator"
   payload = {
      "details": "A tutorial on creating modern websites using HTML, CSS, and JavaScript"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=list)
   
def test_inValid_yt_titles_generator():
   url = youtube_url+"/title-generator"   
   payload = {
      "details": "A12098diwj"
   }
   message = "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video. Could you please provide a more specific topic or script idea?"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=list)
   
def test_valid_yt_usernames_generator():
   url = youtube_url + "/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=list)
   
def test_inValid_yt_usernames_generator():
   url = youtube_url+"/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }
   message = "I'm here to help you generate creative and catchy YouTube usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=list)

# ! Instagram 
   
def test_valid_ig_usernames_generator():
   url = instagram_url+"/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=list)
   
def test_inValid_ig_usernames_generator():
   url = instagram_url+"/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }
   message = "I'm here to help you generate creative and catchy Instagram usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=list)

def test_valid_ig_caption_generator():
   url = instagram_url+"/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)
   
def test_inValid_ig_caption_generator():
   url = instagram_url+"/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   message = "Please provide a valid topic to generate caption."
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=str)

# ! Tiktok 
   
def test_valid_tt_caption_generator():
   url = tiktok_url+"/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)
   
def test_inValid_tt_caption_generator():
   url = tiktok_url+"/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   message = "Please provide a valid topic to generate caption."
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=str)
   
def test_valid_tt_hashtags_generator():
   url = tiktok_url+"/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "اُردُو"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)
   
def test_inValid_tt_hashtags_generator():
   url = tiktok_url+"/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "blakk"
   }
   message = "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=str)
   
# # ! Content-Creation 

def test_valid_cc_video_hooks_generator():
   url = content_creation_url+"/video-hook-generator"
   payload = {
      "topic": "How to make a viral TikTok video",
      "target_audience": "TikTok creators and influencers", 
      "context": "This video will discuss tips and tricks for creating engaging content on TikTok that has the potential to go viral."
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=list)
   
def test_inValid_cc_video_hooks_generator():
   url = content_creation_url+"/video-hook-generator"
   payload = {
      "topic": "/*+48",
      "target_audience": "afopsjc/*-+", 
      "context": "aposc/*-+"
   }
   message = "I'm sorry, but the input you provided doesn't seem to be clear for a hook video. Could you please provide valid video topic, target_audience, or context?"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=list)
      
def test_valid_cc_video_script_generator():
   url = content_creation_url+"/video-script-generator"
   payload = {
      "topic": "Why Saudi Arabia is Building a $1 Trillion City in the Desert"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=str)

def test_valid_cc_video_ideas_generator():
   url = content_creation_url+"/ai-video-idea-generator"
   payload = {
      "keyword": "Beginner's Guide to Python REST Framework"
   }
   helper_func(url=url, payload=payload, status_code=200, message="Success", error=False, data_type=list)
   
def test_inValid_cc_video_ideas_generator():
   url = content_creation_url+"/ai-video-idea-generator"
   payload = {
      "keyword": "basjkasjj/*-+63"
   }
   message = "The text you provided isn't a clear keyword for a YouTube video. Could you please provide a more specific keyword to generate an idea for a YouTube video?"
   helper_func(url=url, payload=payload, status_code=400, message=message, error=True, data_type=list)