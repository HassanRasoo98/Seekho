import os
import openai
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('OPENAI_API_KEY')
openai.api_key = key

response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo-0125",
	
	messages=[
     	{"role": "system", "content": "You are a helpful assistant designed to output JSON."},
		{"role": "user", "content": "Who is the best football player in the World?"}],
	
	max_tokens=150,
	temperature=0.6
)

print(response['choices'][0]['message']['content'])

# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from utils import get_transcript

# load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key) 
# messages = [ {"role": "system", "content": 
# 			"You are a intelligent assistant."} ] 
# while True: 
# 	message = input("User : ") 
# 	if message: 
# 		messages.append( 
# 			{"role": "user", "content": message}, 
# 		) 
# 		chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
# 	reply = chat.choices[0].message.content 
# 	print(f"ChatGPT: {reply}") 
# 	messages.append({"role": "assistant", "content": reply}) 



# if True: 
# 	transcript = get_transcript()
# 	message = input(f"User : Generate 5 mcqs from this transcript. Place an asterik on the correct option: {transcript}") 
# 	if message: 
# 		messages.append( 
# 			{"role": "user", "content": message}, 
# 		)
# 		chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
# 	reply = chat.choices[0].message.content 
# 	print(f"User: {message}")
# 	print(f"ChatGPT: {reply}") 
# 	# messages.append({"role": "assistant", "content": reply}) 
