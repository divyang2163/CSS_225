def banner(title):
    print("=" * 60)
    print(title)
    print("=" * 60)

def prompt_choice(question, options):
    print(question)
    print("Options:", ", ".join(options))
    ans = input("> ").strip().lower()
    valid = [o.lower() for o in options]
    while ans not in valid:
        print("Please choose one of:", ", ".join(options))
        ans = input("> ").strip().lower()
    return ans

def checkpoint(label):
    return label

def restart_chapter(label):
    print("Restarting chapter...")
    return label
