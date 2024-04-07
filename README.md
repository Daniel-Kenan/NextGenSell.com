## Setting Up Environment Variables
To configure your application properly, you need to create a .env file in the root directory of your project. The .env file should contain the following environment variables:

```
DATABASE_URL=postgresql://...   # Database connection URL
USERNAME=<username>             # Username for superuser
EMAIL=<email>                   # Email for superuser
PASSWD=*************             # Password for superuser
DEBUG=True                      # Set to True for debugging, comment out for production
SSL_REDIRECT=False              # Set to False to disable SSL redirection, comment out for production
Make sure to replace placeholders like <username>, <email>, and ************* with your actual credentials.
```
Explanation of Environment Variables:
DATABASE_URL: This variable holds the connection URL for your PostgreSQL database.
USERNAME: The username of the superuser.
EMAIL: The email address of the superuser.
PASSWD: The password for the superuser. Make sure to keep it secure.
DEBUG: Set this to True if you want to run the app in debug mode. Debug mode provides additional information useful for development purposes.
SSL_REDIRECT: Set this to False if you want to disable SSL redirection. In production, it's usually recommended to enable SSL redirection for security reasons.
Note:
Ensure that the .env file is properly configured before running your application.
Do not share your .env file or sensitive information contained within it publicly.