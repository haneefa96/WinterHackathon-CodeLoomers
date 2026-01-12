def generate_story_from_image(labels: list[str], objects: list[str]) -> str:
    main_object = objects[0] if objects else "handcrafted product"
    material = labels[0].lower() if labels else "traditional materials"

    story = (
        f"This handcrafted {material} {main_object.lower()} "
        f"is made by skilled artisans using traditional techniques "
        f"passed down through generations."
    )

    return story
