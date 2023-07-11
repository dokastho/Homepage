"""Development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = (b'\x8a\xac\xb5\xd4\x19\xe6\xef',
              '\x18\xe7\xd4\x11\x05\xf3\x95\x9b\xbeD~-\xdf@[\xf8k')
SESSION_COOKIE_NAME = 'login'
# File Upload to var/uploads/
SITE_ROOT = pathlib.Path(__file__).resolve().parent.parent
# Database file is var/resume.sqlite3
DATABASE_FILENAME = SITE_ROOT/'var'/'homepage.sqlite3'
MY_LOGNAME = "dokastho"
UPLOAD_FOLDER = SITE_ROOT/'homepage'/'static'/'img'
