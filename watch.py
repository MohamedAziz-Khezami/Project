import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(
        r"(?:.)*?src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"(?:.)*?",
        s,
        re.IGNORECASE,
    )
    if match is not None:
        video_id = match.group(1)
        return "https://youtu.be/" + video_id
    else:
        return None


if __name__ == "__main__":
    main()
