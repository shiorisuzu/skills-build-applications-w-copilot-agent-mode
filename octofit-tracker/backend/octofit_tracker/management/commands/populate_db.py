from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        tony = User.objects.create(email='tony@marvel.com', name='Tony Stark', team='marvel', is_superhero=True)
        steve = User.objects.create(email='steve@marvel.com', name='Steve Rogers', team='marvel', is_superhero=True)
        bruce = User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team='dc', is_superhero=True)
        clark = User.objects.create(email='clark@dc.com', name='Clark Kent', team='dc', is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, points=10, date=date.today())
        Activity.objects.create(user=steve, type='walk', duration=60, points=8, date=date.today())
        Activity.objects.create(user=bruce, type='strength', duration=45, points=12, date=date.today())
        Activity.objects.create(user=clark, type='run', duration=25, points=9, date=date.today())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=18)
        Leaderboard.objects.create(team=dc, points=21)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
