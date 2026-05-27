'''
GET-->this GET request is used to retreive data from server
POST-->POST request is to send data to the seerver
PUT-->request is used to update existing data on the server 
DELETE--> Delete is used to delete data from the server

Control Statements
------------------
1.Condition
2.Loops
{% %}

eg:-
{%if marks>35%}
     <h2>pass</h2>
{%else%}
    <h2>fail</h2>

2. loops
{% for item in subjects %}
  <p>{{ item }}</p>
{% end for %}

template inheritance
--------------------
this allows
'''