# Discord Bot with MySQL Database

This project demonstrates a simple Discord bot that uses a MySQL database to store and retrieve authentication tokens for different Discord servers.

## Prerequisites

Before running the bot, ensure you have the following installed:

- Python 3.x
- MySQL server
- Pipenv (optional but recommended for managing dependencies)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/discord-bot-mysql.git
   cd discord-bot-mysql
    ```
2. **Create a virtual environment:**

   ```bash
   phython3 -m venv venv
   source venv/bin/activate
    ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
    ```
4. **Create a MySQL database:** 

   ```bash
   mysql -u root -p
   CREATE DATABASE discord_bot;
   exit
    ```
5. **Add your Discord bot token to your database:**

   ```bash
   mysql -u root -p discord_bot 
   mysql -u root -p
   USE discord_bot; 
    CREATE TABLE tokens (token VARCHAR(255));
    INSERT INTO tokens (token) VALUES ('your-token-here');
    exit
    ```
6. **Create a .env file:**

   ```bash
   touch .env
    ```
7. **Add your database credentials to the .env file:**

   ```bash
   DB_HOST=your-host-here
   DB_USER=your-username-here
   DB_PASSWORD=your-password-here
   DB_DATABASE=discord_bot
    ```
8. **Create .gitignore file:**

   ```bash
   touch .gitignore
    ```
9. **Add the following to the .gitignore file:**

   ```bash
   venv/
   .env
    ```
10. **Check src for screenshots of the discord and bot in action!**


## Usage

To run the bot, simply execute the following command:

```bash
python3 bot.py
```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


