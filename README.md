curl http://127.0.0.1:5000/meals -X POST -H"Content-Type:aplication/json" -d'{"affordability": "2","category": 1,"complexity": "easy","duration": "45","glutenfree": rue,"id": 1,"imageUrl": "https://lh3.googleusercontent.com/UV4RzNqnf4yL0c5AYRdxL22rDyZiH3as-p6ipLIqLGcTtEDqDZoXgg1wNa8XpYtvwYbOcMWco5R01GhHbEHaA=w1200-h1200-c-rj-v1-e365","ingredients": [],"lactosefree": true,"steps": "not ready yet","title": "Chicken curry hotpot","vegan": false,"vegetarian": false,"ingredients":"'onion':3},{'tomato':4}"}'

curl https://mealschedule.herokuapp.com/ingredients -X POST H"Content-Type: application/json"  -d'{"
name":"onion","quantity":1}'

$ curl http://127.0.0.1:5000/ingredients -X POST -H"Content-Type: application/json"  -d'{"
name":"onion","quantity":1}'