import requests
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('OPENAI_API_KEY')
openai.api_key = key

class ParagraphInput(BaseModel):
    paragraph: str

class ParagraphSegmentationRequest(BaseModel):
    text_file_path: str

class Transcribe(BaseModel):
    path: str

def get_mcq(paragraph: str):
    response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo-0125",
	
	messages=[
     	{"role": "system", "content": "You are a helpful assistant designed to output JSON."},
		{"role": "user", "content": f"Generate High Quality MCQs for learners from this transcript. Output must be in JSON. Include a field for correct option in JSON. Paragraph: {paragraph}"}],
	
        max_tokens=150,
        temperature=0.6
    )

    reply = response['choices'][0]['message']['content']
    return reply

def get_heading(paragraph):
    base_url = ""
    url = base_url + "/generate-topics/"
    # url = "" # add ngrok link here
    data = {"paragraph": paragraph}
    
    try:
        response = requests.post(url, json=data)
        heading = str(response.json()).split("Topic:")[1].strip()
        if response.status_code == 200:
            return heading
        else:
            # return f"Error: {response.status_code} - {response.reason}"
            return ""
    except Exception as e:
        # return f"Error: {e}"
        return ""


def final_transcript():
    return """Unsupervised Learning.
Thanks to Wix for supporting PBS Digital Studios. Hey, I'm Jabruro and welcome to Crash Course AI. So far in the series, we focused on artificial intelligence that uses supervised learning. These programs need a teacher to use labeled data to tell them right from wrong. And we humans have places where supervised learning happens, like classrooms with teachers. But that's not the only way we learn. We can also learn lots of things on our own by finding patterns in the world. We can look at dogs and elephants and know they're different animals without anyone telling us. Or we can even figure out the rules of a sport just by watching other people play. This kind of learning without a teacher is called unsupervised learning.

Unsupervised learning
And in some cases, computers can do it too. The key difference between supervised and unsupervised learning is what we're trying to predict. In supervised learning, we're trying to build a model to predict an answer or label provided by a teacher. In unsupervised learning, instead of a teacher, the world around us is basically providing training labels. For example, if I freeze this video of a tennis ball right now, can you draw what could be the next frame? Unsupervised learning is about modeling the world by guessing like this. And it's useful because we don't need labels provided by a teacher. Babies do a lot of unsupervised learning by watching and imitating people. And we'd like computers to be able to learn like this as well.

Unsupervised Learning
This lets us utilize lots of freely available data in the world or on the internet. In many cases, one of the easiest ways to understand how AI can use unsupervised learning is by doing it ourselves.

Flower Classification Using Unsupervised Clustering
So let's look at a few photos of flowers with no labels. The most basic way to model the world is to assume that it's made up of distinct groups of objects that share properties. So, for example, how many types of flowers are here? We can say there are two because there are two colors, purple and yellow. Or we can look at the petal shapes and divide them into round petals and tall vertical ones. Or maybe we have some more experience with flowers and realize that two of these are tulips, one is a sunflower, and the last one is a daisy. So there are three categories. Immediately recognizing different properties like this and creating categories is called unsupervised clustering. We don't have labels provided by a teacher, but we do have a key assumption about the world that we're modeling.

Clustering and classification in data.
Certain objects are more similar to each other than others. We can program computers to perform clustering. But to do that, we need to choose a few properties of flowers we're interested in looking at, like how we picked color or shape just now. For a more realistic example, let's say I bought a packet of iris seeds to plant in my garden. After the flowers bloom, though, it looks like there were several different species of irises mixed up in that one packet. Now, I'm no expert gardener, but I can use some AI to help me analyze my garden. To construct the model, we have to answer two key questions. First, what observation can we measure? All of these flowers are purple, so that's probably not the best way to tell them apart. But different irises seem to have different petal lengths and widths, which we can measure and place on this graph with petal length on the y-axis and width on the x-axis. And second, how do we want to represent the world? We're going to stick to a very simple assumption here. There are clusters in our data. Specifically, we're going to say there are some number of groups called K clusters, but we don't know where they are.

K-means clustering.
To help us, we're going to use the K-means clustering algorithm. K-means clustering is a simple algorithm. All it needs is a way to compare observations, a way to guess how many clusters exist in the data, and a way to calculate averages for each cluster it predicts. In particular, we want to calculate the mean by adding up all data points in a cluster and dividing by the total number of points. Remember, unsupervised learning is about modeling the world, so our algorithm will have two steps. First, our AI will predict. What does the model expect the world to look like? In other words, which flowers should be clustered together because they're the same species? Second, our AI will correct or learn. The model will update its belief to agree with its observation of the world. To start the process, we have to specify how many clusters the model should look for. I'm guessing there are three clusters in the data, so that becomes the model's initial understanding of the world. And we're looking for K equals 3 averages or 3 types of viruses. But to start, our model doesn't really know anything.

Data Science
So the averages are random and so are its predictions. Each data point, which is a flower, is given a label as type 1, type 2, or type 3. Based on the algorithm's beliefs. Next, our model tries to correct itself. The average of each cluster of data points should be in the middle. So the model corrects itself by calculating new averages. We can see those averages here, marked with X's, which gives us an updated model of the three, or so we guessed, types of viruses. But the graph is still pretty noisy. For example, it's a little weird that we have type 2 flowers so close to the average for type 3 flowers. But we did start with a random model, so we can't expect too much accuracy. Logically, we know that irises of the same species tend to have similar petals. So those data points should be clustered together.

Prediction
Since we did a correction or learning step, we can repeat the process, starting with a new prediction step. Let's predict new labels using the X's that mark the averages of each label.

iris clusters and their patterns in nature.
We'll give each data point the label of its closest X. Type 1, type 2, or type 3. And then we'll calculate new averages. Ah, that's better. But still not the cleanest clusters. So we can repeat the process again. Predict, learn, predict, learn. Eventually, the X's will stop moving and we will have a model of iris clusters created with unsupervised learning. Now, the ultimate question is, did we find meaningful patterns about the world with our AI? We made an assumption that there were three types of irises and we assumed that they had different petal lengths and widths. Was this true? Lucky for us, I have a friend who is a master gardener.

Unsupervised Learning with Image Data
I showed him the real life flowers closest to each of the three averages and he said that type 1 is versicolor, type 2 is satosa, and type 3 is virginica. Three different iris species. We learned about the world from observation, which is what makes this unsupervised learning. Even though we relied a tiny bit on a teacher, the master gardener, for confirmation and help. Now that we've learned the basics, we can experiment with harder examples. Let's say we want to use unsupervised learning to sort a bunch of different photos, and not just three iris species. First, what observations can we measure? How much green there is, whether there's a nose and fur? To have a computer make these observations, we need to measure thousands of red, green, and blue pixels in each image. Second, how do we want to represent the world? Before, we were only working with two features, so we could just use the averages of the cluster data points and get meaningful extraction from it. But when dealing with images, we can't use the same method, because we won't get much meaning out of averaging colored pixels for what we want to accomplish. Somehow, we need the model to create a representation that tells us if two images are similar. There are meaningful patterns in the data that are more abstract than individual pixels, and finding them across many images is what's called representation learning. These patterns help us understand what's in the images and how to compare them to each other.

Representation Learning
Representation learning happens both in supervised and unsupervised learning models, so we can do it with or without labels to find patterns in the world. To understand the basic idea of representation learning, check out this experiment.

Drawing from memory.
I'm going to look at a picture really fast and then try and draw it. Ready, set, go. My eyes took in the picture and remembered important features, so I'm building a representation in my mind. But I can't just show you my thoughts to get feedback on what parts I misremembered, so I have to produce a reconstruction or draw the original image from my memory. Alright, so this is what I've got. Now let's compare my drawing to the original image. Let's see, round plate, triangle slice of pizza, some cheese, some crust, tablecloth. Pretty good.

Image Reconstruction in Artificial Intelligence
For an AI, making a reconstruction would mean producing all the right pixel values to make a reconstruction. Arcane means clustering algorithm from before predicted classes for flowers based on how close the data points were to the averages. For images, we will have learned image representations instead of averages. After that step, just like before, the AI will have to correct itself.

Neural Networks
Previously, we updated the K clusters based on how well our predicted labels fit the data, but for images, we'd have to update the model's internal representations based on its reconstructions. There are different ways to use unsupervised learning in combination with representation learning so that an AI can compare images. Like for example, there's a type of neural network called an autoencoder, which uses the same basic principles of weights and biases to process inputs, pass data onto the hidden layers, and finally to a prediction output layer. If John Greenbott was programmed with an autoencoder, the input would be an image, the hidden layers would contain representations, and the output would be a full reconstruction of the original image. Which gets more accurate the more we train this AI. Theoretically, I could give John Greenbott a representation of a pizza and he could reconstruct the original pizza image. What's so powerful about unsupervised learning is that the world is our teacher. By looking around, taking in a lot of data, and predicting what we'll see next, we learn about how the world works and how it should be represented. When asked how AI will fulfill its grand ambitions, 2018 Turing Award winning professor, Jan LeCun said, we all know that unsupervised learning is the ultimate answer. So, I guess we better keep working on it. Unsupervised learning is a huge area of active research. The human brain is specially designed for this kind of learning and has different parts for vision, language, movement, and so on. These structures and what kinds of patterns our brains look for were developed over billions of years of evolution. But it's really tricky to build an AI that does unsupervised learning well, because AI systems can't learn exactly like humans often do, just by watching and imitating. Someone like us has to design the models and tell them how to look for patterns before turning them loose. Next time, we'll look at applying similar concepts to AI systems that find patterns in words and language and what's called natural language processing. See you then. Thanks to Wix for supporting PBS Digital Studios. Check out Wix.com if you're looking to make your own website. Wix is a platform that allows you to build a personalized website for almost any purpose, from promoting your business or creating an online shop to giving you a place for you to test out new ideas. Their technology allows you to create something unique no matter your skill level with templates and all-in-one management. If you'd like to check it out, you can go to wix.com.com.

Go Crash Course or Click the Link in the Description
Go slash crash course or click the link in the description. Crash Course AI is produced in association with PBS Digital Studios. If you want to help keep Crash Course free for everyone forever, you can join our community on Patreon. And if you want to learn more about the math behind K-Means clustering, check out this video from Crash Course Statistics..

"""
    
