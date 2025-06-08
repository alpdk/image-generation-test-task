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

    parser.add_argument('temperature', type=float,
                        help='Model temperature')

    parser.add_argument('model_name', type=str,
                        help='Gemini model name')

    parser.add_argument('gemini_api_key', type=str,
                        help='api key for the gemini')

    parser.add_argument('furniture_reference', type=str,
                        help='Name of the file with furniture picture')

    parser.add_argument('room_description', type=str,
                        help='Name of the file with room description')

    return parser.parse_args()

def main():
    args = parser()
    gen = InteriorGenerator(args)

    furniture_style = gen.extract_style_from_image(args.furniture_reference)
    print("Style:", furniture_style, end="\n\n")

    interior_text = gen.generate_interior(args.room_description, furniture_style)
    print("Interior Prompt:", interior_text, end="\n\n")

    gen.generate_image_prompt(interior_text)


if __name__ == '__main__':
    main()
