import requests

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