def generate_random_text():
    return """ Thanks to Wix for supporting PBS Digital Studios. Hey, I'm Jabruro and welcome to Crash Course AI. So far in the series, we focused on artificial intelligence that uses supervised learning. These programs need a teacher to use labeled data to tell them right from wrong. And we humans have places where supervised learning happens, like classrooms with teachers. But that's not the only way we learn. We can also learn lots of things on our own by finding patterns in the world. We can look at dogs and elephants and know they're different animals without anyone telling us. Or we can even figure out the rules of a sport just by watching other people play. This kind of learning without a teacher is called unsupervised learning. And in some cases, computers can do it too. The key difference between supervised and unsupervised learning is what we're trying to predict. In supervised learning, we're trying to build a model to predict an answer or label provided by a teacher. In unsupervised learning, instead of a teacher, the world around us is basically providing training labels. For example, if I freeze this video of a tennis ball right now, can you draw what could be the next frame? Unsupervised learning is about modeling the world by guessing like this. And it's useful because we don't need labels provided by a teacher. Babies do a lot of unsupervised learning by watching and imitating people. And we'd like computers to be able to learn like this as well. This lets us utilize lots of freely available data in the world or on the internet. In many cases, one of the easiest ways to understand how AI can use unsupervised learning is by doing it ourselves. So let's look at a few photos of flowers with no labels. The most basic way to model the world is to assume that it's made up of distinct groups of objects that share properties. So, for example, how many types of flowers are here? We can say there are two because there are two colors, purple and yellow. Or we can look at the petal shapes and divide them into round petals and tall vertical ones. Or maybe we have some more experience with flowers and realize that two of these are tulips, one is a sunflower, and the last one is a daisy. So there are three categories. Immediately recognizing different properties like this and creating categories is called unsupervised clustering. We don't have labels provided by a teacher, but we do have a key assumption about the world that we're modeling. Certain objects are more similar to each other than others. We can program computers to perform clustering. But to do that, we need to choose a few properties of flowers we're interested in looking at, like how we picked color or shape just now. For a more realistic example, let's say I bought a packet of iris seeds to plant in my garden. After the flowers bloom, though, it looks like there were several different species of irises mixed up in that one packet. Now, I'm no expert gardener, but I can use some AI to help me analyze my garden. To construct the model, we have to answer two key questions. First, what observation can we measure? All of these flowers are purple, so that's probably not the best way to tell them apart. But different irises seem to have different petal lengths and widths, which we can measure and place on this graph with petal length on the y-axis and width on the x-axis. And second, how do we want to represent the world? We're going to stick to a very simple assumption here. There are clusters in our data. Specifically, we're going to say there are some number of groups called K clusters, but we don't know where they are. To help us, we're going to use the K-means clustering algorithm. K-means clustering is a simple algorithm. All it needs is a way to compare observations, a way to guess how many clusters exist in the data, and a way to calculate averages for each cluster it predicts. In particular, we want to calculate the mean by adding up all data points in a cluster and dividing by the total number of points. Remember, unsupervised learning is about modeling the world, so our algorithm will have two steps. First, our AI will predict. What does the model expect the world to look like? In other words, which flowers should be clustered together because they're the same species? Second, our AI will correct or learn. The model will update its belief to agree with its observation of the world. To start the process, we have to specify how many clusters the model should look for. I'm guessing there are three clusters in the data, so that becomes the model's initial understanding of the world. And we're looking for K equals 3 averages or 3 types of viruses. But to start, our model doesn't really know anything. So the averages are random and so are its predictions. Each data point, which is a flower, is given a label as type 1, type 2, or type 3. Based on the algorithm's beliefs. Next, our model tries to correct itself. The average of each cluster of data points should be in the middle. So the model corrects itself by calculating new averages. We can see those averages here, marked with X's, which gives us an updated model of the three, or so we guessed, types of viruses. But the graph is still pretty noisy. For example, it's a little weird that we have type 2 flowers so close to the average for type 3 flowers. But we did start with a random model, so we can't expect too much accuracy. Logically, we know that irises of the same species tend to have similar petals. So those data points should be clustered together. Since we did a correction or learning step, we can repeat the process, starting with a new prediction step. Let's predict new labels using the X's that mark the averages of each label. We'll give each data point the label of its closest X. Type 1, type 2, or type 3. And then we'll calculate new averages. Ah, that's better. But still not the cleanest clusters. So we can repeat the process again. Predict, learn, predict, learn. Eventually, the X's will stop moving and we will have a model of iris clusters created with unsupervised learning. Now, the ultimate question is, did we find meaningful patterns about the world with our AI? We made an assumption that there were three types of irises and we assumed that they had different petal lengths and widths. Was this true? Lucky for us, I have a friend who is a master gardener. I showed him the real life flowers closest to each of the three averages and he said that type 1 is versicolor, type 2 is satosa, and type 3 is virginica. Three different iris species. We learned about the world from observation, which is what makes this unsupervised learning. Even though we relied a tiny bit on a teacher, the master gardener, for confirmation and help. Now that we've learned the basics, we can experiment with harder examples. Let's say we want to use unsupervised learning to sort a bunch of different photos, and not just three iris species. First, what observations can we measure? How much green there is, whether there's a nose and fur? To have a computer make these observations, we need to measure thousands of red, green, and blue pixels in each image. Second, how do we want to represent the world? Before, we were only working with two features, so we could just use the averages of the cluster data points and get meaningful extraction from it. But when dealing with images, we can't use the same method, because we won't get much meaning out of averaging colored pixels for what we want to accomplish. Somehow, we need the model to create a representation that tells us if two images are similar. There are meaningful patterns in the data that are more abstract than individual pixels, and finding them across many images is what's called representation learning. These patterns help us understand what's in the images and how to compare them to each other. Representation learning happens both in supervised and unsupervised learning models, so we can do it with or without labels to find patterns in the world. To understand the basic idea of representation learning, check out this experiment. I'm going to look at a picture really fast and then try and draw it. Ready, set, go. My eyes took in the picture and remembered important features, so I'm building a representation in my mind. But I can't just show you my thoughts to get feedback on what parts I misremembered, so I have to produce a reconstruction or draw the original image from my memory. Alright, so this is what I've got. Now let's compare my drawing to the original image. Let's see, round plate, triangle slice of pizza, some cheese, some crust, tablecloth. Pretty good. For an AI, making a reconstruction would mean producing all the right pixel values to make a reconstruction. Arcane means clustering algorithm from before predicted classes for flowers based on how close the data points were to the averages. For images, we will have learned image representations instead of averages. After that step, just like before, the AI will have to correct itself. Previously, we updated the K clusters based on how well our predicted labels fit the data, but for images, we'd have to update the model's internal representations based on its reconstructions. There are different ways to use unsupervised learning in combination with representation learning so that an AI can compare images. Like for example, there's a type of neural network called an autoencoder, which uses the same basic principles of weights and biases to process inputs, pass data onto the hidden layers, and finally to a prediction output layer. If John Greenbott was programmed with an autoencoder, the input would be an image, the hidden layers would contain representations, and the output would be a full reconstruction of the original image. Which gets more accurate the more we train this AI. Theoretically, I could give John Greenbott a representation of a pizza and he could reconstruct the original pizza image. What's so powerful about unsupervised learning is that the world is our teacher. By looking around, taking in a lot of data, and predicting what we'll see next, we learn about how the world works and how it should be represented. When asked how AI will fulfill its grand ambitions, 2018 Turing Award winning professor, Jan LeCun said, we all know that unsupervised learning is the ultimate answer. So, I guess we better keep working on it. Unsupervised learning is a huge area of active research. The human brain is specially designed for this kind of learning and has different parts for vision, language, movement, and so on. These structures and what kinds of patterns our brains look for were developed over billions of years of evolution. But it's really tricky to build an AI that does unsupervised learning well, because AI systems can't learn exactly like humans often do, just by watching and imitating. Someone like us has to design the models and tell them how to look for patterns before turning them loose. Next time, we'll look at applying similar concepts to AI systems that find patterns in words and language and what's called natural language processing. See you then. Thanks to Wix for supporting PBS Digital Studios. Check out Wix.com if you're looking to make your own website. Wix is a platform that allows you to build a personalized website for almost any purpose, from promoting your business or creating an online shop to giving you a place for you to test out new ideas. Their technology allows you to create something unique no matter your skill level with templates and all-in-one management. If you'd like to check it out, you can go to wix.com.com. Go slash crash course or click the link in the description. Crash Course AI is produced in association with PBS Digital Studios. If you want to help keep Crash Course free for everyone forever, you can join our community on Patreon. And if you want to learn more about the math behind K-Means clustering, check out this video from Crash Course Statistics."""

