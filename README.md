This is my first ever project.
# Introducing game recommender 3000 
> A game recommendation/prediction app for the Steam games.
> o/p accuracy is around 0.88. Do NOT expect the app to predict your next 20 games and solve your homework while simultaneously paying your taxes. It can make mistakes.
> this app is just for fun, maybe for a silly game recommendation. do not rely on it, as it can still make mistakes and inaccurate outputs. ( inputted for a free to play game and got a recommendation of game with 19.99$ ) 
### characteristics
- My first ever project related to machine learning.
- used logistic regression for the model. it has an accuracy of 0.88.
- frontend pipeline to backend done via streamlit and deployed the model on both huggingface and streamlit.
### challenges
while in the initial phase of the development of this applications, i encountered some little challenges and here are the solutions i had: 
- Trying to train models like SVM, KNN (with feeding it big data) with a free tier google colab (it didnt work) - switched to simple classification model (Logistic Regression)
- getting 0.0 accuracy for the model - I did a nonconventional workaround here by removing the ```train_test_split``` entirely and training the model wth all the data. got an accuracy of 0.88. went with 0.88 because i didn't want it to overfit and wanted a bit of generalization
- Data cleaning took me more time than expected. deleted around 500 features to keep it just 30 featues. initially the dataset had around 50k elements, and for the training purposes i had to shorten it to just 3000.hence the "3000" in the title.
