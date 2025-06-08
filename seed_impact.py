import os

from main import parser
from generator import InteriorGenerator
from PIL import Image
from tqdm import tqdm


def test_repeatability(num_runs=10):
    """
    Method for identifying amount of unique outputs from the model with respect to the seed and temperature

    Parameters:
         num_runs (int): number of repetitions
    """
    args = parser()

    style_results = []
    interior_results = []

    for i in tqdm(range(num_runs)):
        gen = InteriorGenerator(args)

        furniture_style = gen.extract_style_from_image(args.furniture_reference)
        interior_text = gen.generate_interior(args.room_description, furniture_style)
        gen.generate_image_prompt(interior_text, f"seed_impact_test_{i}.png")

        style_results.append(furniture_style)

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(path, f"images/generated/seed_impact_test_{i}.png")
        interior_image = Image.open(path)
        interior_results.append(interior_image)

    unique_styles = set(style_results)
    unique_interiors = set(interior_results)

    unique_styles = len(unique_styles)
    unique_interiors = len(unique_interiors)

    print(f"[Style Description] Unique in {unique_styles} of {num_runs} runs.")
    print(f"[Interior Generation] Unique in {unique_interiors} of {num_runs} runs.")


if __name__ == "__main__":
    test_repeatability()