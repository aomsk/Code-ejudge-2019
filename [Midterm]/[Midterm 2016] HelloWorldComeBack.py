"""HelloWorldComeBack"""
def main():
    """HelloWorldComeBack"""
    name = input()
    if name >= chr(65) and name <= chr(122):
        print("Hello %s."%name)
    else:
        print("สวัสดี %s"%name)

main()