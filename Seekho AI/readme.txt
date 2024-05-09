AI backend of the Seekho application
Flow:
1. get video transcription.
2. transcription is then segmented.
3. Mcqs and topics are then generated for each paragraph.
4. transcription and segmentation api will run on local servers while mcqs and topic apis will work on colab servers, 
    their api links will be made public and used through ngrok.
