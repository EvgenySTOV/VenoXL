<p align="center">
  <img width="800" height="300" src="https://user-images.githubusercontent.com/107706039/182932807-84d6646c-08c7-405d-b743-1f3954e4bce8.jpg">
</p>

# <p align="center"> This web app is very first beta version for VenoXBank which is focusing on non % loan for all clients.</p> 

## <p align="center"> The goal of this app is to help bank customers to make a loan request with their estimated pay date. After that each request will be carefully rewied by bank employee and then you will be contacted via E-mail confirming if you are eligeble for this loan or not. </p>


## FEATURES
- Login/Signup
- Display data
- Add data
- Edit data
- Delete data

## INSTALATION

```bash
git clone https://github.com/EvgenySTOV/VenoX.git
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
## HOW APPLICATION IS WORKING?

### 1. You need to register an account with your personal details (All fields are required)
- *After that all you data will be stored in a database, ensuring that you can login after*
### 2. Go to a loan details page
- *Clicking on loan details 'here' button it's redirecting you on a page displaying all your loan requests (If you have any)*
### 3. Press a button "Make request"
- *After pressing that button, you will be asking to fulfill required fields in order to make request.*
### 4. Now you should see all your existing loan requests
- *There will be 3 tables displaying data from a database*
    <p>First table: Your loan amount </p>
    <p>Second Table: Posted Date </p>
    <p>Third Table: Your estimated pay day </p>
### 5. Now all what you need its - wait.
- *One of our emoloyee is going to review your request and contact you via E-mail*
### 6. In a mean time you can explore our website. You are able to edit your request or even delete it
- *If you changed your mind, you can easily Update(Edit) your request, or even delete it. Close to "Estimated Payday" you should have 'Edit' and 'Delete' buttons.*
### 7. If you want to create a new account or login in another, simply press 'Logout' button on right up corner.
- *You will be redirected on home page*

## HOW PIPELINE IS WORKING?
### A Pipeline is a group of events interlinked with each other in a sequence, the Jenkins server will take to perform the required tasks of the CI/CD process.
> (CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment.)
- Pipeline is a suite of plugins which supports implementing and integrating continuous delivery pipelines into Jenkins
- The scripted pipeline is a traditional way of writing the Jenkins pipeline as code. Scripted pipeline is written in Jenkinsfile. Scripted pipeline strictly uses groovy based syntax. Since this, The scripted pipeline provides huge control over the script and can manipulate the flow of script extensively. This helps developers to develop advance and complex pipeline as code.
- Pipeline is made of different stages, such as build, test and deploy stages. Each stage are declared as commands with parameters and encapsulated in curly brackets
performing a certain task. The Jenkins server then reads the Jenkinsfile and executes its commands, pushing the code down the pipeline from committed source code to production runtime. A Jenkinsfile can be created through a GUI or by writing code directly.

<p align="center">
  <img width="800" height="300" src="https://user-images.githubusercontent.com/107706039/182934438-22146222-5fdb-48d5-bdaf-e9152498c41a.png">
</p>

## EXAMPLE OF PIPELINE SCRIPT
![Declarative Pipeline](https://user-images.githubusercontent.com/107706039/182931938-2c712421-d5af-404b-8e89-fc3ad47f8400.png)

## A FULL CI/CD PIPELINE DIAGRAM WITH INFRASTRUCTURE DIAGRAM
1
