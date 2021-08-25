# Build a salad program
# Clsss definition

class Salad():
    """Modelling a salad"""

    def __init__(self, dressing, size):
        """Initialise attributes which describe the salad."""
        self.dressing = dressing # assign dressing value to the dressing attribute
        self.size = size # assign size value to size attribute

    def salad_mix(self, *ingredients):
        """Add ingredients to the salad."""
        for ingredient in ingredients:
            print(ingredient + " added to the " + self.dressing + " salad.")

    def choose_bowl(self):
        """Choose appropriate bowl for the salad size."""
        print(self.size + " bowl for the " + self.dressing + " salad\n")

# Create objects (instances) from the Salad class
salad_one = Salad('Ranch', 'Medium')
salad_two = Salad('Balsamic', 'Small')

#Call methods on Salad class objects
salad_one.choose_bowl()
salad_two.choose_bowl()
salad_one.salad_mix('letuce', 'cheese', 'carrots', 'celery', 'tomatoes')
salad_two.salad_mix('letuce', 'avocado', 'walnuts', 'croutons', 'tomatoes')