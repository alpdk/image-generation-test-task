import argparse

from generator import InteriorGenerator

def parser():
    """
    Parse command line arguments

    Returns:
         args (Namespace): parsed command line arguments
    """
    parser = argparse.ArgumentParser(description='Arguments for training a model')

    parser.add_argument('seed', type=int,
                        help='Seed for random generation')

    parser.add_argument('model_name', type=str,
                        help='Gemini model name')

    parser.add_argument('gemini_api_key', type=str,
                        help='api key for the gemini')

    return parser.parse_args()

def main():
    args = parser()
    gen = InteriorGenerator(args)

    furniture_style = gen.extract_style_from_image("test.jpg")
    print("Style:", furniture_style, end="\n\n")

    room_description = "Светлая гостиная с большим окном, деревянным полом и нейтральной цветовой гаммой."
    interior_text = gen.generate_interior(room_description, furniture_style)
    print("Interior Prompt:", interior_text, end="\n\n")

    image_prompt = gen.generate_image_prompt(interior_text)
    print("Prompt for image generator:", image_prompt, end="\n\n")


if __name__ == '__main__':
    main()
