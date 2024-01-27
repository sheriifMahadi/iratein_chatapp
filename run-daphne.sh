daphne -b -0.0.0.0 -p 8000 core.asgi:application 
docker run -p 6379:6379 -d redis:5
