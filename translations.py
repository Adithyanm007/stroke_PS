# translations.py

LANGS = ["English", "Kannada", "Malayalam"]

ui_text = {
    "English": {
        "login_title": "Login",
        "username": "Username",
        "password": "Password",
        "login_button": "Login",
        "login_success": "Logged in successfully!",
        "login_error": "Invalid username or password",
        "select_language": "Select Language",
        "app_title": "Stroke Risk Prediction",
        "gender": "Your Gender",
        "hypertension": "Do you have hypertension?",
        "heart_disease": "Do you have heart disease?",
        "ever_married": "Did you ever marry?",
        "work_type": "Your Work Type",
        "residence_type": "Your Residence Type",
        "avg_glucose": "Average Glucose Level",
        "bmi": "Your BMI",
        "smoking_status": "Your Smoking Status",
        "age": "Your Age",
        "predict_button": "Predict Stroke Risk",
        "prediction_result": "Predicted risk of stroke:",
        "logout_button": "Logout"
    },
    "Kannada": {
        "login_title": "[ಲಾಗಿನ್]",
        "username": "[ಬಳಕೆದಾರ ಹೆಸರು]",
        "password": "[ಗುಪ್ತಪದ]",
        "login_button": "[ಲಾಗಿನ್]",
        "login_success": "[ಯಶಸ್ವಿಯಾಗಿ ಲಾಗಿನ್ ಆಗಿದ್ದು!]",
        "login_error": "[ಅಮಾನ್ಯ ಬಳಕೆದಾರ ಹೆಸರು ಅಥವಾ ಗುಪ್ತಪದ]",
        "select_language": "[ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ]",
        "app_title": "[ಸ್ಟ್ರೋಕ್ ಅಪಾಯ ಭವಿಷ್ಯವಾಣಿ]",
        "gender": "[ನಿಮ್ಮ ಲಿಂಗ]",
        "hypertension": "[ನಿಮಗೆ ಹೈಪರ್ಟೆನ್ಷನ್ ಇದೆಯೇ?]",
        "heart_disease": "[ನಿಮಗೆ ಹೃದಯ ರೋಗ ಇದೆಯೇ?]",
        "ever_married": "[ನೀವು ಮದುವೆಯಾಗಿದ್ದೀರಾ?]",
        "work_type": "[ನಿಮ್ಮ ಉದ್ಯೋಗ ಪ್ರಕಾರ]",
        "residence_type": "[ನಿಮ್ಮ ವಾಸಸ್ಥಳ ಪ್ರಕಾರ]",
        "avg_glucose": "[ಸರಾಸರಿ ಗ್ಲೂಕೋಸ್ ಮಟ್ಟ]",
        "bmi": "[ನಿಮ್ಮ ಬಿ.ಎಂ.ಐ]",
        "smoking_status": "[ನಿಮ್ಮ ಧೂಮಪಾನ ಸ್ಥಿತಿ]",
        "age": "[ನಿಮ್ಮ ವಯಸ್ಸು]",
        "predict_button": "[ಸ್ಟ್ರೋಕ್ ಅಪಾಯ ಮುನ್ಸೂಚನೆ]",
        "prediction_result": "[ಸ್ಟ್ರೋಕ್ ಅಪಾಯದ ಭವಿಷ್ಯವಾಣಿ:]",
        "logout_button": "[ಲಾಗ್ ಔಟ್]"
    },
    "Malayalam": {
        "login_title": "[ലോഗിൻ]",
        "username": "[ഉപയോക്തൃനാമം]",
        "password": "[പാസ്‌വേഡ്]",
        "login_button": "[ലോഗിൻ ചെയ്യുക]",
        "login_success": "[സഫലമായി ലോഗിൻ ചെയ്തു!]",
        "login_error": "[അസാധുവായ ഉപയോക്തൃനാമം അല്ലെങ്കിൽ പാസ്‌വേർഡ്]",
        "select_language": "[ഭാഷ തിരഞ്ഞെടുക്കുക]",
        "app_title": "[സ്ട്രോക്ക് അപകടം പ്രവചനം]",
        "gender": "[നിങ്ങളുടെ ലിംഗം]",
        "hypertension": "[നിങ്ങൾക്ക് ഹൈപ്പർടെൻഷൻ ഉണ്ടോ?]",
        "heart_disease": "[നിങ്ങൾക്ക് ഹൃദ്രോഗമുണ്ടോ?]",
        "ever_married": "[നിങ്ങൾ വിവാഹിതനല്ലേ?]",
        "work_type": "[നിങ്ങളുടെ ജോലി തരമെന്താണ്?]",
        "residence_type": "[നിങ്ങളുടെ താമസസ്ഥലം]",
        "avg_glucose": "[ശരാശരി ഗ്ലൂക്കോസ് നില]",
        "bmi": "[നിങ്ങളുടെ ബിഎംഐ]",
        "smoking_status": "[നിങ്ങളുടെ പുകവലി നില]",
        "age": "[നിങ്ങളുടെ പ്രായം]",
        "predict_button": "[സ്ട്രോക്ക് അപകടം പ്രവചിക്കുക]",
        "prediction_result": "[സ്ട്രോക്ക് അപകട സാധ്യത:]",
        "logout_button": "[ലോഗ്ഔട്ട്]"
    }
}

dropdown_vals = {
    "gender": {
        "English": ["Female", "Male"],
        "Kannada": ["[ಹೆಣ್ಣು]", "[ಗಂಡು]"],
        "Malayalam": ["[സ്ത്രീ]", "[പുരുഷൻ]"]
    },
    "yesno": {
        "English": ["No", "Yes"],
        "Kannada": ["[ಇಲ್ಲ]", "[ಹೌದು]"],
        "Malayalam": ["[ഇല്ല]", "[ഉണ്ട്]"]
    },
    "work_type": {
        "English": ["children", "Government job", "Never worked", "Private", "Self Employed"],
        "Kannada": [
            "[ಮಕ್ಕಳು]", "[ಸರ್ಕಾರಿ ಉದ್ಯೋಗ]", "[ಕೆಲಸಮಾಡಿಲ್ಲ]", "[ಖಾಸಗಿ]", "[ಸ್ವಯಂ ಉದ್ಯೋಗ]"
        ],
        "Malayalam": [
            "[കുട്ടികള്‍]", "[സർക്കാർ ജോലി]", "[ ജോലി ചെയ്യാത്തവർ]", "[പ്രൈവറ്റ്]", "[സ്വയം തൊഴില്‍]"
        ]
    },
    "residence": {
        "English": ["Rural", "Urban"],
        "Kannada": ["[ಗ್ರಾಮೀಣ]", "[ನಗರ]"],
        "Malayalam": ["[ഗ്രാമീണ]", "[നഗരീക]"]
    },
    "smoking": {
        "English": ["Never smoked", "Formerly smoked", "Smokes", "Unknown"],
        "Kannada": [
            "[ಧೂಮಪಾನ ಮಾಡಿರಲಿಲ್ಲ]", "[ಹಿಂದೆ ಧೂಮಪಾನ ಮಾಡಿದವರು]", "[ಧೂಮಪಾನ ನಿವಾಸಿಗಳು]", "[ಮಾಹಿತಿ ಇಲ್ಲ]"
        ],
        "Malayalam": [
            "[പുകവലി ചെയ്തിട്ടില്ല]", "[മുൻപ് പുകവലിച്ചവർ]", "[പുകവലിയ്ക്കുന്നവർ]", "[അജ്ഞാതം]"
        ]
    }
}
