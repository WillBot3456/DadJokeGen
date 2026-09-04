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
            ],
            "animals": [
                ("What do you call a sleeping bull?", "A dozer!"),
                ("Why don't eggs tell jokes?", "They'd crack each other up!"),
                ("What do you call a bear with no teeth?", "A gummy bear!"),
                ("Why do cows wear bells?", "Because their horns don't work!"),
                ("What do you call a fish wearing a bowtie?", "Sofishticated!"),
            ],
            "food": [
                ("What did the cookie say to the sad chocolate chip?", "Don't worry, you're semi-sweet!"),
                ("Why did the coffee file a police report?", "It got mugged!"),
                ("What do you call cheese that isn't yours?", "Nacho cheese!"),
                ("Why did the cookie go to the doctor?", "Because it felt crumbly!"),
                ("What's the difference between a poorly dressed man and a well-dressed llama?", "One wears a suit, the other is a well-suit llama!"),
            ],
            "occupations": [
                ("Why did the electrician fall off the ladder?", "He wanted to see if he was a live wire!"),
                ("What do you call a dentist's dog?", "A Molar retriever!"),
                ("Why did the teacher go to jail?", "For making too many assumptions!"),
                ("What do construction workers eat for lunch?", "Lunch bricks!"),
                ("Why did the gardener plant light bulbs?", "She wanted to grow a power plant!"),
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
