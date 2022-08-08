<p align="center">
  <img width="800" height="300" src="https://user-images.githubusercontent.com/107706039/182932807-84d6646c-08c7-405d-b743-1f3954e4bce8.jpg">
</p>

# <p align="center"> This web app is very a first beta version for VenoXBank which is focusing on non % loan for all clients.</p> 

## <p align="center"> The goal of this app is to help bank customers to make a loan request with their estimated pay date. After that each request will be carefully rewied by bank employee and then you will be contacted via E-mail confirming if you are eligeble for this loan or not. </p>

### SCOPE 
This project will be based upon:
* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

## FEATURES
- Login/Signup
- Display data
- Add data
- Edit data
- Delete data

## HOW TO INSTALL
1. Update and install the necessary packages
```
         sudo apt update && sudo apt install python3 python3-venv python3-pip
```
2. Clone the repo & cd into the directory
```
         git clone https://github.com/EvgenySTOV/VenoXL.git
```
3. Initiate the virtual environment
```
         python3 -m venv venv
``` 
4. Activate the virtual environment
```
         source venv/bin/activate (Ubuntu) or source venv/Scripts/activate (Windows)
```
5. Install the requirements
```
         pip3 install -r requirements.txt
```
6. Log into MySQL
```
         sudo mysql -u root
```
7. Create the user which matches what is written in app.py
```
         CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
```
8. Grant the necessary privileges to the newly created user
```
         GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
```
9. Flush the privileges to update the privileges table
```
         FLUSH PRIVILEGES;
```
10. Create the database which matches the database name written in app.py
```
         CREATE DATABASE venox1;
```
11. Exit out of MySQL
```
         EXIT
```
12. Create the tables
```
         python3 create.py
```
13. Start the app
```
         python3 run.py        
```  
14. Deactive the virtual environment
```
         deactivate
```

## HOW APPLICATION IS WORKING?

### 1. You need to register an account with your personal details (All fields are required)
- *After that all your data will be stored in a database, ensuring that you can login after*
### 2. Go to a loan details page
- *Clicking on loan details 'here' button it's redirecting you on a page displaying all your loan requests (If you have any)*
### 3. Press a button "Make request"
- *After pressing that button, you will be asking to fulfill required fields in order to make request.*
### 4. Now you should see all your existing loan requests
- *There will be a table displaying data from a database*
    <p>First Row: Your loan amount </p>
    <p>Second Row: Your estimated pay day </p>
### 5. Now all what you need its - wait.
- *One of our emoloyee is going to review your request and contact you via E-mail (Not 100% confirmed :))*
### 6. In a mean time you can explore our website. You are able to edit your request or even delete it!

- *If you changed your mind, you can easily Update(Edit) your request, or even delete it. Close to "Estimated Payday" you should have 'Edit' and 'Delete' buttons.*
### 7. If you want to create a new account or login in another, simply press 'Logout' button on right up corner.
- *You will be redirected on home page*

## DEMONSTRATING CRUD FUNCTIONALITY
https://drive.google.com/file/d/1Z0J06FQsifmxtYovkdH2jIavDsiLxmrt/view?usp=sharing

## HOW PIPELINE IS WORKING?
### A Pipeline is a group of events interlinked with each other in a sequence, the Jenkins server will take to perform the required tasks of the CI/CD process.
> (CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment.)
- Pipeline is a suite of plugins which supports implementing and integrating continuous delivery pipelines into Jenkins. The scripted pipeline is a traditional way of writing the Jenkins pipeline as code. Scripted pipeline is written in Jenkinsfile. *Scripted* pipeline strictly uses groovy based syntax. Since this, The scripted pipeline provides huge control over the script and can manipulate the flow of script extensively. This helps developers to develop advance and complex pipeline as code. Pipeline is made of different stages, such as build, test and deploy stages. Each stage are declared as commands with parameters and encapsulated in curly brackets performing a certain task. The Jenkins server then reads the Jenkinsfile and executes its commands, pushing the code down the pipeline from committed source code to production runtime.
<br>
- Declarative Checkout SCM - The first stage triggered by a webhook is the source code management acquisition where jenkins will create a blank workspace and navigate to the github url repository clone it, switch into it and then checkout to the specified branch.
<br>
<br>
- Testing - The second stage is the application testing stage where both the front-end and back-end will be testing using the specified bash testing script, test files and test tool.
<br>
<br>
- Build Images - The third stage is the dockerization of the front-end and the back-end using the docker-compose.yaml to build the contents into a snapshop image with all the required dependencies to deploy the application as a container or pod.  
<br>
<br>
- Push - The fourth stage push`s the docker images built in the previous stage to dockerhub. 
<br>
<br>
- Deployment - The fifth and final stage of the pipeline is to pulldown the previously built docker images from dockerhub, then deploy them in the terraform built kubernetes cluster using the bash deployment.sh script.
<br>

## SOFTWARE APPLICATION DESIGN
![24](https://user-images.githubusercontent.com/107706039/183316551-46f1c383-161f-426b-b272-ca31f863f051.png)

## MY FULL CI/CD PIPELINE DIAGRAM
![444](https://user-images.githubusercontent.com/107706039/183322737-1eeccc12-d255-4c11-ac50-0ae1ab1e861d.png)

## KANBAN/JIRA BOARD
![Screenshot (1)](https://user-images.githubusercontent.com/107706039/183324561-70981643-3c3a-483b-b2ae-f20c56dee024.png)

## FUTURE IMPROVEMENTS
- Adding more complex design
- Make it more user friendly
- Improve testing coverage..
![271442874_351378523482441_3078156453661238674_n](https://user-images.githubusercontent.com/107706039/183329544-311d114e-0131-41ee-bcca-8eafd5778e18.gif)
- Secret keys unsecure
- Deploy using gunicorn
- Add NGINX
- Project structure and more 'clean' code

## CONCLUSION
From this bootcamp my IT journey has started. Say that it was intense and challenging for me - it's say nothing. But I learnt a lot, and even more is ahead. This was very interesting and exciting expirience for me for sure. I clearly understand, that my project is not covering all required scopes, but I did my best with writing backend/frontend code (Google was my biggest ally), configuring system, "figting" with errors and tools/software confrontation, must to reinstall Windows after an issue when put my hands not in a right place haha. Sad, that I have discovered project details too late. The thing is, that I made too complex ERD at the beginning and tried to stick with it, wasted my time on building things which were dropped at the end anyway. The project also helped me identify which skills I needed to improve and, even better, helped me improve those very same skills. I was able to learn from the first project by examining how I complete my work and how effectively I complete it. This has helped give me a baseline of how much time it takes to complete parts of the project which allows me to manage my time better. My next goal is to continue pushing and dive deeper into Cloud/DevOps world and find my very first job there. 
