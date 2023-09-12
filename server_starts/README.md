# Server Starts

## **Links**

1. [React & Firebase Servers](#react_frontend_with_firebase_functionsbat)

## `react_frontend_with_firebase_functions.bat`

### **Description**

This BAT script is designed to simplify the process of starting your React frontend and Firebase functions local testing servers. When executed, the script opens two separate command prompt windows, one for each server. Additionally, it opens the respective directories in Visual Studio Code.

### **How to Use**

Place the provided BAT script in a directory of your choice.

Before running the script, ensure that the paths for the `create_react_app_frontend` and `firebase_functions` variables are correctly set to the locations of your React frontend and Firebase functions folders on your system. This script assumes that the `functions` directory for Firebase is located in the folder generated by `create-react-app`.

```batch
set create_react_app_frontend="path\to\react_frontend"
set firebase_functions="react_frontend\functions"
```

To start your local development environment, double-click the BAT script, or open a command prompt, navigate to the directory containing the script, and run the script by typing its filename and pressing Enter.

The script will start the React frontend and Firebase functions servers in separate command prompt windows, and it will open the respective directories in Visual Studio Code.

<br/>