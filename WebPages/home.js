import React from 'react'

<html>
    <!title and head>
    <head>
        <title>Home pages</title>
        <h1>Home Page</h1>
    </head>
    <!section where messages are flashed>
	{%for message in get_flashed_messages()%}
        <div style="text-align:center;" class="alert alert-warning alert-dismissible fade show" role="alert">
            {{message}}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="close"></button>
        </div>
	{%endfor%}

    <!links to other pages>
    <ul>
        <li><a href="/Add_Food">Add food</a></li>
        <li><a href="/Remove_Food">Remove food</a></li>
        <li><a href="/Check_Food">Check food</a></li>
    </ul>
</html>