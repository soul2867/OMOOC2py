%#template for the form for neworld_note

<head>
<p><h1>Welcome to Neworld! </h1></p>
<p>Please write down your notes:</p>
</head>
<body>

<form action="/neworld" method="POST">
<input type= "text" size="100" maxlength="100" name="notes" autofocus>
<input type= "submit" name="save" value="save">
</form>
        <textarea cols=50 rows=50>{{note}}
        </textarea>
</body>

