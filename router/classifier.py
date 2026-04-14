"""
    - The classifier will label the prompt with one out of the following labels coding, 
    reasoning, creative or factual.
"""
import re

class Router:

    #Word pools for classifying user prompts
    coding_word_pool = {"auto", "else", "long", "switch", "break", "enum", "register", "typedef", "case", 
                        "extern", "return", "union", "char", "float", "short", "unsigned", "const", "for", 
                        "signed", "void", "continue", "goto", "sizeof", "volatile", "abstract", "assert", 
                        "boolean", "byte", "catch", "class", "default", "do", "double", "extends", "final", 
                        "finally", "if", "implements", "import", "instanceof", "int", "interface", "native", 
                        "new", "package", "private", "protected", "public", "static", "strictfp", "super", 
                        "synchronized", "this", "throw", "throws", "transient", "try", "while", "and", "exec", 
                        "not", "or", "pass", "from", "print", "global", "raise", "def", "del", "elif", "in", "is", 
                        "with", "except", "lambda", "yield", "struct", "_Packed", "function", "code", "python", 
                        "javascript", "java", "c++", "algorithm", "sort", "array", "variable", "debug", "compile", 
                        "syntax", "loop", "recursion", "stack", "queue", "api"}
    
    reasoning_word_pool = {"why", "how", "explain", "analyze", "compare", "contrast",
            "calculate", "solve", "math", "equation", "logic", "prove",
            "what if", "predict", "evaluate", "justify"}

    creative_word_pool = {"write", "story", "poem", "creative", "brainstorm", "generate",
            "compose", "imagine", "design", "create", "invent", "fiction",
            "character", "plot", "dialogue", "metaphor"}

    def __init__(self, prompt):
        self.prompt = prompt

    """
       Categories are selected by counting how many words from the prompt appear in each 
       category's word pool. The category with the highest weighted word count is chosen. 
       If no category meets the threshold, a default category is used.

       Categories: coding, reasoning, creative, and factual(default)
    """
    def category(self):

        #Tokenize text by words and punctuation, then lowercase for consistent algorithm input.
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




