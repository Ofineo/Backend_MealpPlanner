curl  https://mealschedule.herokuapp.com/meals -X POST -H"Content-Type: application/json" -d'{"affordability": "","category": 0,"complexity": "","duration": "","glutenfree": true,"imageUrl": "","lactosefree": true,"steps": [],"title": "Only for list of veggies","vegan": true,"vegetarian": true}'

curl  https://mealschedule.herokuapp.com/meals -X POST -H"Content-Type: application/json" -d'{"affordability": "2","category": 1,"complexity": "easy","duration": "45","glutenfree": true,"id": 1,"imageUrl": "https://media.self.com/photos/5862946e788377c57db95a08/master/pass/raw-diet-pros-cons.jpg","lactosefree": true,"steps": [1,2,3,4],"title": "Chicken curry hotpot","vegan": false,"vegetarian": false,"ingredients":[{"name":"onion","quantity":3,"meal_id":"1"},{"name":"asparragus","quantity":7,"meal_id":"1"}]}'


curl http://127.0.0.1:5000/meals -X POST -H"Content-Type: application/json" -d'{"affordability": "2","category": 1,"complexity": "easy","duration": "45","glutenfree": true,"id": 1,"imageUrl": "https://media.self.com/photos/5862946e788377c57db95a08/master/pass/raw-diet-pros-cons.jpg","lactosefree": true,"steps": [1,2,3,4],"title": "Chicken curry hotpot","vegan": false,"vegetarian": false,"ingredients":[{"name":"onion","quantity":3,"meal_id":"1"},{"name":"asparragus","quantity":7,"meal_id":"1"}]}'

curl https://mealschedule.herokuapp.com/ingredients -X POST -H"Content-Type: application/json"  -d'{" 
name":"chorizo","quantity":1, "meal_id": 1}'


$ curl http://127.0.0.1:5000/ingredients -X POST -H"Content-Type: application/json"  -d"{" 
name":"chorizo","quantity":1, "meal_id": 1}"