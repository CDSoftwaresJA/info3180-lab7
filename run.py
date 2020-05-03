#! /usr/bin/env python
from app import app
app.config.from_object(__name__)
app.config['UPLOADED_IMAGES_DEST']= "static/"
app.run(debug=True, host="0.0.0.0", port=8080)
