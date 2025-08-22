This is my first ever project.
# Introducing game recommender 3000 
>A game recommendation/prediction app for Steam games.
>Model accuracy: ~0.88.
>Disclaimer: This app is just for fun. It may make mistakes — don’t expect it to predict your next 20 games, do your homework, or pay your taxes. For example, a free-to-play >input might still get a paid game recommendation ($19.99).

###Features

-My first machine learning project.

-Built with Logistic Regression, achieving ~0.88 accuracy.

-Frontend and backend connected via Streamlit; deployed on both Hugging Face and Streamlit Cloud.

#####Challenges & Solutions

-Training complex models (SVM, KNN) on large data: Free-tier Colab couldn’t handle it → switched to Logistic Regression for simplicity.

-0.0 accuracy issue: Removed train_test_split temporarily and trained on all data to get ~0.88 accuracy, balancing generalization and overfitting.

-Data cleaning: Reduced features from 500 to 30 and dataset size from 50k to 3000 entries (hence the “3000” in the title).
