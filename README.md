# SETUP
- follow https://wiki.python.org/moin/BeginnersGuide/Download to install python
- go to root directory "API_Assets" and run `pip install -r ./requirements.txt` to install all needed
dependencies
- add ".env" file to root directory 
# RUNNING 
- to run server write `uvicorn main:app` into cmd in root directory 
 Server should be running on : http://127.0.0.1:8000 
 To get access to Swagger UI you should follow http://127.0.0.1:8000/docs
