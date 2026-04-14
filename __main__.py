import sys
from art import *
from router.classifier import Router
from router.model_registry import Models


title = text2art("\nLLM Query Router\n", space=1)

def main():

    try:
        print(f'\nPlease enter prompt below:')
        prompt = input()

        #Allows user to exit program
        if prompt == 'EXIT':
            sys.exit("\nExiting program. Goodbye!\n")

        else:

            prompt_router = Router( prompt = prompt)

            m = Models(
                category = prompt_router.category(),
                prompt = prompt
            )
            

            result = m.loadModel()
            print(f'\n================================================================')
            print(f'- Prompt: {prompt}\n- Category: {prompt_router.category().capitalize()}\n- Result: {result}')
            print(f'================================================================\n')
    
    except Exception as e:
        
        print(f'Error: {e}')


if __name__ == "__main__":
    print(title)
    print(f'\nWelcome! If you wish to exit the program, type EXIT and press Enter.')
    while True:
        main()