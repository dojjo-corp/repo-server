from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('key.json')
default_app = firebase_admin.initialize_app(cred)

@app.route('/')
def hello():
    return 'Hello World!'


# Endpoint For Deleting Users
@app.route('/delete_user', methods=['POST'])
def delete_user():
    request_data = request.get_json()
    # get USER's uid
    uid = request_data.get('uid')

    user = auth.get_user(uid)

    try: 
        auth.delete_user(user)
        return jsonify({'success': True, 'message': 'User deleted successfully'})
    except auth.AuthError as e:
        return jsonify({'success': False, 'message': f'Error deleting user: {e}'})

if __name__ == '__main__':
    app.run(debug=True)
