import threading
import os
from requests_html import *


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


def save_rom(link: dict, queue: list, saved: list, qntd: int):
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
                        print(
                            f"{bcolors.OKCYAN}Completed: {round((len(saved) / qntd) * 100,2)}% {bcolors.OKGREEN}({len(saved)} Saved){bcolors.ENDC} {bcolors.BOLD}{title_rom}",
                            end="\r")
                        write_rom.flush()
                        queue.remove(title_rom)
                else:
                    title_rom = next(title_rom_i)

            except:
                print(f"{bcolors.FAIL}(Faild){bcolors.ENDC} {bcolors.BOLD}{title_rom}")
                return
    except:
        return


if __name__ == "__main__":
    os.system("clear")
    queue_rom = []
    saved_rom = []
    links = {}
    URL = "https://archive.org/download/nointro.snes/"
    html_content = HtmlContent(URL)

    for i in html_content.request_html_response.html.find("a"):
        title = i.full_text
        if ".zip" in title or ".7z" in title:
            for j in i.links:
                links[title] = j
                break

    qntd_links = len(links)
    print(f"{bcolors.WARNING}{qntd_links} Roms found")
    t1 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t1.start()
    t2 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t2.start()
    t3 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t3.start()
    t4 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t4.start()
    t5 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t5.start()
    t6 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t6.start()
    t7 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t7.start()
    t8 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t8.start()
    t9 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t9.start()
    t10 = threading.Thread(target=save_rom, args=(links, queue_rom, saved_rom, qntd_links))
    t10.start()
