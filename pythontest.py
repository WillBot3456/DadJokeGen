import random

class DadJokeGenerator:
    """A class to generate hilarious (groan-worthy) dad jokes."""
    
    def __init__(self):
        self.jokes = {
            "puns": [
                ("Why don't scientists trust atoms?", "Because they make up everything!"),
                ("Did you hear about the claustrophobic astronaut?", "He just needed a little space!"),
                ("What do you call a fake noodle?", "An impasta!"),
                ("Why did the scarecrow win an award?", "He was outstanding in his field!"),
                ("How do you organize a space party?", "You planet!"),
                ("Why did the math book look sad?", "Because it had too many problems!"),
                ("Why did the bicycle fall over?", "Because it was two-tired!"),
                ("What do you call a snowman with a six-pack?", "An abdominal snowman!"),
                ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
                ("What do you call a belt made of watches?", "A waist of time!"),
                ("Why did the golfer bring two pairs of pants?", "In case he got a hole in one!"),
                ("Why did the computer go to the doctor?", "It caught a virus!"),
                ("Why did the cookie go to the doctor?", "Because it felt crummy!"),
                ("Why did the coffee file a police report?", "It got mugged!"),
                ("Why did the scarecrow win an award?", "Because he was outstanding in his field!"),
                ("Why did the chicken join a band?", "Because it had the drumsticks!"),
                ("Why did the bicycle fall over?", "Because it was two-tired!"),
                ("Why did the math book look sad?", "Because it had too many problems!"),
                ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
                ("Why did the golfer bring two pairs of pants?", "In case he got a hole in one!"),
                ("Why did the computer go to the doctor?", "It caught a virus!"),
            ],
            "animals": [
                ("What do you call a sleeping bull?", "A dozer!"),
                ("Why don't eggs tell jokes?", "They'd crack each other up!"),
                ("What do you call a bear with no teeth?", "A gummy bear!"),
                ("Why do cows wear bells?", "Because their horns don't work!"),
                ("What do you call a fish wearing a bowtie?", "Sofishticated!"),
                ("Why did the chicken go to the seance?", "To talk to the other side!"),
                ("Why did the cow go to space?", "To see the moooon!"),
                ("Why did the duck go to the doctor?", "Because it had the quacks!"),
                ("Why did the cat sit on the computer?", "To keep an eye on the mouse!"),
                ("Why did the dog sit in the shade?", "Because it didn't want to be a hot dog!"),
                ("Why did the owl get a promotion?", "Because it was outstanding in its field!"),
                ("Why did the horse go behind the tree?", "To change its jockeys!"),
                ("Why did the frog take the bus to work?", "Because his car got toad away!"),
                ("Why did the elephant bring a suitcase?", "Because it wanted to pack its trunk!"),
                ("Why did the penguin cross the road?", "To go to the ice cream shop!"),
                ("Why did the rabbit go to the party?", "Because it was a hare-raising experience!"),
                ("Why did the turtle cross the road?", "To get to the shell station!"),
                ("Why did the snake go to school?", "To learn hisself!"),
                ("Why did the kangaroo go to the party?", "Because it was a jumpin' good time!"),
                ("Why did the lion eat the tightrope walker?", "He wanted a well-balanced meal!"),
                ("Why did the giraffe get bad grades?", "Because it had its head in the clouds!"),
                ("Why did the monkey like the banana?", "Because it had appeal!"),
                ("Why did the parrot go to the party?", "Because it was a bird of a feather!"),
                ("Why did the sheep go to the party?", "Because it was a baa-rilliant time!"),
                ("Why did the pig go to the casino?", "Because it wanted to play the slop machines!"),
                ("Why did the raccoon go to the party?", "Because it was a trashy affair!"),
                ("Why did the skunk go to the party?", "Because it was a stinky situation!"),
                ("Why did the squirrel go to the party?", "Because it was nuts about fun!"),
                ("Why did the turkey go to the party?", "Because it was a gobbling good time!"),
            ],
            "food": [
                ("What did the cookie say to the sad chocolate chip?", "Don't worry, you're semi-sweet!"),
                ("Why did the coffee file a police report?", "It got mugged!"),
                ("What do you call cheese that isn't yours?", "Nacho cheese!"),
                ("Why did the cookie go to the doctor?", "Because it felt crumbly!"),
                ("What's the difference between a poorly dressed man and a well-dressed llama?", "One wears a suit, the other is a well-suit llama!"),
                ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
                ("Why did the banana go to the doctor?", "Because it wasn't peeling well!"),
                ("Why did the grape stop in the middle of the road?", "Because it ran out of juice!"),
                ("Why did the bread go to therapy?", "Because it kneaded help!"),
                ("Why did the lettuce break up with the tomato?", "Because it couldn't romaine calm!"),
                ("Why did the mushroom go to the party?", "Because he was a fungi to be with!"),
                ("Why did the pancake go to the doctor?", "Because it was feeling flat!"),
                ("Why did the ice cream cone go to school?", "Because it wanted to be a little cooler!"),
                ("Why did the watermelon go to the party?", "Because it was one in a melon!"),
                ("Why did the orange stop rolling down the hill?", "Because it ran out of juice!"),
                ("Why did the potato go to therapy?", "Because it had too many eyes on it!"),
                ("Why did the carrot get an award?", "Because it was outstanding in its field!"),
                ("Why did the corn go to school?", "Because it wanted to be a little corny!"),
                ("Why did the pepper go to school?", "Because it wanted to be a little spicy!"),
                ("Why did the onion go to therapy?", "Because it had too many layers of emotions!"),
                ("Why did the celery go to the party?", "Because it was a stalker!"),
                ("Why did the garlic go to the party?", "Because it was a little clove!"),
                ("Why did the tomato go to the party?", "Because it was a little saucy!"),
                ("Why did the cucumber go to the party?", "Because it was a little cool!"),
                ("Why did the zucchini go to the party?", "Because it was a little squashy!"),
                ("Why did the eggplant go to the party?", "Because it was a little purple!"),
                ("Why did the radish go to the party?", "Because it was a little spicy!")
            ],
            "occupations": [
                ("Why did the electrician fall off the ladder?", "He wanted to see if he was a live wire!"),
                ("What do you call a dentist's dog?", "A Molar retriever!"),
                ("Why did the teacher go to jail?", "For making too many assumptions!"),
                ("What do construction workers eat for lunch?", "Lunch bricks!"),
                ("Why did the gardener plant light bulbs?", "She wanted to grow a power plant!"),
                ("Why did the chef go to therapy?", "Because he had too many layers of stress!"),
                ("Why did the firefighter go to school?", "Because he wanted to be a little brighter!"),
                ("Why did the pilot go to therapy?", "Because he had too many ups and downs!"),
                ("Why did the musician go to therapy?", "Because he had too many notes of anxiety!"),
                ("Why did the actor go to therapy?", "Because he had too many roles to play!"),
                ("Why did the writer go to therapy?", "Because he had too many plot twists in his life!"),
                ("Why did the artist go to therapy?", "Because he had too many colors of emotions!"),
                ("Why did the scientist go to therapy?", "Because he had too many experiments of stress!"),
                ("Why did the lawyer go to therapy?", "Because he had too many cases of anxiety!"),
                ("Why did the doctor go to therapy?", "Because he had too many patients of stress!"),
                ("Why did the nurse go to therapy?", "Because she had too many patients of anxiety!"),
                ("Why did the engineer go to therapy?", "Because he had too many calculations of stress!"),
                ("Why did the architect go to therapy?", "Because he had too many blueprints of anxiety!"),
                ("Why did the accountant go to therapy?", "Because he had too many numbers of stress!"),
                ("Why did the banker go to therapy?", "Because he had too many accounts of anxiety!")
            ]
        }
        # Create joke ratings dictionary with joke as key
        self.ratings = {}
    
    def get_random_joke(self):
        """Get a random joke from any category."""
        all_jokes = [joke for category in self.jokes.values() for joke in category]
        setup, punchline = random.choice(all_jokes)
        return setup, punchline
    
    def get_joke_by_category(self, category):
        """Get a random joke from a specific category."""
        if category not in self.jokes:
            return None, f"Sorry, '{category}' isn't a valid category. Try: {', '.join(self.jokes.keys())}"
        setup, punchline = random.choice(self.jokes[category])
        return setup, punchline
    
    def get_all_categories(self):
        """Return all available joke categories."""
        return list(self.jokes.keys())
    
    def display_joke(self, setup, punchline, delay=0):
        """Display a joke with a delay before the punchline (for dramatic effect!)."""
        print(f"\n😄 {setup}")
        if delay > 0:
            import time
            print("   ...", end="", flush=True)
            time.sleep(delay)
            print()
        print(f"   {punchline}\n")
        return (setup, punchline)
    
    def rate_joke(self, joke_tuple, rating):
        """Rate a joke on a scale of 1-5."""
        if rating not in range(1, 6):
            return "Rating must be between 1-5!"
        
        if joke_tuple not in self.ratings:
            self.ratings[joke_tuple] = []
        
        self.ratings[joke_tuple].append(rating)
        avg_rating = sum(self.ratings[joke_tuple]) / len(self.ratings[joke_tuple])
        
        rating_stars = "⭐" * rating
        print(f"\n✅ You rated this joke: {rating_stars} ({rating}/5)")
        print(f"   Average rating: {avg_rating:.1f}/5 ({len(self.ratings[joke_tuple])} ratings)\n")
        return f"Thank you for rating! Average: {avg_rating:.1f}/5"
    
    def get_top_rated_jokes(self, num=5):
        """Get the top-rated jokes."""
        if not self.ratings:
            return []
        
        rated_jokes = []
        for joke, ratings in self.ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            rated_jokes.append((joke, avg_rating, len(ratings)))
        
        # Sort by average rating (descending), then by number of ratings
        rated_jokes.sort(key=lambda x: (x[1], x[2]), reverse=True)
        return rated_jokes[:num]
    
    def display_statistics(self):
        """Display rating statistics."""
        if not self.ratings:
            print("\n📊 No jokes have been rated yet!")
            return
        
        print("\n" + "=" * 60)
        print("📊 TOP-RATED JOKES 📊")
        print("=" * 60)
        
        top_jokes = self.get_top_rated_jokes(10)
        for i, (joke, avg_rating, num_ratings) in enumerate(top_jokes, 1):
            setup, punchline = joke
            stars = "⭐" * int(avg_rating) + ("✨" if avg_rating % 1 >= 0.5 else "")
            print(f"\n{i}. {stars} ({avg_rating:.1f}/5 - {num_ratings} ratings)")
            print(f"   Q: {setup}")
            print(f"   A: {punchline}")
        
        # Overall statistics
        all_ratings = [r for ratings in self.ratings.values() for r in ratings]
        avg_all = sum(all_ratings) / len(all_ratings) if all_ratings else 0
        print(f"\n{'=' * 60}")
        print(f"Overall average rating: {avg_all:.2f}/5")
        print(f"Total jokes rated: {len(self.ratings)}")
        print(f"Total ratings given: {len(all_ratings)}")
        print(f"{'=' * 60}\n")


