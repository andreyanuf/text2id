from text2id import Text2Id

if __name__ == "__main__":
    t2i = Text2Id()

    text = "Müller said 11 12 13"
    print(t2i.text_to_sequence(text))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text)))
    print(t2i.text_to_sequence(text, use_dict=False))
    print(t2i.sequence_to_text(t2i.text_to_sequence(text, use_dict=False)))