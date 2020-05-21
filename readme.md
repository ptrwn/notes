## Notes
App to store and manage notes

## Setup

```
1. Create virtual environment
2. In the vistual environment, run:
pip install requirements.txt
3. Run migration:
python manage.py migrate
4. Initialize database:
python manage.py loaddata dump.json
5. The following users are created upon init: jdoe, vpupkin, ptutkin
Reset password

manage.py changepassword *username*  --- reset password, then log in 
```
