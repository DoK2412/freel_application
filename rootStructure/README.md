    Pythom v. 3.10;
    Базы данных PostgreSQL v. 14.3;
    Связь м базами данных SQLmodel v. 0.0.6;
    Фрейм FastAPI v. 0.78.0.


    Программа запускается из файла __main.py__, на данном этапе прорабатывается 
    авторизация пользователя в приложении.


// Регистрация //


    `POST` `/beg_registration`
     Request body (JSON):
    `{
      "first_name": "first_name",
      "last_name": "last_name",
      "phone": "number",
      "password": "password",
      "confirmations_password": "password"
    }`

    где: `first_name` - это  имя предполагаемого пользователя, 
         `last_name` - это  фамилия предполагаемого пользователя
         `phone` - номер телефона 
         `password` - пароль для регистрации пользователя,
         `confirmations_password` - подтверждение пароля пользоателя.
Response:

True

    {
      'status': 200, 
      'message': 'You will receive a call to your phone number, enter the last 4 digits'}
    }

False

    {
      "detail": "The user is in the database"
    }
    {
      "detail": "Passwords don't match"
    }
    {
      "detail": "The number does not meet the standard"
    }
    {
      "detail": "Error working with the number confirmation service"
    }

***
    `POST` `/end_registration`
     Request body (JSON):
    `{
        "code": "5724"
    }`

    где: `code` - код подтверждения регистрации. 
         
Response:

True


    {
      "status": 200,
      "message": "You have successfully registered"
    }

False

    {
      "detail": "The verification code is not correct"
    }

***
    `POST` `/entrancevk`
     Request body (JSON):
    `{
        `token`: "token"
    }`

    где: `token` - токен VK пользователя. 
         
Response:

True

    {
      "status": 200,
      "message": "Your VK account is successfully found and connected. Enter the phone number to confirm it."
    }

False

    {
      "detail": "VK token is not valid"
    }
***
    `POST` `/confirmation_phone`
     Request body (JSON):
    `{
        `phone`: "phone"
    }`

    где: `phone` - номер телефона пользователя. 
         
Response:

True

    {
      "status": 200,
      "message": "You will receive a call to your phone number, enter the last 4 digits"
    }

False

    {
      "detail": "The number does not meet the standard +7, 8, 7 and 10 digits per line"
    }
***
    `POST` `/confirmation_phone`
     Request body (JSON):
    `{
        `code`: "code"
    }`

    где: `code` - код подтверждения регистрации. 
         
Response:

True

    {
      "status": 200,
      "message": "You have successfully registered"
    }

False

    {
      "detail": "Confirmation keys are not correct"
    }