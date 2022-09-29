"""SceneSwitch I"""
def main():
    """SceneSwitch I"""
    text = input()
    last = count = mode = onoff = 0
    while text != "End":
        text = float(text)
        onoff = (onoff+1)%2
        if onoff:
            if text - last > 6:
                mode = 0
            count += mode
            mode = (mode+1)%2
        text, last = input(), text
    print(count)

main()