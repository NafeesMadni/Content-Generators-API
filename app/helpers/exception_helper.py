from fastapi.responses import JSONResponse

def get_exception_response(data, message, status_code):
   return JSONResponse(
      content={
         "data": data,
         "message": message,
         "error": True
      }, 
      status_code=status_code
   )