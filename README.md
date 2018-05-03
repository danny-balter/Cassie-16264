# Cassie The Dating Advice Robot for 16-284
Danny Balter

Vinitha Ranganeni

# Purpose
Cassie’s primary goal is to provide dating advice to all of her users. She not only provides advice but remembers her users and adapts to them based on previous information that she has stored about them. She does not provide relatively serious advice, but more so exists as a conversational agent that provides humorous advice. 

# Our Original Goals

Allow Cassie to uniquely tailor her conversations with a user based on their user data and things they say while interacting with Cassie. e.g. “Cassie, I just got dumped” would result in Cassie being less funny and more kind, whereas “Cassie, my girlfriend cheated on me” would result in Cassie telling you to “dump her ass via text.”

Have Cassie adapt to a user overtime. Primarily through storing information from everything a user says to use in conversation with them later.

Source information all social media accounts that the user links to Cassie and use this information to adapt conversations. This would allow Cassie to perform Image analysis on things they like, content analysis to see who they interact with most in posts, comments, private messages, etc. Additionally, Cassie could source images of the user and possibly their significant others from social media so we can see the interactions between the two of them.

Enable “Hot word” detection so that Cassie can begin a conversation the moment you say her name. e.g. “Hey Cassie” will prompt her to start listening, as opposed to always being listening.

Allow Cassie to answer questions using Google’s API and email results if they are too long. e.g. “How do I get a girlfriend” would email you the first result from google which is a relative long guide.

# Reality Check
Adapting conversation to what a user says in real time is SUPER hard.

Having Cassie store information from the user as they speak is easy, but parsing it for things we actually want to store is quite challenging.

Sourcing info from social media should have been accomplished, but due to Facebook’s legal struggles, they removed the part of their api that we were trying to use and due to this loss in time there wasn’t an option to pivot to another service before the deadline.

There was a limited amount of time and some features such as using google’s cloud vision API were quite time consuming to get working.

# Goals We Achieved
Cassie has a user account system which includes, profiles with logins, passwords, and extra stored info such as age, gender, and relationship status.

Cassie has a login setup where if she recognizes your name she’ll ask you to login and if not she offers you the ability to make an account. This is followed by account setup if she doesn’t know you. Additionally, you can edit or delete your profile at any time. Finally, the logout command will log you out and shut Cassie down at any time.

Cassie has rules that she follows with her users. For example, if you give her information about your age and your S/O’s age that contradicts the half plus seven rule for dating, Cassie will tell you that “she is deeply uncomfortable” and will proceed to delete your account. This is part of her “funny” features.

Cassie’s coolest feature is her photo recognition.

If you ask her to analyze your relationship, she’ll prompt you for information about your S/O, followed by doing rule analysis. If she sees nothing wrong with your relationship from that, she’ll ask for pictures.
The pictures are analyzed for two things: (i) Labels and (ii) Facial Expressions. Currently Cassie doesn’t do anything with the labels but she does output them to the user in case they want to see them. For facial analysis, Cassie analyzes images and if there are two people, she’ll check their facial expressions to see if they’re having a good time. This allows her to make a judgement about your relationship and recommend whether or not it should continue. Obviously this is mostly silly and not to be taken literally.

# Big Struggles

We had two major struggles. The first was with the voice library. Cassie can communicate through either text or voice. She can take input and output in both of these modes. However, on my version of OSX the voice library doesn’t work properly, so she could only be a chatbot for the demo. The second was with Google's Cloud Vision API. Setting up the Google Cloud Vision API to do label and facial recognition was very challenging. The API is non obvious to setup and the credentials/package installation was challenging to figure out.

# Future Goals
There are many things we’d like to add into Cassie in the future. The first big thing is the option to link social media to the accoun, including Facebook, Instagram, etc. Cassie will be able to scan your account to get pictures of you, see your publicly listed relationship analysis, birthday, etc. so she doesn’t require you to input that information. Additionally, Cassie will be able to see your interactions with other people through posts and conversations, and given your permissions, read your messages to see who you interact with most. This will allow Cassie to recommend relationships to you that you may not have considered.

Adding more rules for judging relationships. It would be wonderful to change up the way she speaks based on your relationship, for example taking into account the gender of your S/O.

Adding in another photo analysis algorithm, for example Microsoft's Azure Recognition. Google is not always accurate and soetimes doesn't return good results, so having two sources of data would allow us to add better/more accurate information.

Storing permanent info about the users, as mentioned in the original goals section.

# Cassie Guide
Cassie.py -- main file that runs Cassie.

Login.py -- all login and account modification functions

Process.py -- processing user commands and images

Speech.py -- all speech libraries

