#shipping_app 

# ABOUT
It's the simple REST-API project developer using Django Rest Framework.
Includes standard functions providing database store handling by calling http-requests.

# BUILT IN
- Python v3.9;
- DRF v3.14;
- Advanced logging package: Loguru;
- DBMS: PostgreSQL;
- Geographical data extension: GeoPy.

# USAGE
- Firstly edit settings by manually creating ".env" file at 'Shipping' directory with next variables:
    - DJANGO_KEY (your django private key);
    - DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME (database params you need).
- After that you should just to start server and its database handling by writing standard Django command-line command:
  - "*python manage.py*" - 
  The command will initiate auto-reformatting of your DB if needed. It includes django-models migrations and creating
  of default objects sets. Maybe it will be necessary to wait 10 seconds
- Then you can call standard functions by sending HTTP-queries for working server API. Available queries examples:
    1) "*/api/v1/cargo*" (method *POST*) - creating new cargo object by zipcode and weight/description params;
    2) "*/api/v1/cargo*" (method *GET*) - getting all cargo objects with listing nearby machines for using selected cargo;
    3) "*/api/v1/cargo/<cargo_id>/*" (method *GET*) - getting details about cargo with needed ID with listing of all
        cars that existing, with showing current distance from selected cargo;
    4) "*/api/v1/machine/<machine_id>*" (method *PUT*) - editing of selected machine object (including currently location);
    5) "*/api/v1/cargo/<cargo_id>*" (method *PUT*) - editing of selected cargo object (including its weight, description);
    6) "*/api/v1/cargo/<cargo_id>*" (method *DELETE*) - manually deleting of selected cargo object.
- API also supports all standard DRF-queries. For example:
    - "*/api/v1/machine(or location)*" (method *GET*) - getting all model objects through DRF-serializers handling of 
      models query sets;
    - etc.