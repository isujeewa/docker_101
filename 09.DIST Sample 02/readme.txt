is used to create a .tar archive of the file random_numbers_api.py and store it in the dist directory under the name app.tar.

tar -cvf dist/app.tar random_numbers_api.py  


docker build -t flask-app-tar-demo .
docker run -p 5122:5122 flask-app-tar-demo

http://localhost:5122/random-numbers

