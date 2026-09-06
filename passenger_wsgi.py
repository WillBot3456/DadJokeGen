import os
import sys

# 1. Add the virtual environment site-packages path
sys.path.insert(0, '/home/thepione/virtualenv/DadJokeGenerator/3.10/lib/python3.X/site-packages')

# 2. Add the directory where your app.py file lives
sys.path.insert(0, '/home/thepione/DadJokeGenerator')

# 3. Import your Flask app instance
from app import app as application