def get_transcript():
	return """Thanks to Wix for supporting PBS Digital Studios. Hey, I'm Jabruro and welcome to Crash Course AI. So far in the series, we focused on artificial intelligence that uses supervised learning. These programs need a teacher to use labeled data to tell them right from wrong. And we humans have places where supervised learning happens, like classrooms with teachers. But that's not the only way we learn. We can also learn lots of things on our own by finding patterns in the world. We can look at dogs and elephants and know they're different animals without anyone telling us. Or we can even figure out the rules of a sport just by watching other people play. This kind of learning without a teacher is called unsupervised learning.
And in some cases, computers can do it too. The key difference between supervised and unsupervised learning is what we're trying to predict. In supervised learning, we're trying to build a model to predict an answer or label provided by a teacher. In unsupervised learning, instead of a teacher, the world around us is basically providing training labels. For example, if I freeze this video of a tennis ball right now, can you draw what could be the next frame? Unsupervised learning is about modeling the world by guessing like this. And it's useful because we don't need labels provided by a teacher. Babies do a lot of unsupervised learning by watching and imitating people. And we'd like computers to be able to learn like this as well.
This lets us utilize lots of freely available data in the world or on the internet. In many cases, one of the easiest ways to understand how AI can use unsupervised learning is by doing it ourselves.
So let's look at a few photos of flowers with no labels. The most basic way to model the world is to assume that it's made up of distinct groups of objects that share properties. So, for example, how many types of flowers are here? We can say there are two because there are two colors, purple and yellow. Or we can look at the petal shapes and divide them into round petals and tall vertical ones. Or maybe we have some more experience with flowers and realize that two of these are tulips, one is a sunflower, and the last one is a daisy. So there are three categories. Immediately recognizing different properties like this and creating categories is called unsupervised clustering. We don't have labels provided by a teacher, but we do have a key assumption about the world that we're modeling.
Certain objects are more similar to each other than others. We can program computers to perform clustering. But to do that, we need to choose a few properties of flowers we're interested in looking at, like how we picked color or shape just now. For a more realistic example, let's say I bought a packet of iris seeds to plant in my garden. After the flowers bloom, though, it looks like there were several different species of irises mixed up in that one packet. Now, I'm no expert gardener, but I can use some AI to help me analyze my garden. To construct the model, we have to answer two key questions. First, what observation can we measure? All of these flowers are purple, so that's probably not the best way to tell them apart. But different irises seem to have different petal lengths and widths, which we can measure and place on this graph with petal length on the y-axis and width on the x-axis. And second, how do we want to represent the world? We're going to stick to a very simple assumption here. There are clusters in our data. Specifically, we're going to say there are some number of groups called K clusters, but we don't know where they are.
To help us, we're going to use the K-means clustering algorithm. K-means clustering is a simple algorithm. All it needs is a way to compare observations, a way to guess how many clusters exist in the data, and a way to calculate averages for each cluster it predicts. In particular, we want to calculate the mean by adding up all data points in a cluster and dividing by the total number of points. Remember, unsupervised learning is about modeling the world, so our algorithm will have two steps. First, our AI will predict. What does the model expect the world to look like? In other words, which flowers should be clustered together because they're the same species? Second, our AI will correct or learn. The model will update its belief to agree with its observation of the world. To start the process, we have to specify how many clusters the model should look for. I'm guessing there are three clusters in the data, so that becomes the model's initial understanding of the world. And we're looking for K equals 3 averages or 3 types of viruses. But to start, our model doesn't really know anything.
So the averages are random and so are its predictions. Each data point, which is a flower, is given a label as type 1, type 2, or type 3. Based on the algorithm's beliefs. Next, our model tries to correct itself. The average of each cluster of data points should be in the middle. So the model corrects itself by calculating new averages. We can see those averages here, marked with X's, which gives us an updated model of the three, or so we guessed, types of viruses. But the graph is still pretty noisy. For example, it's a little weird that we have type 2 flowers so close to the average for type 3 flowers. But we did start with a random model, so we can't expect too much accuracy. Logically, we know that irises of the same species tend to have similar petals. So those data points should be clustered together.
Since we did a correction or learning step, we can repeat the process, starting with a new prediction step. Let's predict new labels using the X's that mark the averages of each label.
We'll give each data point the label of its closest X. Type 1, type 2, or type 3. And then we'll calculate new averages. Ah, that's better. But still not the cleanest clusters. So we can repeat the process again. Predict, learn, predict, learn. Eventually, the X's will stop moving and we will have a model of iris clusters created with unsupervised learning. Now, the ultimate question is, did we find meaningful patterns about the world with our AI? We made an assumption that there were three types of irises and we assumed that they had different petal lengths and widths. Was this true? Lucky for us, I have a friend who is a master gardener.
I showed him the real life flowers closest to each of the three averages and he said that type 1 is versicolor, type 2 is satosa, and type 3 is virginica. Three different iris species. We learned about the world from observation, which is what makes this unsupervised learning. Even though we relied a tiny bit on a teacher, the master gardener, for confirmation and help. Now that we've learned the basics, we can experiment with harder examples. Let's say we want to use unsupervised learning to sort a bunch of different photos, and not just three iris species. First, what observations can we measure? How much green there is, whether there's a nose and fur? To have a computer make these observations, we need to measure thousands of red, green, and blue pixels in each image. Second, how do we want to represent the world? Before, we were only working with two features, so we could just use the averages of the cluster data points and get meaningful extraction from it. But when dealing with images, we can't use the same method, because we won't get much meaning out of averaging colored pixels for what we want to accomplish. Somehow, we need the model to create a representation that tells us if two images are similar. There are meaningful patterns in the data that are more abstract than individual pixels, and finding them across many images is what's called representation learning. These patterns help us understand what's in the images and how to compare them to each other.
Representation learning happens both in supervised and unsupervised learning models, so we can do it with or without labels to find patterns in the world. To understand the basic idea of representation learning, check out this experiment.
I'm going to look at a picture really fast and then try and draw it. Ready, set, go. My eyes took in the picture and remembered important features, so I'm building a representation in my mind. But I can't just show you my thoughts to get feedback on what parts I misremembered, so I have to produce a reconstruction or draw the original image from my memory. Alright, so this is what I've got. Now let's compare my drawing to the original image. Let's see, round plate, triangle slice of pizza, some cheese, some crust, tablecloth. Pretty good.
For an AI, making a reconstruction would mean producing all the right pixel values to make a reconstruction. Arcane means clustering algorithm from before predicted classes for flowers based on how close the data points were to the averages. For images, we will have learned image representations instead of averages. After that step, just like before, the AI will have to correct itself.
Previously, we updated the K clusters based on how well our predicted labels fit the data, but for images, we'd have to update the model's internal representations based on its reconstructions. There are different ways to use unsupervised learning in combination with representation learning so that an AI can compare images. Like for example, there's a type of neural network called an autoencoder, which uses the same basic principles of weights and biases to process inputs, pass data onto the hidden layers, and finally to a prediction output layer. If John Greenbott was programmed with an autoencoder, the input would be an image, the hidden layers would contain representations, and the output would be a full reconstruction of the original image. Which gets more accurate the more we train this AI. Theoretically, I could give John Greenbott a representation of a pizza and he could reconstruct the original pizza image. What's so powerful about unsupervised learning is that the world is our teacher. By looking around, taking in a lot of data, and predicting what we'll see next, we learn about how the world works and how it should be represented. When asked how AI will fulfill its grand ambitions, 2018 Turing Award winning professor, Jan LeCun said, we all know that unsupervised learning is the ultimate answer. So, I guess we better keep working on it. Unsupervised learning is a huge area of active research. The human brain is specially designed for this kind of learning and has different parts for vision, language, movement, and so on. These structures and what kinds of patterns our brains look for were developed over billions of years of evolution. But it's really tricky to build an AI that does unsupervised learning well, because AI systems can't learn exactly like humans often do, just by watching and imitating. Someone like us has to design the models and tell them how to look for patterns before turning them loose. Next time, we'll look at applying similar concepts to AI systems that find patterns in words and language and what's called natural language processing. See you then. Thanks to Wix for supporting PBS Digital Studios. Check out Wix.com if you're looking to make your own website. Wix is a platform that allows you to build a personalized website for almost any purpose, from promoting your business or creating an online shop to giving you a place for you to test out new ideas. Their technology allows you to create something unique no matter your skill level with templates and all-in-one management. If you'd like to check it out, you can go to wix.com.com.
Go slash crash course or click the link in the description. Crash Course AI is produced in association with PBS Digital Studios. If you want to help keep Crash Course free for everyone forever, you can join our community on Patreon. And if you want to learn more about the math behind K-Means clustering, check out this video from Crash Course Statistics.."""