import json
import numpy as np
import pandas as pd


df = pd.read_json('dataset.json')

with open('recommendation_data.json', 'r') as f:
    data = json.load(f)


cosine_sim = np.array(data['matrix'])
indices = data['indices']

def content_recommender(title, cosine_sim=cosine_sim, indices=indices):
    #check if title is in the dataset
    if title not in indices:
        return []
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    song_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[song_indices]


is_continue = True
while is_continue:
    title = input("Enter a song title or type 'exit' to exit: ")
    if title == 'exit':
        is_continue = False
        print("Thank you for using our recommender program!")
        continue
    recommendations = content_recommender(title)
    if len(recommendations) == 0:
        print(f"We don't have recommendations for {title}")

    else:
        for i, recommendation in enumerate(recommendations):
            print(f"{i+1}. {recommendation}")