# PERPLEXITY Q&A SYSTEM 

## Project Overview and Objectives 

A functional mini Perplexity system that can accept user queries, perform web searches, generate concise answers using a language model (I used Hugging Face Transformers), and provide source citations.

## Setup and Installation instructions 

Required softwares - Python, Flask, HTML, CSS and JavaScript

### Backend Setup  
- Clone the repository.
- Install dependencies listed in requirements.txt.
- Configure API key and Search engine ID for Google Custom Search API and choose the language model to process search results and generate coherent, concise answers.

### Frontend Setup 
- Create index.html, style.css and script.js. 
- Open index.html in a browser or serve it through a local server.  

### Running the application 
- Start the Flask server using python app.py.
- Open index.html to access the frontend.

### Deployment steps and and Access Details 
Local Deployment : 
  - Run the backend on http://127.0.0.1:5000/ 
  - Access the frontend via your browser

### Cloud Deployment 


## Usage Guidelines and and Example Interactions 

 Input a query - Users can type a question into the input box and click "Go" to fetch an answer.
   
 <img width="700" alt="image" src="https://github.com/user-attachments/assets/618b4650-3457-4a78-b064-ed0f1fd9842c" />


   #### Example interactions -
   
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/1de67719-d151-48cc-9b47-7a8eec496a5b" />


  <img width="700" alt="image" src="https://github.com/user-attachments/assets/cbd824be-8e04-4ea9-a000-d6e891a19829" />


## Design decisions

1. Backend Framework - Chose Flask for simplicity and lightweight performance.
2. Frontend Structure - Used HTML/CSS/JS for a simple, accessible interface. 
3. Language Model - Hugging Face as it offers a variety of pre-trained transformer models that are freely accessible and open-source. 
4. Search API  - Google Custom Search API as it uses Google’s search engine, which is often more familiar for users.


## Challenges 
1. OpenAI Access Limitations
2. Hugging Face models provided a workable alternative, they sometimes lacked the accuracy or specificity needed for diverse and complex questions.
3. Implementing a seamless follow-up question system proved challenging without integrating openAI.
4. Response time for generating answers was slower than desired due to the load required by transformer models, particularly for tasks like summarization or large-scale text processing.


## Potential Areas for Future Improvement
1. Enhanced NLP: Integrate a model like GPT for more natural responses.
2. Implementing a follow-up question system.
3. Optimizing response time 



   

