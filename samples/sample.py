from text2id import Text2Id


def run_sample(t2i, text):
    print(t2i.text_to_sequence(text))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text)))
    print(t2i.text_to_sequence(text, use_dict=False))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text, use_dict=False)))


if __name__ == "__main__":
    t2i = Text2Id()
    print("Supported symbols: ", t2i.get_symbols())
    text = "Müller said 11 12 13"
    run_sample(t2i, text)

    text = "Hello 1234."
    run_sample(t2i, text)
