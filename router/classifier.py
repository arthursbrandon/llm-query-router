"""
    - The classifier will label the prompt with one out of the following labels coding, reasoning, creative or factual.
"""
import re

class Router:

    coding_word_pool = {"function", "code", "python", "javascript", "java", "c++", 
        "algorithm", "sort", "array", "variable", "debug", "compile",
        "syntax", "loop", "recursion", "stack", "queue", "api"}
    
    reasoning_word_pool = {"why", "how", "explain", "analyze", "compare", "contrast",
            "calculate", "solve", "math", "equation", "logic", "prove",
            "what if", "predict", "evaluate", "justify"}

    creative_word_pool = {"write", "story", "poem", "creative", "brainstorm", "generate",
            "compose", "imagine", "design", "create", "invent", "fiction",
            "character", "plot", "dialogue", "metaphor"}

    def __init__(self, prompt):
        self.prompt = prompt


    def category(self):

        clean_prompt = re.findall( r'\w+|[^\s\w]+',self.prompt.lower())

        coding_word_pool_count = len(set(clean_prompt).intersection(Router.coding_word_pool))
        reasoning_word_pool_count = len(set(clean_prompt).intersection(Router.reasoning_word_pool))
        creative_word_pool_count = len(set(clean_prompt).intersection(Router.creative_word_pool))

        #coding
        if coding_word_pool_count > reasoning_word_pool_count and coding_word_pool_count > creative_word_pool_count:
            return 'coding'

        #reasoning
        elif reasoning_word_pool_count > creative_word_pool_count and reasoning_word_pool_count > coding_word_pool_count:
            return 'reasoning'
        
        #creative
        elif creative_word_pool_count > coding_word_pool_count and creative_word_pool_count > reasoning_word_pool_count:
            return 'creative'

        #factual
        else:
            return 'factual'




