from openai import OpenAI

from utils import get_transcript

client = OpenAI(api_key='YOUR_API_KEY') 
messages = [ {"role": "system", "content": 
			"You are a intelligent assistant."} ] 
while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		) 
		chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages) 
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply}) 



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
