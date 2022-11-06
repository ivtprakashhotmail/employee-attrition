# employee-attrition project 

Employee are important assets to any organization. The organization spends most of it resource for the employee training. when a employee quits their job unexpectedly. it can result in spending again the same amount of time & resource to groom another resources. 

Retaining skilled employee is an important chanllenges the organization faces. It is important for a organization to understand why the employee leaves and modify its HR policy to retain its employees. 

In this project, with the employee details available within organization, we are going to predict whether the employee leaves the organization or not. 



Data Set: explaination ( filename : employee-attrition.csv)
Important field details. 

1. Age - age of the employee 
2. Attrition - Yes, the employee has left the company. 
3. Business Travel - whether the employee travels for business purpose or not. 
4. DailyRate - The daily charging rate of the employee. 
5. Department - employee department he last worked. 
6. Distance from Home - The distance is miles from the home to office. 
7. Education - The no of college/university degree the employee has. 
8. Education Field - The specialization degree. 
9. Enviornment statisfication - The rating scale. 
10. Gender - gender of the employee 
11. Hourlyrate -Hourly chargable rate 
12. JobLevel - The job grade. 
13. JobRole - The designation 
14. Job Statisfication 
15. Marital Status 
16. Monthly Income 
17. Monthly Rate
18. No of Companies worked
19. Over 18 year exp. 
20. Over Time - 
21. Percent Salary Hike: 
22. Performance Rating - 
23. Relationship Satisfication:- 
24. 

Like this they are 34 details about the employees are available in the dataset. 


Steps: 

notebook.ipynb ( jupiter notebook file)

1.  Data Cleaning 
    a. The column are changed to lower case 
    b. The categorical columns value are converted to local cases and spaces are removed. 
2. EDA 
    a. The correlation and Mutual Exclusion of the features are Analysed. 
3. Model Selection & Parameter Tunning 
    a. Linear Regression provide a accuracy of 87% ( with threshold of 0.6) - The roc auc score is 0.799
    b. Xgboost provide a roc auc is 0.835 ( the parmeter are tunned to achived this eta 0.1 , min child weight 1, no of boost weight: 170 ) 


train_xgboost.ipynb ( Jupiter nodebook file) 

This file contain the xgboost alogorithm with full data training. This file is exported as python to produce train.py

Train.py 

This file is used to train the Model with full date set and save as bentoML model. 

predict.py 

This is the bentoml service file using the expose the prediction as the service. 

bentofile.yaml 

This is the bentoml build file contains all the dependency needed for building the docker image. 





Steps to build the Model and deploy to Docker:- 

1. Run Python train.py to create the bentoml model 

![image](https://user-images.githubusercontent.com/117583458/200181003-737c3f6d-9e52-4bf8-ab1e-46b72efde644.png)



2. Use bentoml models list to find the version of the recently created models. 


3. To build the docker image use the command bentoml build 

![image](https://user-images.githubusercontent.com/117583458/200181221-a07737fb-c89d-458a-9cb4-4fabb8a5f52d.png)

4.  Preapre the docker image  use the command  bentoml containerize employee_attrition:mxywwes53s2xqia6

5. To run the docker image in the local machine. 
    docker run -it --rm -p 3000:3000 employee_attrition:mxywwes53s2xqia6 serve --production
    
    ![image](https://user-images.githubusercontent.com/117583458/200181343-638e11bd-c653-4a9c-ba2a-58e6bd7b9f19.png)

6.  The API is called using the swagger file. 

![image](https://user-images.githubusercontent.com/117583458/200181399-5a7f0250-c7d0-4df1-a0db-0ad351df6656.png)

    
7.  To deploy the docker image to the Kubernetes. 

Enable the kuberntes in the docker desktop. it would start a single node K8 cluster. 

![image](https://user-images.githubusercontent.com/117583458/200181834-53ee9f4e-9606-4256-9212-e3117485fa5a.png)


To deploy the image to the K8 

kubectl create deployment employee-att --image=employee_attrition:mxywwes53s2xqia6

![image](https://user-images.githubusercontent.com/117583458/200183360-145274a8-ad1e-479b-9d82-7a00b16f0c23.png)

This would create the running pod, a depoyment & replicaset

To access the deployed pod easily in the local machine use port-forward

![image](https://user-images.githubusercontent.com/117583458/200183408-27eb9574-6a33-4404-b868-54ed82abf97a.png)


now the API can be access in the http://localhost:3000 

   
    

