import threading
import tqdm


from requests_html import *
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class HtmlContent:
    def __init__(self, url: str):
        self.url = url
        self.session = HTMLSession()
        self.async_session = AsyncHTMLSession()
        self.request_html_response: HTMLResponse = None
        self.async_session.run(self._get_request)

    async def _get_request(self):
        self.request_html_response = self.session.get(self.url)

    def get_link(self):
        return self.request_html_response.html.links


def save_rom(link: dict, queue: list, saved: list):
    try:
        title_rom_i = iter(link)
        title_rom = next(title_rom_i)
        while len(links) > 0:
            try:
                if title_rom not in queue and title_rom not in saved:

                    queue.append(title_rom)
                    response = requests.get(URL + link[title_rom])
                    with open("./roms/" + title_rom, "wb") as write_rom:
                        write_rom.write(response.content)
                        saved.append(title_rom)
                        print(' ' * 110, end='\r')
                        print(f"{bcolors.OKCYAN}Completed: {int(len(saved)/len(link))}% {bcolors.OKGREEN}({len(saved)} Saved){bcolors.ENDC} {bcolors.BOLD}{title_rom}", end="\r")
                        write_rom.flush()
                        queue.remove(title_rom)
                else:
                    title_rom = next(title_rom_i)

            except:
                print(f"{bcolors.FAIL}(Faild){bcolors.ENDC} {bcolors.BOLD}{title_rom}")
                return
    except:
        return




queue_rom = []
saved_rom = []

URL = "https://archive.org/download/nointro.snes/"
html_content = HtmlContent(URL)

links = {}

for i in html_content.request_html_response.html.find("a"):
    title = i.full_text
    if ".zip" in title or ".7z" in title:
        for j in i.links:
            links[title] = j
            break
print(f"{bcolors.WARNING}({len(links)} Links found)")


if __name__ == "__main__":
    link = iter(links)
    t1 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t1.start()
    t2 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t2.start()
    t3 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t3.start()
    t4 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t4.start()
    t5 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t5.start()
    t6 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t6.start()
    t7 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t7.start()
    t8 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t8.start()
    t9 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t9.start()
    t10 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom))
    t10.start()
