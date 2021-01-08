from app.database.models.user import UserModel

mentor1 = UserModel(
    name='Mentor 1',
    email='mentor@example.com',
    username='mentor1',
    password='12345678x',
    terms_and_conditions_checked=True,
)
mentor1.available_to_mentor = True
mentor1.save_to_db()

mentor2 = UserModel(
    name='Mentor 2',
    email='mentor2@example.com',
    username='mentor2',
    password='12345678x',
    terms_and_conditions_checked=True,
)
mentor2.available_to_mentor = True
mentor2.save_to_db()

mentee1 = UserModel(
    name='Mentee 1',
    email='mentee1@example.com',
    username='mentee1',
    password='12345678x',
    terms_and_conditions_checked=True,
)
mentee1.is_email_verified = True
mentee1.need_mentoring = True
mentee1.save_to_db()


mentee2 = UserModel(
    name='Mentee 2',
    email='mentee2@example.com',
    username='mentee2',
    password='12345678x',
    terms_and_conditions_checked=True,
)
mentee2.is_email_verified = True
mentee2.need_mentoring = True
mentee2.save_to_db()

