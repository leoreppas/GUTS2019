# GUTS2019 - ChadDevelopers

Team members:
    Andrew Maclellan
    Angelos Perivolaropoulos
    Georgia Constantinou
    Leonidas Reppas
    Jordan Kalfas
    Minos Psarakis
    
## Inspiration / What it does
We've all been in an highly intoxicated state at one point in our student lives. One of the worst feelings is waking up and realising you've sent the wrong thing to the wrong person !! Our solution is Intexticated. Intexticated is here to analyse your messages using highly sophisticated machine learning techniques to provide you with restraint when you have none. We're here to save you from embarrassment from colleagues and worse exes.

## How we built it
We used the Twilion API and IBM Watson API for managing SMS and analysing texts respectively. Our architecture is split in two, with text handling being managed with twilio to manage conversations between parties while the Watson API and custom machine learning algorithms to process and make decisions on the content of the texts.

- Twilio: Twilio acts as a middleman for communication between the two parties. Every text sent is packaged and sent to the analysis portion of the app. This includes information about the relationship with the sender and what the message was.

- Watson API with machine learning decisions: This portion of the algorithm receives the SMS and relationship information from Twilio and processes it through the IBM Watson sentiment analysis API. This API outputs emotion metrics for texts limited to 5 emotions (sadness, joy, disgust, fear, anger). For each relationship we define a different decision parameter for what messages are okay to send. Our decision parameter was implemented using Linear Discriminant Analysis to find the optimal thresholding using a dataset of previously okay and not-okay messages.

- Linear Discriminant Analysis models: We created our own LDA models using custom created datasets to classify each text sent. We trained the models using those datasets using numpy and sklearn and saved them for use in the flask app that twilio uses for its infrastructure. The models are really fast and quite accurate for the amount of data we used.

## Challenges we ran into
Handling the state of the conversation because of the use of two Twilio flows simultaneously. We could not use the session state because we were using two different HTTP sessions.

We needed to create our own dataset to teach our decision model what types of sentiment were okay to send. This involved writing dummy messages with a label for each.

## Accomplishments that we're proud of
Creating an accurate classical machine learning model using our own datasets. Retrains in a matter of seconds. Using the Twilio API efficiently as a middleman between two people texting each other. We actually receive texts to our phones.

## What we learned
Twilio does UK based numbers (£13 spent sending texts to the US) How to use the Watson and Twilio API with their frameworks. Both very intuitive to use. How to implement a decision model using classical machine learning.

## What's next for Intexticated
Total global domination and saviour of embarrassment for the intoxicated human race.

## Built With
`ibm-watson` `python` `twilio`
