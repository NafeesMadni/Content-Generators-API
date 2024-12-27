import requests


# ! Youtube
def test_valid_yt_hashtag_generator():
   url = "http://127.0.0.1:8000/youtube/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "urdu"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()
   
   # Assert the response structure and values
   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success", "Message field value mismatch"
   assert response_data["error"] is False, "Error field value mismatch"
   
   # validation for "data" should be a string 
   assert isinstance(response_data["data"], str), "'data' field should be a string"

   print("Test passed successfully!")
   
def test_inValid_yt_hashtag_generator():
   url = "http://127.0.0.1:8000/youtube/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "blnk"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!", "Message field value mismatch"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
def test_valid_yt_description_generator():
   url = "http://127.0.0.1:8000/youtube/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Saudi Arabia Built a $16BN Clock Tower"
   }

   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
def test_inValid_yt_description_generator():
   url = "http://127.0.0.1:8000/youtube/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Sodqidw01298"
   }

   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video."
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"

def test_valid_yt_title_generator():
   url = "http://127.0.0.1:8000/youtube/title-generator"
   payload = {
      "details": "A tutorial on creating modern websites using HTML, CSS, and JavaScript"
   }

   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_inValid_yt_titles_generator():
   url = "http://127.0.0.1:8000/youtube/title-generator"
   payload = {
      "details": "A12098diwj"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I'm sorry, but the text you provided doesn't seem to be a clear topic or script for a YouTube video. Could you please provide a more specific topic or script idea?"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_valid_yt_usernames_generator():
   url = "http://127.0.0.1:8000/youtube/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_inValid_yt_usernames_generator():
   url = "http://127.0.0.1:8000/youtube/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }

   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I'm here to help you generate creative and catchy YouTube usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
      
# ! Instagram 
   
def test_valid_ig_usernames_generator():
   url = "http://127.0.0.1:8000/instagram/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_inValid_ig_usernames_generator():
   url = "http://127.0.0.1:8000/instagram/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I'm here to help you generate creative and catchy Instagram usernames. Please provide the following details: \n   1. Your full name. \n   2. The theme or topic of your account. \n   3. A brief description of the style or vibe you want for your username.\nOnce you provide this information, I can suggest some personalized username ideas for you!"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_valid_ig_caption_generator():
   url = "http://127.0.0.1:8000/instagram/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
def test_inValid_ig_caption_generator():
   url = "http://127.0.0.1:8000/instagram/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Please provide a valid topic to generate caption."
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   

# ! Tiktok 
   
def test_valid_tt_caption_generator():
   url = "http://127.0.0.1:8000/tiktok/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
def test_inValid_tt_caption_generator():
   url = "http://127.0.0.1:8000/tiktok/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Please provide a valid topic to generate caption."
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
      
def test_valid_tt_hashtags_generator():
   url = "http://127.0.0.1:8000/tiktok/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "اُردُو"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
def test_inValid_tt_hashtags_generator():
   url = "http://127.0.0.1:8000/tiktok/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "blakk"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I can only assist with recognized languages. Some examples of valid languages include English, Urdu, Hindi, and more. Kindly provide your request in a supported language to ensure I can help effectively!"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a string"
   
   
# ! Content-Creation 

def test_valid_cc_video_hooks_generator():
   url = "http://127.0.0.1:8000/content-creation/video-hook-generator"
   payload = {
      "topic": "How to make a viral TikTok video",
      "target_audience": "TikTok creators and influencers", 
      "context": "This video will discuss tips and tricks for creating engaging content on TikTok that has the potential to go viral."
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
   
def test_inValid_cc_video_hooks_generator():
   url = "http://127.0.0.1:8000/content-creation/video-hook-generator"
   payload = {
      "topic": "/*+48",
      "target_audience": "afopsjc/*-+", 
      "context": "aposc/*-+"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "I'm sorry, but the input you provided doesn't seem to be clear for a hook video. Could you please provide valid video topic, target_audience, or context?"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
      
def test_valid_cc_video_script_generator():
   url = "http://127.0.0.1:8000/content-creation/video-script-generator"
   payload = {
      "topic": "Why Saudi Arabia is Building a $1 Trillion City in the Desert"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], str), "'data' field should be a str"

def test_valid_cc_video_ideas_generator():
   url = "http://127.0.0.1:8000/content-creation/ai-video-idea-generator"
   payload = {
      "keyword": "Beginner's Guide to Python REST Framework"
   }

   response = requests.post(url, json=payload)

   assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "Success"
   assert response_data["error"] is False, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"
      
def test_inValid_cc_video_ideas_generator():
   url = "http://127.0.0.1:8000/content-creation/ai-video-idea-generator"
   payload = {
      "keyword": "basjkasjj/*-+63"
   }
   response = requests.post(url, json=payload)

   assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
   
   response_data = response.json()

   assert "data" in response_data, "Missing 'data' field in response"
   assert "message" in response_data, "Missing 'message' field in response"
   assert "error" in response_data, "Missing 'error' field in response"
   assert response_data["message"] == "The text you provided isn't a clear keyword for a YouTube video. Could you please provide a more specific keyword to generate an idea for a YouTube video?"
   assert response_data["error"] is True, "Error field value mismatch"
   
   assert isinstance(response_data["data"], list), "'data' field should be a list"