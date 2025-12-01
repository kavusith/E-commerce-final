import os
from app import create_app

# Create the app instance using the factory function
app = create_app()

if __name__ == '__main__':
    # Only enable debug if FLASK_ENV is not 'production'
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    app.run(debug=debug_mode)
