# main.py
from noapi import AnimalManager


def main():
    manager = AnimalManager()     # Create AnimalManager instance
    manager.display_dog_json()    # Call method to display dog JSON

if __name__ == "__main__":
    main()  # Entry point