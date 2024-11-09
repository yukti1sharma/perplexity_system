from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
from transformers import pipeline
from flask_cors import CORS


load_dotenv()


# Initialize Flask app
app = Flask(__name__)
CORS(app)


API_KEY = os.getenv('GOOGLE_API_KEY')
CX_ID = os.getenv('GOOGLE_CSE_CX')

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def google_search(query):
    """
    Performs a Google Custom Search for the given query and returns results.
    """
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX_ID}&q={query}"
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad responses
    results = response.json()
    search_results = [
        {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
        for item in results.get("items", [])
    ]
    return search_results

def generate_answer_with_sources(query):
    """
    Generates an answer with sources for the given query.
    """

    search_results = google_search(query)
    if not search_results:
        return "No relevant information found."

    combined_snippets = " ".join(result["snippet"] for result in search_results)
    
    try:
        summary = summarizer(combined_snippets, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
    except Exception as e:
        summary = "Could not summarize the information. Try refining your query."

    #OUTPUT
    response_data = {
        "answer": summary,
        "sources": [
            {"title": result["title"], "link": result["link"], "snippet": result["snippet"]}
            for result in search_results
        ]
    }
    return response_data

@app.route("/generate_answer", methods=["POST"])
def generate_answer():
    """
    API endpoint to get an answer and sources based on the query provided in JSON payload.
    """
    data = request.json
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "Query parameter is required."}), 400

    result = generate_answer_with_sources(query)
    
    return jsonify(result)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
