from flask import Flask, render_template
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    p = Post(0)
    data = p.titles()
    return render_template("index.html", data = data)

@app.route('/post/<num>')
def get_post(num):
    p = Post(num)
    data = p.blog()
    if data:  # Check if the post was found
        return render_template("post.html", data=data)
    else:
        return "<h1>Post not found</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)


