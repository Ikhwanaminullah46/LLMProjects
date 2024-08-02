from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
import ollama


def generateStory(character_description, goals, dilemma, decision, outcome):
    llm = OllamaLLM(model="llama3")
    
    ## PromptTemplate
    prompt = PromptTemplate.from_template(
    """
    Write a short story with the following criteria:
    characters: {Character_description} 
    Goals : {Goals}
    Dilemma: {Dilemma}
    Decision: {Decision}
    Outcome: {Outcome}

    The story should include a title and a good hook.
    """
    )

    prompt = prompt.format(
        Character_description = character_description,
        Goals = goals,
        Dilemma = dilemma,
        Decision = decision,
        Outcome = outcome
    )
    response = llm.invoke(prompt)

    return response