# export ALGORITHMS=['RS256']
# export ATH0_DOMAIN='ofineo.eu.auth0.com'
# export API_AUDIENCE='portfolio'
# export DATABASE_URL="postgres://postgres:postgres@localhost:5432/portfolio"
export FLASK_APP=app.py
export FLASK_DEBUG=true
flask run --reload
