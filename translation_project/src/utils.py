import random

def sample_data(dataset,num_samples=3):
    return random.sample(list(zip(dataset['input_text'],dataset['target_text'])),num_samples)