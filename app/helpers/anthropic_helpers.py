import json, anthropic, os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .exception_helper import get_exception_response
from constants import MODEL, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, FAIL_RESPONSE


load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def get_response(max_tokens, temperature, system, messages, data):
   try:
      response = client.messages.create(
         model=MODEL,
         temperature=temperature,
         max_tokens=max_tokens,
         system=system,
         messages=messages
      )
      try:
         res = json.loads(response.content[0].text)
         if res["error"]:
            return JSONResponse(content=res, status_code=HTTP_400_BAD_REQUEST)
         else: 
            return JSONResponse(content=res, status_code=HTTP_200_OK)
      
      except json.JSONDecodeError:
         return get_exception_response(data=data, message=FAIL_RESPONSE, status_code=HTTP_400_BAD_REQUEST)
         
   except Exception as e:
      return get_exception_response(data=data, message=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)