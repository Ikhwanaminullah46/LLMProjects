# LLM01 - Short Story Generator
This projects tries to create a simple app to generate short stories using 5 simple descriptions. The 5 descriptions are character, goals, dilemma/obstacle, decision, and outcome. This app is build using Ollama to run llama3 locally. The app is built with streamlit where the user will gives inputs to the model and then the model will will generate the short story along with a title.

### Goals
The goal of this project is to create an app using the LLM to generate short story from simple ideas.

## setup
```
pip install -r requirements.txt
```
## Conclusion
The app built is able to generate a short story with the 5 given description by the user. The app runs successfully if the user provided the expected input.

Some improvements can be made especially from the user experience part. such as: The model is still going to generate a story even if the user doesn't provide any random input (including blank or random combintion of alphabets like "zzzz"). Streaming also can be implemented for better experience.
