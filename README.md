# NLP-workout-tracker 🏋🏻‍♀️
A workout tracker built in python, that converts a sentence expressed in natural language into workout data, stored in a Google Sheets document. 

![Screenshot 2022-09-08 at 17 16 40](https://user-images.githubusercontent.com/76702446/189160290-eba34412-3ab7-43dd-8f48-894f5afc4717.png)

![Screenshot 2022-09-08 at 17 17 48](https://user-images.githubusercontent.com/76702446/189160532-ddf12ff3-fa27-423b-adf7-f554b51d6774.png)


## Installation
1. Create a Nutritionxi account to use the API, and get the **API Key** and **app ID**.
2. Create two variables called **NUTRITIONIX_KEY** and **NUTRITIONIX_APP_ID** and assign the corrisponding data to them.
3. Create a Google Sheets document, and add make sure the structure is identical to the one down below.

> ![Screenshot 2022-09-08 at 16 53 55](https://user-images.githubusercontent.com/76702446/189154912-9f61e514-a6fd-4b74-b717-4a038df752dc.png)

4. Create a Sheety account and setup a project, linking your Google Sheets document.
5. Create a Basic or Bearer authentication key on the Sheety dashboard and assign its value to a new environment variable called **SHEETY_AUTH**.
