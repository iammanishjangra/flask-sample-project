from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Ye function hamare home page (index.html) ko render karega
    return render_template('index.html')

@app.route('/about')
def about():
    # Ek simple about api endpoint
    return {"message": "Hello Manish! Ye apka naya python web project hai."}

if __name__ == '__main__':
    # Flask app ko port 5000 par run karenge, debug=True se development asaan hoti hai
    print("🚀 App start ho raha hai! Browser me http://127.0.0.1:5000 kholiye")
    app.run(host='0.0.0.0', port=5000, debug=True)
