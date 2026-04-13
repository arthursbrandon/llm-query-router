import sys
from router.classifier import Router
from router.model_registry import Models

#prompt = sys.argv[1]


def main():

    try:

        print(f'\nPlease enter prompt below:')
        prompt = input()

        c = Router( prompt = prompt)

        m = Models(
            category = c.category(),
            prompt = prompt
        )
        
        result = m.loadModel()
        print(f'\n================================================================')
        print(f'Prompt: {prompt}\nCategory: {c.category()}\nResult: {result}')
        print(f'================================================================\n')
    
    except Exception as e:
        
        print(f'Error: {e}')
    

if __name__ == "__main__":
    main()