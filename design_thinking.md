## Key Design Choices 

1. Choice of Hugging Face over OpenAI - Initially, OpenAI’s API was considered for its advanced, versatile NLP capabilities and efficiency in understanding complex queries. However, due to payment limitations, Hugging Face models became the practical alternative.
2. Flask for backend development
3. HTML, CSS and JavaScript for the frontend development.

## Challenges with Hugging Face Models  
1. Slower response time
2. Certain complex or specialized questions did not yield highly accurate or satisfying responses.

## Areas for future improvement  
1. Enhancing response speed 
2. Improving Response Accuracy and Contextual Understanding 
3. Potential for Follow-Up Questions by integrating an OpenAI model. 


## Challenges while deploying the project 
Many free-tier cloud platforms (like Heroku, AWS Lambda, AWS EC2, pythonAnywhere, Vercel, Render, GitHub Codespaces) have resource limits, such as storage space or memory, which restricted my ability to deploy the app effectively, especially for larger models or dependencies.
