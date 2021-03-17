import pyautogui
import time


def wait(num):
    time.sleep(num)


def check_is_whatsapp():
    is_whatsapp = pyautogui.getActiveWindowTitle()

    while is_whatsapp != "WhatsApp":
        is_whatsapp = pyautogui.getActiveWindowTitle()
        if is_whatsapp == "WhatsApp":
            pass


class main:
    def __init__(self):
        self.contact_name = input("Enter the target contact:\n")
        self.message_to_send = input("Enter message to send: \n")
        self.iterations = int(input("How often do you want to send the message:\n"))

        print("Please open WhatsApp now, I will start automatically-->\r\n")

    def box_locator(self, photo):
        field_locator = pyautogui.locateOnScreen(photo)
        pyautogui.click(field_locator)


def click():
    pyautogui.click()


def write(msg):
    pyautogui.write(msg)
    pyautogui.press('enter')

if __name__ == '__main__':
    main = main()

    check_is_whatsapp()

    main.box_locator("search_box_light_mode.png")
    pyautogui.write(main.contact_name)
    pyautogui.move(xOffset = 0, yOffset=130)
    wait(1)
    click()
    wait(1)
    start = time.time()
    for i in range(main.iterations):
        wait(0.001)
        write(main.message_to_send)
    print(f"Total Time: {time.time() - start}s")
