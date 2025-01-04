from helpers.testing_helper import helper_func

youtube_url = "http://127.0.0.1:8000/youtube"
instagram_url = "http://127.0.0.1:8000/instagram"
tiktok_url = "http://127.0.0.1:8000/tiktok"
content_creation_url = "http://127.0.0.1:8000/content-creation"

# ! Youtube

def test_valid_yt_hashtag_generator():
   url = youtube_url+"/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "urdu"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)
   
def test_inValid_yt_hashtag_generator():
   url = youtube_url+"/hashtag-generator"
   payload = {
      "topic": "Gta 10 release date",
      "lang": "blnk"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=str)
   
def test_valid_yt_description_generator():
   url = youtube_url+"/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Saudi Arabia Built a $16BN Clock Tower"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)
   
def test_inValid_yt_description_generator():
   url = youtube_url+"/description-generator"
   payload = {
      "video_size": "shorts",
      "topic": "Sodqidw01298"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=str)
   
def test_valid_yt_title_generator():
   url = youtube_url+"/title-generator"
   payload = {
      "details": "A tutorial on creating modern websites using HTML, CSS, and JavaScript"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=list)
   
def test_inValid_yt_titles_generator():
   url = youtube_url+"/title-generator"   
   payload = {
      "details": "A12098diwj"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=list)
   
def test_valid_yt_usernames_generator():
   url = youtube_url + "/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=list)
   
def test_inValid_yt_usernames_generator():
   url = youtube_url+"/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=list)

# ! Instagram 
   
def test_valid_ig_usernames_generator():
   url = instagram_url+"/username-generator"
   payload = {
      "name": "John Doe",
      "topic": "Technology and Gadgets",
      "description": "A fun and informative vibe for tech enthusiasts"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=list)
   
def test_inValid_ig_usernames_generator():
   url = instagram_url+"/username-generator"
   payload = {
      "name": "blajskl",
      "topic": "*5662+",
      "description": "lwdijaww"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=list)

def test_valid_ig_caption_generator():
   url = instagram_url+"/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)
   
def test_inValid_ig_caption_generator():
   url = instagram_url+"/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=str)

# ! Tiktok 
   
def test_valid_tt_caption_generator():
   url = tiktok_url+"/caption-generator"
   payload = {
      "topic": "A cute puppy playing with a ball"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)
   
def test_inValid_tt_caption_generator():
   url = tiktok_url+"/caption-generator"
   payload = {
      "topic": "5/*+662"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=str)
   
def test_valid_tt_hashtags_generator():
   url = tiktok_url+"/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "اُردُو"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)
   
def test_inValid_tt_hashtags_generator():
   url = tiktok_url+"/hashtag-generator"
   payload = {
      "topic": "Cooking tips",
      "lang": "blakk"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=str)
   
# # ! Content-Creation 

def test_valid_cc_video_hooks_generator():
   url = content_creation_url+"/video-hook-generator"
   payload = {
      "topic": "How to make a viral TikTok video",
      "target_audience": "TikTok creators and influencers", 
      "context": "This video will discuss tips and tricks for creating engaging content on TikTok that has the potential to go viral."
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=list)
   
def test_inValid_cc_video_hooks_generator():
   url = content_creation_url+"/video-hook-generator"
   payload = {
      "topic": "/*+48",
      "target_audience": "afopsjc/*-+", 
      "context": "aposc/*-+"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=list)
      
def test_valid_cc_video_script_generator():
   url = content_creation_url+"/video-script-generator"
   payload = {
      "topic": "Why Saudi Arabia is Building a $1 Trillion City in the Desert"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=str)

def test_valid_cc_video_ideas_generator():
   url = content_creation_url+"/ai-video-idea-generator"
   payload = {
      "keyword": "Beginner's Guide to Python REST Framework"
   }
   helper_func(url=url, payload=payload, status_code=200, error=False, data_type=list)
   
def test_inValid_cc_video_ideas_generator():
   url = content_creation_url+"/ai-video-idea-generator"
   payload = {
      "keyword": "basjkasjj/*-+63"
   }
   helper_func(url=url, payload=payload, status_code=400, error=True, data_type=list)