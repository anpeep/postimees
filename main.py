from openai import OpenAI

from config import OPEN_AI_API_KEY

client = OpenAI(api_key=OPEN_AI_API_KEY)


def make_prompt(initial_prompt: str, improvement_prompt: str, iterations: int, model: str) -> dict[str, str]:
    current_prompt = initial_prompt

    for i in range(iterations):
        response = client.chat.completions.create(
            model=model,
            store=True,
            messages=[
                {"role": "system", "content": improvement_prompt},
                {"role": "user", "content": current_prompt}
            ]
        )

        current_prompt = response.choices[0].message.content.strip()
        print(f"\n--- Iteration {i + 1} ---\n{current_prompt}")

    return {
        "final_prompt": current_prompt,
        "iterations_performed": iterations,
        "model_used": model
    }


if __name__ == "__main__":
    initial_prompt = input("Initial prompt: ")
    improvement_prompt = input("Improvement prompt: ")
    iterations = int(input("Iterations: "))
    model = input("Model (e.g., gpt-3.5-turbo): ")

    result = make_prompt(initial_prompt, improvement_prompt, iterations, model)

    print("\n=== Final Result ===")
    print(f"Prompt: {result['final_prompt']}")
    print(f"Iterations: {result['iterations_performed']}")
    print(f"Model: {result['model_used']}")
