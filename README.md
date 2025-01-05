# Social Media Content Generator API 🚀
 
A FastAPI-powered application that leverages Claude AI (Anthropic) to generate diverse content for social media platforms, including YouTube, Instagram, and TikTok. The application is being expanded to include video downloading capabilities for Reddit, Facebook, Instagram, LinkedIn, X (formerly Twitter), Pinterest, and TikTok (currently under development).

## Features 

### YouTube Tools 🎥
- **Description Generator**: Creates optimized descriptions for both long and short-form videos
- **Hashtag Generator**: Generates platform-specific hashtags in multiple languages
- **Title Generator**: Creates 10 catchy video titles based on provided details
- **Username Generator**: Suggests creative channel usernames based on name, topic, and style

### Instagram Tools 📸
- **Caption Generator**: Creates engaging captions with relevant emojis and hashtags
- **Username Generator**: Generates Instagram-specific usernames following platform guidelines

### TikTok Tools 📱
- **Caption Generator**: Creates platform-optimized captions with trending hashtags
- **Hashtag Generator**: Produces relevant hashtags in multiple languages

### Content Creation Tools ✍️

- **Video Hook Generator**: Creates 10 engaging hooks based on topic, target audience, and context
- **Video Script Generator**: Produces well-structured, markdown-formatted video scripts
- **Video Idea Generator**: Generates 10 creative video ideas from keywords

## Technology Stack

- **Framework**: FastAPI
- **AI Model**: claude-3-5-sonnet-20241022 (Anthropic)
- **Python Libraries**:
  - anthropic
  - pydantic
  - python-dotenv
  - fastapi

## Installation

Install the dependencies:
```bash
pip install -r requirements.txt
```

## Getting Started

1. Set up your environment variables:
```
ANTHROPIC_API_KEY=your_api_key_here
```

2. Run the project:
```bash
uvicorn main:app --reload
```
The API will be available at `http://localhost:8000`

3. Access the API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### YouTube Endpoints
```
POST /youtube/description-generator
POST /youtube/hashtag-generator
POST /youtube/title-generator
POST /youtube/username-generator
```

### Instagram Endpoints
```
POST /instagram/caption-generator
POST /instagram/username-generator
```

### TikTok Endpoints
```
POST /tiktok/caption-generator
POST /tiktok/hashtag-generator
```

### Content Creation Endpoints
```
POST /content-creation/video-hook-generator
POST /content-creation/video-script-generator
POST /content-creation/ai-video-idea-generator
```

## Key Features

- **Multi-platform Support**: Generates content for YouTube, Instagram, and TikTok
- **Language Support**: Multilingual hashtag generation
- **Error Handling**: Robust error handling with appropriate HTTP status codes
- **Input Validation**: Request validation using Pydantic models
- **Consistent Response Format**: Standardized JSON responses across all endpoints

## Response Format

All endpoints return responses in the following JSON format:
```json
{
    "data": "<generated_content>",
    "message": "Success | Error",
    "error": false | true
}
```

## Error Handling

The API implements comprehensive error handling:
- 200: Successful response
- 400: Bad request (invalid input)
- 500: Internal server error

## Environment Setup
Add `.env` file in the root directory.
Required environment variables:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Testing

Tests can be run using pytest:
```bash
pytest app/free_tools/testing/test_api.py
```

---
*Note: This API utilizes claude-3-5-sonnet-20241022 for content generation. Ensure you have the necessary API credentials before deployment.*
