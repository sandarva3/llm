from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer


model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

print("Chatbot: Type 'exit()' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit()':
        print("Goodbye!")
        break
    
    response = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
    print(f"Chatbot: {response[len(user_input):]}")

