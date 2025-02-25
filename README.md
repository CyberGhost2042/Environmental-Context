# 📖🔍 1v1 Retrieval-Augmented Generation (RAG) Showdown

Welcome to the **1v1 RAG Showdown** This experimentation pits two models against each other, ever had the doubt of utilizing general purpose model for a domain specific RAG pipeline? iykyk- to save on api billings 🧐 what would be the pros and cons of picking this rather than a domain specific model.

we will be evaluating their performance on 3 scenarios
```
1. ZERO TO LOW SIMILARITY CONTEXT WINDOWS
2. MEDIUM SIMILARITY CONTEXT WINDOWS 
3. HIGH SIMILARITY CONTEXT WINDOWS
```
These scenarios are formed by giving both models their ideal playground, utilizing same data and configuration.

## 🚀 Project Overview

In the realm of Natural Language Processing, Retrieval-Augmented Generation (RAG) combines the strengths of retrieval-based and generation-based models. This experimentation aims to understand the behaviour of models based on the pre-trained data (environmental data) via their generated outcomes.

Gemini and BioGPT will be given their ideal playgrounds to perform on queries from a user, The queries related to general health and health recommendations. RAG Pipeline is built on top of them to infer data from bio-medical literature.

```
Why Bio-medical literature ? Health recommendations required careful evaluation before suggesting,
ofc BioGPT will have a clear advantage but this vanilla model has smaller context windows 
lets see how it is utilizing it effectively
```

Lets start by understanding the following :

- **Compare** 
Suggestions given by the models and their relevancy with bio-medical literature data
- **Analyze** 
their performance on queries by slowing increasing complexity.
- **Provide** 
insights into their strengths and weaknesses in various contexts.

## 🛠️ METRICS ? meh just trust your gut bro
Just Kidding, we can analyze our raw suggestions in a metric called english 😌 and as well as some graphs for the nerds

- **Comprehensive Metrics:** Detailed performance metrics including accuracy, relevance, response time and utilization of previous generations.

## 📂 Structure

```
├── data
│   ├── research-articles directory/...          
│   ├── processed_gemini
│   ├── processed_biogpt
├── models/
│   ├── model_gemini     
│   ├── model_biogpt    
├── vectorization/
│   ├── data_preparation.ipynb
│   ├── model_evaluation.ipynb
├── config and settings/
│   ├── docker-compose.yaml
│   ├── example.env
│   ├── model settings.py
├── vector database/
│   ├── vectorstores.py
│   ├── RAG Pipeline.py
├── README.md
├── requirements.txt
└── showcase-results.txt
```

""" WILL BE UPDATING FILES BY CLEAN UP EVERYTHING BY TOMORROW """

<h1> Currently building Config file for this mini project</h1>
<img width="1078" alt="Screenshot 2025-02-14 at 6 57 58 AM" src="https://github.com/user-attachments/assets/f14f6696-21df-418f-a2d1-c3edb9e0cb00" />


