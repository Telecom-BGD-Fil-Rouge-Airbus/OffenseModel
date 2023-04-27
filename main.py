from inference_offenseEval_taskA import load_model, predict_offense


clear_examples = ["You are so fat, you should lose weight.", "I'm grateful for all your help.", "I can't believe you're this stupid.", "Thank you for taking the time to talk to me about this.", "You're not good enough to do this.", "I'm sorry to bother you, but could you help me with this problem?", "I'm not racist, but...", "I'm impressed with the work you've done, it's truly remarkable."]
edge_examples = ["I'm very impressed by how ignorant you are"]

model_path = "./model_offenseEval_taskA.pth.tar"
model = load_model(model_path, verbose=True)

for text in clear_examples:
    
    prediction = predict_offense(model, text)
    print("text :",text)
    if prediction == 1:
        print("The phrase is offensive")
    else:
        print("The phrase is not offensive")