from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    print("Seeding DB...")

    db.drop_all()
    db.create_all()

    u1 = User(username="admin")
    u1.set_password("admin")
    db.session.add(u1)

    g1 = Guest(name="Guest A", occupation="Actor")
    db.session.add(g1)

    e1 = Episode(date="2024-01-01", number=1)
    db.session.add(e1)

    a1 = Appearance(rating=5, guest_id=1, episode_id=1)
    db.session.add(a1)

    db.session.commit()
    print("Done.")
