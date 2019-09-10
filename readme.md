### Basic Flask-jQuery-Ajax app with MongoDB backend

Shows how the Flask, jQuery (JavaScript), Ajax and CSS parts fit together, avoids Jinja templating in Flask. Demonstrates SQLite database access and data editing. Also demonstrates a clickable row that retrieves and displays data from the mouse position.

To run the demo from the command line:  

```
$ export FLASK_APP=app.py FLASK_ENV=development  
$ flask run  
```

Running in the Flask development environment auto-reloads the server with changes to the code files. The default port is `127.0.0.1:5000`. Use `<Ctrl-C>` in the terminal window to kill the server process.  

See the 'js-sqlite' branch in this repo for demo of the same app with MongoDB serving the data at the backend.
