import random

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
        {% for rating in range(1, 6) %}<button type="button" data-rating="{{ rating }}" aria-label="{{ rating }} out of 5">★</button>{% endfor %}
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
    const BaseURL = 'https://thepioneersnest.com';

    async function getJoke() {
      const selected = category.value;
      const url = selected ? `${BaseURL}/api/joke?category=${encodeURIComponent(selected)}` : `${BaseURL}/api/joke`;
      const response = await fetch(url, {credentials: 'omit'});
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Failed to fetch joke");
      currentJoke = data;
      setup.textContent = data.setup;
      punchline.textContent = data.punchline;
      message.textContent = '';
    }

    document.querySelector('#joke-button').addEventListener('click', () => getJoke().catch(error => {
      setup.textContent = "Error loading joke.";
      punchline.textContent = "";
      message.textContent = error.message;
    }));
    
    document.querySelectorAll('[data-rating]').forEach(button => button.addEventListener('click', async () => {
      if (!currentJoke) { message.textContent = 'Get a joke before rating it.'; return; }
      try {
        const response = await fetch(`${BaseURL}/api/rate`, {
          method: 'POST', 
          credentials: 'omit',
          headers: {'Content-Type': 'application/json'}, 
          body: JSON.stringify({ joke: [currentJoke.setup, currentJoke.punchline], rating: Number(button.dataset.rating) }) 
        });
        const data = await response.json();
        message.textContent = data.message || data.error;
      } catch (err) {
        message.textContent = "Failed to submit rating.";
      }
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
    try:
        if category:
            if category not in generator.jokes:
                valid = ", ".join(generator.jokes.keys())
                return jsonify(error=f"Sorry, '{category}' isn't a valid category. Try: {valid}"), 400
            jokes = generator.jokes[category]
        else:
            jokes = [joke for group in generator.jokes.values() for joke in group]

        setup, punchline = random.choice(jokes)
        return jsonify(setup=setup, punchline=punchline)
    except Exception as e:
        return jsonify(error=f"Joke retrieval error: {str(e)}"), 500

@app.post("/api/rate")
def rate():
    data = request.get_json(silent=True) or {}
    try:
        rating = int(data["rating"])
        # Standardise text elements to strip out white space issues
        joke_tuple = (str(data["joke"][0]).strip(), str(data["joke"][1]).strip())
    except (KeyError, TypeError, ValueError, IndexError):
        return jsonify(error="Provide a valid joke array and a rating."), 400
        
    if rating not in range(1, 6):
        return jsonify(error="Rating must be between 1 and 5."), 400
        
    try:
        result = generator.rate_joke(joke_tuple, rating)
        return jsonify(message=result)
    except Exception as e:
        return jsonify(error=f"Rating system error: {str(e)}"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

