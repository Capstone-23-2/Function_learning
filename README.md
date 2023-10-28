Fast api server for conversation using Palm2 api
For Python>=3.6

1. Create key.py in ./common directory
   in key.py
   palm_api_key='Your api key'
2. run $sudo apt install python3.10 #if python not installed
3. run $sudo apt install python3-pip #pip version 22.0.2
4. run $pip install -r requirements.txt
5. $python3 -m uvicorn main:app --host=0.0.0.0 --port=80
