features = encoder(x)  # Freeze or fine-tune
logits = classifier(features)
loss = criterion(logits, labels)
