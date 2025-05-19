


# main.py
if __name__ == "__main__":
    encoder = train_simclr_model(...)
    classifier = train_downstream_classifier(encoder, ...)
    evaluate_model(classifier, ...)
