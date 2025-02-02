from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting server on http://localhost:8080")
    app.run(debug=True, port=8080, host='0.0.0.0')
