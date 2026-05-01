from flask import Flask, request, jsonify, session, render_template
from models import db, User, Opportunity
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return render_template('admin.html')


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}

    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "All fields required"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Signup successful"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or user.password != data.get('password'):
        return jsonify({"error": "Invalid email or password"}), 401

    session['user_id'] = user.id

    return jsonify({"message": "Login successful"})


@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    return jsonify({"message": "If account exists, reset link sent"})


@app.route('/opportunity', methods=['POST'])
def create_opportunity():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json() or {}

    opp = Opportunity(
        name=data.get('name'),
        duration=data.get('duration'),
        start_date=data.get('start_date'),
        description=data.get('description'),
        skills=data.get('skills'),
        category=data.get('category'),
        future=data.get('future'),
        max_applicants=data.get('max_applicants'),
        user_id=session.get('user_id')
    )

    db.session.add(opp)
    db.session.commit()

    return jsonify({"message": "Created"})


@app.route('/opportunity', methods=['GET'])
def get_opportunities():
    opps = Opportunity.query.all()

    result = []
    for o in opps:
        result.append({
            "id": o.id,
            "name": o.name,
            "duration": o.duration,
            "start_date": o.start_date,
            "description": o.description,
            "skills": o.skills,
            "category": o.category,
            "future": o.future,
            "max_applicants": o.max_applicants
        })

    return jsonify(result)


@app.route('/opportunity/<int:id>', methods=['GET'])
def get_one(id):
    opp = Opportunity.query.get(id)

    if not opp:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": opp.id,
        "name": opp.name,
        "description": opp.description
    })


@app.route('/opportunity/<int:id>', methods=['PUT'])
def update_opportunity(id):
    opp = Opportunity.query.get(id)

    if not opp:
        return jsonify({"error": "Not found"}), 404

    data = request.get_json() or {}

    opp.name = data.get('name', opp.name)
    opp.description = data.get('description', opp.description)

    db.session.commit()

    return jsonify({"message": "Updated"})


@app.route('/opportunity/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    opp = Opportunity.query.get(id)

    if not opp:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(opp)
    db.session.commit()

    return jsonify({"message": "Deleted"})


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)