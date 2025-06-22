from server.app import app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

print("Seeding DB...")

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create sample data
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    guest = Guest(name="Trevor Noah", occupation="Comedian")
    episode = Episode(date="2024-06-21", number=1)
    appearance = Appearance(rating=5, guest=guest, episode=episode)

    db.session.add_all([guest, episode, appearance])
    db.session.commit()

print("Done.")
