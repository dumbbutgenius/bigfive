from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run()