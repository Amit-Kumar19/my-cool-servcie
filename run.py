from app import create_app

app = create_app()

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    """
    app.run(host='0.0.0.0', port=8000)
