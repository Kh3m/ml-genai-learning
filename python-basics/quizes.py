model_accuracies = {"ResNet": 0.91, "AlexNet": 0.85, "VGG": 0.88, "Inception": 0.92}

model_accuracies_values = model_accuracies.values()
average_accuracy = 0
sum = 0
best_model = None
max_model = 0

for key in model_accuracies:
    sum += model_accuracies[key]
    if(model_accuracies[key] > max_model):
        best_model = key
    
average_accuracy = sum / len(model_accuracies_values)
model_accuracies["MobileNet"] = 0.89


print(model_accuracies)
print(average_accuracy, best_model)
