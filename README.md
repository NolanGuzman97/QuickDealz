# QuickDealz
A React Native app that scours the vast internet for great deals


Prerequisites: 
1. Install python 3.7.4
2. Install VisualStudioCode(Chosen IDE)
3. Install Xcode(can utilize the simulator for testing if needed)
4. Install Docker and Docker-Compose

Setup? (DEFINETLEY A work in progress)

1. Open the terminal and cd to your Desktop. Clone the directory using ```git clone git@github.com:NolanGuzman97/QuickDealz.git``` (Highly reccomend you setup ssh keys, it is a good habit)
2. cd into newly cloned git repository named QuickDealz
3. Setup your python environment. Start with running ```python3.7 -m venv QDEnv```
4. Now run ```source env /bin/activate```. You should now be in your own python dev environment.
5. Now run ``` pip3.7 install -r requirements.txt```
6. Your python environment is now ready to go.
7. Now let's setup your docker for testing
8. Start up docker with ```docker-compose up -d``` and verify that you see the container with ```docker ps```
9. Once that is done, go ahead and startup the backend with ```python3.7 wsgi.py```
10. Open up google chrome and navigate to [http://localhost:5000](http://localhost:5000)
11. You should be able to see the swagger page allowing you to test the API calls
12. Go ahead and click on POST /api/v1/users and then press the "Try it Out!" button
to make a test api call
13. Use a real email address as the program will send you an activation email for a user account. The rest doesn't matter so long as the passwords match.
14. Check you email and click the activation link. If you a see a success call on the redirected page then you are ready to go!
15. Now let's setup the front end. cd to QuickDealzApp and run ```npm install```
16. Once that has completed try ```npm start```
17. Navigate to [http://localhost:8081](http://localhost:8081) and test to see if react native packager is running.
18. The rest is TBD

Docker Neccessary Good To Know command lines:
1. ```docker-compose up -d``` This will setup the docker container that you need.
2. ```docker container stop $(docker container ls -aq)``` This will stop all running containers
3. ```docker rmi $(docker images -q)``` In case of error this will remove all containers and images (Use Carefully if you have other important docker containers! This deletes ALL running images)
4. ```docker exec -it quickdealz_mongo_1 mongo -u mongoadmin -p password``` This will allow you to ssh into the mongo database and check out things like the schema, collections, etc. (This is admin privliges so you can empty database, manually populate, etc. if needed)
    1. Once in database to currently check user database use command ```use todo_inventory```
    2. To view contents of the collection and check that your api call was successful use ```db.users.find({})```