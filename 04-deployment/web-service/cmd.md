pipenv shell
PS1=">"
gunicorn --bind=0.0.0.0:9696 predict:app

docker build -t ride-duration-prediction-service:v1 .

docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1