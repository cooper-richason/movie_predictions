# AUTOGENERATED! DO NOT EDIT! File to edit: ../exporter.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'examples', 'demo', 'classify_image']

# %% ../exporter.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../exporter.ipynb 3
learn = load_learner('movie_predictions.pkl')

# %% ../exporter.ipynb 5
categories = ('Comedy 😂','Horror 👻')

def classify_image(img):
    prediction,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% ../exporter.ipynb 7
examples = ['barbie.jpg','hangover.jpg','theshinning.jpg','freddy.jpg']

demo = gr.Interface(classify_image, gr.Image(), gr.Label(), 
                    examples=examples, 
                    title = "Fun or RUN",
                    description = "Image classifier that predicts a movie's genre based on the movie poster!",
                    theme = gr.themes.Base())
demo.launch()
