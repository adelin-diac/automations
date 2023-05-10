@REM This script assumes the functions folder is inside project directory

set create_react_app_frontend="C:\Users\adeli\Desktop\mh1_tutors\Applications\mh1_tutors"
set firebase_functions="C:\Users\adeli\Desktop\mh1_tutors\Applications\mh1_tutors\functions"


START "React Frontend" cmd /k "cd %create_react_app_frontend% & code . & npm start"

START "Firebase Functions" cmd /k "cd %create_react_app_frontend% & firebase emulators:start --only functions"
