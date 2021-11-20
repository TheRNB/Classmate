![alt text](https://raw.githubusercontent.com/TheRNB/ClassBoom/main/logo.png)
# ClassBoom #

Classboom is an easy-to-use learning platform. This project was initially the class project of the Basic Programming course at the university of Tehran but I decided to move forward with it and make it more advanced. Classboom is designed with simplicity in mind and seeks to provide intuitive functionalities, especially the ability to use various different themes for it's front-end to suit every academy's needs.
- It currently supports the following features for professors:
    - Upload various lectures recordings
    - Assign as many assignments as necessary for every lesson
    - Evaluate the submitted answers to the assignments
- And it has the following features for students:
    - Stream the uploaded lectures
    - Submit answers to the assignments
    - View the scores given to the said answers

### Installaion: ###
#### VirtualEnv ####
first of all you should install VirtualEnv:
```pip install virtualenv
```
(if you don't already have pip installed, see [here](https://pip.pypa.io/en/stable/installation/))
now go to your desired directory and type in:
#### Creating a VirtualEnv ####
```
virtualenv ClassBoomVEnv
```
#### Activating the VirtualEnv ####
```
source ClassBoomVEnv/venv/bin/activate
```
#### Cloning the project ####
```
git clone https://github.com/TheRNB/ClassBoom.git
```
#### Installing the dependencies ####
```
cd ClassBoom
pip install -r requirements.txt
```

### Execution: ###
You can setup your desired setting in manage.py. Once done, you can run the server by:
```
python3 manage.py runserver
```
(Note: The project comes with a temporary front-end so that you can tune the settings to your liking and see wether you like it or not.)

### Contributors: ###
This project was mainly developed by [Aaron Bateni](https://github.com/TheRNB).
