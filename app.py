from flask import Flask, render_template, abort
import model as md

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	object_list = md.get_csv()
	return render_template("index.html", object_list=object_list)


@app.route("/<row_id>/")
def detail(row_id):
	object_list = md.get_csv()
	for row in object_list:
		if row['id'] ==row_id:
			return render_template("detail.html",object=row)
	abort(404)


if __name__ =="__main__":
	app.run(port=5000, debug = True)