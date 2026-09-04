from flask import Flask, jsonify, request, render_template_string

from pythontest import DadJokeGenerator

app = Flask(__name__)
generator = DadJokeGenerator()

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Dad Joke Generator</title>
  <style>
    :root { color-scheme: light; font-family: system-ui, sans-serif; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #fff7ed; color: #3b2416; }
    main { width: min(92vw, 680px); padding: 2rem; text-align: center; }
    h1 { font-size: clamp(2rem, 8vw, 4rem); margin: 0 0 .5rem; }
    .joke { min-height: 10rem; display: grid; align-content: center; gap: 1rem; margin: 2rem 0; padding: 2rem; border: 2px solid #f59e0b; border-radius: 1rem; background: #fffbeb; font-size: clamp(1.2rem, 3vw, 1.7rem); }
    .punchline { font-weight: 700; color: #b45309; }
    button, select { border: 0; border-radius: .6rem; padding: .8rem 1rem; font: inherit; cursor: pointer; }
    button { background: #ea580c; color: white; font-weight: 700; }
    button:hover { background: #c2410c; }
    select { margin-right: .5rem; background: white; border: 1px solid #d6d3d1; }
    .ratings { margin-top: 1.5rem; }
    .stars button { padding: .35rem; background: transparent; color: #f59e0b; font-size: 1.5rem; }
    #message { min-height: 1.5rem; color: #78716c; }
  </style>
</head>
<body>
  <main>
    <h1>Dad Joke Generator</h1>
    <p>Fresh groans, sorted by category.</p>
    <div class="joke" aria-live="polite">
      <div id="setup">Click the button for a joke.</div>
      <div id="punchline" class="punchline"></div>
    </div>
    <select id="category" aria-label="Joke category">
      <option value="">Any category</option>
      {% for category in categories %}<option value="{{ category }}">{{ category.title() }}</option>{% endfor %}
    </select>
    <button id="joke-button">Tell me a joke</button>
    <section class="ratings" aria-label="Rate this joke">
      <div>Rate this joke</div>
      <div class="stars">
        {% for rating in range(1, 6) %}<button type="button" data-rating="{{ rating }}" aria-label="{{ rating }} out of 5">&#9733;</button>{% endfor %}
      </div>
    </section>
    <div id="message" role="status"></div>
  </main>
  <script>
    let currentJoke = null;
    const setup = document.querySelector('#setup');
    const punchline = document.querySelector('#punchline');
    const message = document.querySelector('#message');
    const category = document.querySelector('#category');

    async function getJoke() {
      const selected = category.value;
      const url = selected ? `/api/joke?category=${encodeURIComponent(selected)}` : '/api/joke';
      const response = await fetch(url);
      const data = await response.json();
      if (!response.ok) throw new Error(data.error);
      currentJoke = data;
      setup.textContent = data.setup;
      punchline.textContent = data.punchline;
      message.textContent = '';
    }

    document.querySelector('#joke-button').addEventListener('click', () => getJoke().catch(error => message.textContent = error.message));
    document.querySelectorAll('[data-rating]').forEach(button => button.addEventListener('click', async () => {
      if (!currentJoke) { message.textContent = 'Get a joke before rating it.'; return; }
      const response = await fetch('/api/rate', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ joke: [currentJoke.setup, currentJoke.punchline], rating: Number(button.dataset.rating) }) });
      const data = await response.json();
      message.textContent = data.message || data.error;
    }));
  </script>
</body>
</html>"""


@app.get("/")
def index():
    return render_template_string(PAGE, categories=generator.get_all_categories())


@app.get("/api/joke")
def joke():
    category = request.args.get("category")
    setup, punchline = (generator.get_random_joke() if not category else generator.get_joke_by_category(category))
    if not setup:
        return jsonify(error=punchline), 400
    return jsonify(setup=setup, punchline=punchline)


@app.post("/api/rate")
def rate():
    data = request.get_json(silent=True) or {}
    try:
        rating = int(data["rating"])
        joke_tuple = tuple(data["joke"])
    except (KeyError, TypeError, ValueError):
        return jsonify(error="Provide a joke and a rating from 1-5."), 400
    result = generator.rate_joke(joke_tuple, rating)
    if rating not in range(1, 6):
        return jsonify(error=result), 400
    return jsonify(message=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
