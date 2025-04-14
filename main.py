import requests

from config import OPEN_AI_API_KEY


def make_prompt(initial_prompt: str, improvement_prompt: str, iterations: int, model: str) -> dict[str, str]:
    current_prompt = initial_prompt

    for i in range(iterations):
        response = requests.post(
            url='https://api.openai.com/v1/chat/completions',
            headers={
                "Authorization": f"Bearer {OPEN_AI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": improvement_prompt},
                    {"role": "user", "content": current_prompt}
                ]
            }
        )

        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            current_prompt = result['choices'][0]['message']['content'].strip()
            print(f"\n--- Iteration {i + 1} ---\n{current_prompt}")
        else:
            print("Error or empty response:", result)
            break

    return {
        "final_prompt": current_prompt,
        "iterations_performed": i + 1,
        "model_used": model
    }


if __name__ == '__main__':
    initial_prompt = input("Your initial prompt: ")
    improvement_prompt = input("Your improvement prompt: ")

    while True:
        iterations = input("Iterations: ")
        if iterations.isdigit():
            iterations = int(iterations)
            break
        print("Please enter a valid number.")

    model = input("Your model (e.g., gpt-3.5-turbo): ")
    result = make_prompt(initial_prompt, improvement_prompt, iterations, model)

    print(f"Final Prompt: {result['final_prompt']}")
    print(f"Iterations: {result['iterations_performed']}")
    print(f"Model Used: {result['model_used']}")
