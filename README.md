# Real Time Chatroom

A real-time chat application that allows users to communicate instantly. This project is built using Django and Django templates, leveraging modern web technologies and supporting multiple chat rooms.

## Features

- **Real-Time Messaging:** Instant messaging using WebSockets.
- **Multiple Chat Rooms:** Users can join different chat rooms.
- **User Authentication:** Secure user registration and login.
- **Typing Indicators:** See when other users are typing.
- **Message History:** Persistent message storage and retrieval.
- **Responsive Design:** Works on both desktop and mobile devices.

## Technologies Used

- **Frontend:**
  - HTML, CSS, JavaScript
  - Django Templates

- **Backend:**
  - Django
  - Django Channels
  - WebSockets
  - PostgreSQL (or any preferred database)

- **Authentication:**
  - Django Authentication System

## Installation


   ```sh
   git clone https://github.com/erfan-hamidi/realtimechat.git 
   cd realtimechat
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
   
   Open your browser and navigate to http://localhost:8000.

## Screenshot
![screenshot](/screenshots/Screenshot%20from%202024-06-16%2018-25-31.png)
![screenshot](/screenshots/Screenshot%20from%202024-06-16%2018-30-26.png)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries, please contact erfan9757@gmail.com.
