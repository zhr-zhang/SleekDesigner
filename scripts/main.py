from batch_generator import DefaultBatchGenerator


if __name__ == "__main__":
    generator = DefaultBatchGenerator(
        image_shape="square",
        min_width=512,
        min_height=512,
        logo_size_ratio=0.7,
        power_range=range(1),
        use_round_shape=False,
    )
    generator.generate(
        draw=True,
        save=True,
    )
