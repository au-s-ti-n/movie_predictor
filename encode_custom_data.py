import json
import pandas as pd

# get df columns
df = pd.read_csv("data/final_data_min_lists.csv")
columns = df.drop('audience_rating', axis=1).columns
df['runtime'] = df['runtime'].apply(int)
max_runtime = max(df['runtime'])

# get encodings
with open('data/director_encoding.json', 'r') as file:
    director_encoding = json.load(file)

with open('data/actor_encoding.json', 'r') as file:
    actor_encoding = json.load(file)

with open('data/production_company_encoding.json', 'r') as file:
    production_company_encoding = json.load(file)

max_director = max(director_encoding.values()) + 1
max_actor = max(actor_encoding.values()) + 1
max_production_company = max(production_company_encoding.values()) + 1


# create encoding function
def encode_custom_data(data):
  new_data = {}

  if 'directors' in data:
    min_director = max_director
    for director in data['directors']:
      if director in director_encoding:
        encoding = director_encoding[director]
        min_director = min(min_director, encoding)
    new_data['directors'] = min_director / max_director
  else:
    new_data['directors'] = 1

  if 'actors' in data:
    actors = list(map(lambda actor: actor_encoding[actor] if actor in actor_encoding else max_actor, data['actors']))
    actors = sorted(actors)
    if len(actors) > 0:
      new_data['actors1'] = actors[0] / max_actor
    else:
      new_data['actors1'] = 1
    if len(actors) > 1:
      new_data['actors2'] = actors[1] / max_actor
    else:
      new_data['actors2'] = 1
    if len(actors) > 2:
      new_data['actors3'] = actors[2] / max_actor
    else:
      new_data['actors3'] = 1
  else:
    new_data['actors1'] = 1
    new_data['actors2'] = 1
    new_data['actors3'] = 1

  if 'production_company' in data and data['production_company'] in production_company_encoding:
      production_company = production_company_encoding[data['production_company']]
      new_data['production_company'] = production_company / max_production_company
  else:
    new_data['production_company'] = 1
  
  if 'genres' in data:
    for genre in data['genres']:
      if genre in columns:
        new_data[genre] = 1
  
  if 'content_rating' in data:
    content_rating = data['content_rating']
    if content_rating in columns:
      new_data[content_rating] = 1

  if 'runtime' in data:
    new_data['runtime'] = int(data['runtime']) / max_runtime
  else:
    new_data['runtime'] = df['runtime'].mean() / max_runtime

  new_data = pd.DataFrame(new_data, index=[0])
  new_data = new_data.reindex(columns=columns, fill_value=0)

  return new_data