def main():
    """Main function to run the dad joke generator."""
    generator = DadJokeGenerator()
    
    print("🎭 Welcome to the Dad Joke Generator! 🎭")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Get a random joke")
        print("2. Get a joke from a category")
        print("3. See all categories")
        print("4. View top-rated jokes")
        print("5. View statistics")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == "1":
            setup, punchline = generator.get_random_joke()
            joke = generator.display_joke(setup, punchline, delay=2)
            rate = input("Would you like to rate this joke? (1-5, or press Enter to skip): ").strip()
            if rate:
                try:
                    rating = int(rate)
                    generator.rate_joke(joke, rating)
                except ValueError:
                    print("Invalid rating. Please enter a number between 1-5.")
        
        elif choice == "2":
            categories = generator.get_all_categories()
            print(f"\nAvailable categories: {', '.join(categories)}")
            category = input("Enter a category: ").strip().lower()
            setup, punchline = generator.get_joke_by_category(category)
            if setup:
                joke = generator.display_joke(setup, punchline, delay=2)
                rate = input("Would you like to rate this joke? (1-5, or press Enter to skip): ").strip()
                if rate:
                    try:
                        rating = int(rate)
                        generator.rate_joke(joke, rating)
                    except ValueError:
                        print("Invalid rating. Please enter a number between 1-5.")
            else:
                print(punchline)
        
        elif choice == "3":
            print(f"\nAvailable categories: {', '.join(generator.get_all_categories())}")
        
        elif choice == "4":
            top_jokes = generator.get_top_rated_jokes(5)
            if not top_jokes:
                print("\n No jokes rated yet! Start rating to see the top jokes!")
            else:
                print("\n🏆 TOP 5 RATED JOKES 🏆")
                for i, (joke, avg_rating, num_ratings) in enumerate(top_jokes, 1):
                    setup, punchline = joke
                    stars = "⭐" * int(avg_rating) + ("✨" if avg_rating % 1 >= 0.5 else "")
                    print(f"\n{i}. {stars} ({avg_rating:.1f}/5 - {num_ratings} ratings)")
                    print(f"   Q: {setup}")
                    print(f"   A: {punchline}")
                print()
        
        elif choice == "5":
            generator.display_statistics()
        
        elif choice == "6":
            print("\n👋 Thanks for laughing! Have a dad-tastic day!\n")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
