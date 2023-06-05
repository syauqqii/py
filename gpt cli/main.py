from os import system, name
from gpt4free.you import Completion

def main():
    system('cls' if name == 'nt' else 'clear')

    print("\n      +---+---+---+---+---+---+")
    print("      | A | I | _ | C | L | I |")
    print("      +---+---+--+-[./0xd1m5]-+")

    chat = []
    while True:
        prompt = input("\n > [YOU] : ")
        if prompt.lower() in ['exit', 'quit']:
            break

        response = Completion.create(prompt=prompt, chat=chat)
        print(" > [BOT] :", response.text)
        chat.append({"question": prompt, "answer": response.text})

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit(0)
