from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page with the form
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract input data
    age = int(data.get('age', 0))
    lifestyle = data.get('lifestyle', '').lower()
    diet = data.get('diet', '').lower()
    symptoms = data.get('symptoms', [])

    # Placeholder logic for probiotic recommendation
    recommendation = "Standard Probiotic Blend"

    # Basic logic examples:
    # If user has bloating/gas, choose "Digestive Relief Probiotic"
    if 'bloating' in symptoms or 'gas' in symptoms:
        recommendation = "Digestive Relief Probiotic"
    
    # If user is over 50, choose "Senior Probiotic Formula"
    if age > 50:
        recommendation = "Senior Probiotic Formula"
    
    # If user is active & vegetarian, choose "Vegetarian Active Probiotic Blend"
    if lifestyle == 'active' and diet == 'vegetarian':
        recommendation = "Vegetarian Active Probiotic Blend"

    # Return the recommendation in JSON format
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
