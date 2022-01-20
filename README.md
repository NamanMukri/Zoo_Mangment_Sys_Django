Zoo Management App 
1. Created a Django app named animals<br />
2. Created 3 models in animals app -> Mammal, Bird and Fish with features mentioned above<br />
6. Created views to Get and POST Data for Mammals, Bird, Fish Models Hint: Use ORM<br />
7. For Views and Urls More Details are given below <br />



**Expected Ip/Op**


**Part 1: GET, POST, PUT and DELETE request for fetching Mammals**

**Django URL name: mammals**<br />
No parameter<br />

**Actions**:<br />
1. GET - get list of all or one mammal<br />
2. POST - Add a new mammal to the Zoo<br />
3. PUT - Feed the Mammal i.e **Update last_feed_time to current time**<br />
4. DELETE - Remove Animal from the zoo<br />
<br />

      1. GET:
         Part 1:
            
            Response Data format {"data": [name,species,gender,food]}
            If no data is present
            /animals/mammals/
            Response -> {‘data’: []}


            /animals/mammals
             Response ->{"data": [["lion", "Panthera", "M", "meat"], ["tiger", "Panthera", "M", "chicken"]]}
        
        Part 2:
             Response Data format {"name": name, "species": species, "gender": gender, "food": food}
            /animals/mammals/lion
             Response ->{"name": "lion", "species": "Panthera", "gender": "M", "food": "meat"}


      2. POST
      Response Data format {"created": {"name": name}}
      /animals/mammals/ -d "name=lion&species=Panthera&gender=M&food=meat"
      Response -> {"created": {"name": "lion"}}
      
      3. PUT
      Response Data format {"Feeded": name}
      /animals/mammals/lion
      Response -> {"Feeded": "lion"}
      
      4. DELETE 
      Response Data format {"Deleted ": name}
      /animals/mammals/lion
      Response -> {"Deleted": "lion"}
 
 
**Part 2: GET, POST, PUT and Delete request for fetching Birds<br />**

**Django URL name: birds**<br />
No parameter<br />

**Actions**:<br />
1. GET - get list of all or one Birds<br />
2. POST - Add a new bird to the Zoo<br />
3. PUT - Feed the Bird i.e **Update last_feed_time to current time**<br />
4. DELETE - Remove Bird from the zoo<br />
<br />
 
      1. GET:
      Part 1:
            Response Data format {"data": [name,species,food]}
            If no data is present
            /animals/birds/
            Response -> {"data": []}

            /animals/birds/
             Response ->{"data": [["Parrot", "parrata", "insects"]]}
          
       Part 2:
             Response Data format {"name": name, "species": species, "food": food}
            /animals/birds/Parrot
             Response ->{"name": "Parrot", "species": "parrata", "food": "insects"}
       


      2. POST
      Response Data format {"created": {"name": name}}
      /animals/birds/ -d "name=Parrot&species=parrata&food=insects"
      Response -> {"created": {"name": "Parrot"}}
      
      3. PUT
      Response Data format {"Feeded": name}
      /animals/birds/Parrot
      Response -> {"Feeded": "Parrot"}
      
      4. DELETE 
      Response Data format {"Deleted ": name}
      /animals/birds/Parrot
      Response -> {"Deleted": "Parrot"}

 
**Part 3: GET, POST and DELETE request for fetching Fishes<br />**
<br />

**Django URL name: fishes**<br />
No parameter<br />

**Actions**
1. GET - get list of all or one Fish species<br />
2. POST - Add a new fish species to the Zoo<br />
3. PUT - Feed the Fish species i.e **Update last_feed_time to current time**<br />
4. DELETE - Remove Fish species from the zoo<br />
 
            1. GET:
              Part 1:
                  Response Data format {"data": [name,species,food]}

                  If no data is present
                  /animals/fishes/
                  Response -> {"data": []}

                  /animals/fishes/
                  Response ->{"data": ["yellow", "GoldFisha", "grain", 100]}

             Part 2:
                   Response Data format {"color": color, "species": species, "food": food,"count" : count }
                  /animals/fishes/GoldFisha
                   Response ->{"color": "yellow", "species": "GoldFisha", "food": "grain", "count": 100}


            2. POST
            Response Data format {"created": {"species": species}}
            /animals/fishes/ -d "color=yellow&species=GoldFisha&food=grain&count=2000"
            Response -> {"created": {"species": "GoldFisha"}}

            3. PUT
            Response Data format {"Feeded": species}
            /animals/fishes/GoldFisha
            Response -> {"Feeded": "GoldFisha"}

            3. DELETE 
            Response Data format {"Deleted ": species}
            /animals/fishes/GoldFisha
            Response -> {"Deleted": "GoldFisha"}


