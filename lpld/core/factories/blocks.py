def generate_block(*, block_type: str, value: dict):
    """
    Create the dictionary that can be passed into a StreamField.


    """
    return {
        "type": block_type,
        "value": value,
    }
